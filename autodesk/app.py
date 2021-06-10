from flask import Flask, request
from flask import has_request_context, request
import autodesk.util.logging

app = Flask(__name__)


@app.get("/")
def hello_world():
    app.logger.debug(f"request url: {request.url}")
    if "application/json" in request.headers["Accept"]:
        return {"message": "Hello, World!"}
    else:
        return "<p>Hello, World!</p>"


# The take does mention it but does not mention what it should do so,
# it just does what the get does
@app.post("/")
def hello_world_post():
    app.logger.debug(f"request url: {request.url}")
    if "application/json" in request.headers["Accept"]:
        return {"message": "Hello, World!"}
    else:
        return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()