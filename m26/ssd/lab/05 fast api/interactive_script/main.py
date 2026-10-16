import asyncio
import time

import jwt
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# ---------------------------------------------------------
# Slide 4: Interactive Walkthrough 1 - Minimal App Setup
# ---------------------------------------------------------
app = FastAPI(
    title="FastAPI Architecture to Production Lab",
    description="Interactive companion script for lecture walkthroughs.",
    version="1.0.0",
)

# ---------------------------------------------------------
# Slide 13: CORS Middleware
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Slide 4: Root Endpoint
# ---------------------------------------------------------
@app.get("/", tags=["Slide 4: Getting Started"])
def read_root():
    """Slide 4: Minimal ASGI entry point."""
    return {"message": "my first fastapi server"}


# ---------------------------------------------------------
# Slide 3: WSGI vs. ASGI (Non-blocking Concurrency)
# ---------------------------------------------------------
@app.get("/fast", tags=["Slide 3: Concurrency & ASGI"])
async def fast():
    """Slide 3: Non-blocking async sleep yields execution to event loop."""
    await asyncio.sleep(2)
    return {"message": "Done after non-blocking 2s sleep"}


# ---------------------------------------------------------
# Slides 6 & 7: Path vs. Query Parameters & Type Validation
# ---------------------------------------------------------
@app.get("/todos/{todo_id}", tags=["Slide 6-7: Parameters & Validation"])
def get_todo(todo_id: int):
    """
    Slide 7: Dynamic path capture with auto type casting.
    Try /todos/42 (HTTP 200) vs /todos/abc (HTTP 422 Unprocessable Entity).
    """
    return {"todo_id": todo_id, "type": str(type(todo_id))}


@app.get("/items/search", tags=["Slide 6-7: Parameters & Validation"])
def search_items(category: str = "books", skip: int = 0, limit: int = 10):
    """
    Slide 6: Query parameters with default values for filtering/pagination.
    Try /items/search?category=electronics&skip=5&limit=20
    """
    return {"category": category, "skip": skip, "limit": limit}


# ---------------------------------------------------------
# Slides 8, 9 & 11: Pydantic Schemas & In-Memory CRUD
# ---------------------------------------------------------
class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None


# In-memory storage mock
items_db: list[dict] = [
    {"id": 1, "name": "Laptop", "price": 999.99, "description": "Workstation"},
    {"id": 2, "name": "Notebook", "price": 4.50, "description": None},
]


@app.get("/items", response_model=list[Item], tags=["Slide 11: In-Memory CRUD"])
def list_items():
    return items_db


@app.get("/items/{item_id}", response_model=Item, tags=["Slide 11: In-Memory CRUD"])
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post(
    "/items", status_code=status.HTTP_201_CREATED, tags=["Slide 11: In-Memory CRUD"]
)
def create_item(item: Item):
    # Slide 8-9: Pydantic validates payload schema before running function body
    for existing in items_db:
        if existing["id"] == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db.append(item.model_dump())
    return {"message": "Item created successfully", "item": item}


@app.delete("/items/{item_id}", tags=["Slide 11: In-Memory CRUD"])
def delete_item(item_id: int):
    global items_db
    items_db = [i for i in items_db if i["id"] != item_id]
    return {"message": f"Item {item_id} deleted"}


# ---------------------------------------------------------
# Slide 12: Jinja2 Templating
# ---------------------------------------------------------
@app.get("/render", response_class=HTMLResponse, tags=["Slide 12: Fullstack & Jinja2"])
def render_page(request: Request, user_name: str = "Student"):
    """
    Slide 12: Renders dynamic HTML via Jinja2 interpolation {{ ... }}
    No external template folder required for quick testing.
    """
    from jinja2 import Template

    html_template = """
    <!DOCTYPE html>
    <html>
        <head><title>FastAPI Jinja Demo</title></head>
        <body style="font-family: Arial; padding: 2rem;">
            <h2>Welcome to Systems Lab, {{ user_name }}!</h2>
            <p>Expression evaluation: 10 + 20 = {{ 10 + 20 }}</p>
            <h3>Current Items in DB:</h3>
            <ul>
                {% for item in items %}
                    <li><b>{{ item.name }}</b> - ${{ item.price }}</li>
                {% endfor %}
            </ul>
        </body>
    </html>
    """
    template = Template(html_template)
    rendered_content = template.render(user_name=user_name, items=items_db)
    return HTMLResponse(content=rendered_content)


# ---------------------------------------------------------
# Slides 14 & 15: Stateless Auth (JWT) & Dependency Injection
# ---------------------------------------------------------
JWT_SECRET = "super-secret-key-change-in-production"
JWT_ALGORITHM = "HS256"


def sign_jwt(user_id: str) -> dict[str, str]:
    """Slide 14: Encodes user payload and 10-minute expiry into a signed JWT."""
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}


def decode_jwt(token: str) -> dict:
    """Slide 14: Validates JWT signature and expiration timestamp."""
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded if decoded.get("expires", 0) >= time.time() else {}
    except Exception:
        return {}


# Slide 15: Declarative Route Guard with HTTPBearer
security = HTTPBearer()


async def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token or expired token.",
        )
    return payload


class PostSchema(BaseModel):
    title: str
    content: str


posts_db: list[dict] = []


@app.post("/auth/login", tags=["Slide 14-15: JWT & Security"])
def login(username: str):
    """Generates a bearer token for testing guarded routes."""
    return sign_jwt(user_id=username)


@app.post(
    "/posts",
    dependencies=[Depends(verify_jwt)],
    tags=["Slide 14-15: JWT & Security"],
)
async def add_post(post: PostSchema):
    """
    Slide 15: Guarded endpoint using dependency injection.
    Requires header: 'Authorization: Bearer <token>'
    """
    posts_db.append(post.model_dump())
    return {"data": "Post added securely", "post": post}


@app.get("/posts", tags=["Slide 14-15: JWT & Security"])
def get_posts():
    return {"posts": posts_db}
