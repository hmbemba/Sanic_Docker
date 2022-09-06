from blueprints.simple import bp as user_bp
from blueprints.medium import bp as medium_bp
from sanic import Sanic
from pathlib import Path
from jinja2.loaders import FileSystemLoader
from jinja2 import Environment
from sanic.response import text

# app = Sanic("MyHelloWorldApp")
# app.blueprint([user_bp, medium_bp])

# @app.before_server_start
# def setup_template_env(app, _):
#     app.ctx.env = Environment(
#         loader=FileSystemLoader(Path(__file__).parent /"templates"),
#         autoescape=True,
#     )
app = Sanic("MySanicApp")

@app.get('/')
async def hello(request):
    return text("OK!")

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8000)
    app.run(host='127.0.0.1', port=7777)
