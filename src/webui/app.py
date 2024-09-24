from asgi_htmx import HtmxMiddleware
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from webui.templates import with_template


@with_template('pages/index.html')
async def homepage(_: Request):
    return {}


def create_app():
    routes = [
        Route('/', homepage),
        Mount('/static', StaticFiles(directory='static'), name='static')
    ]
    app = Starlette(debug=True,
                    routes=routes,
                    middleware=[
                        Middleware(HtmxMiddleware),
                    ]
                    )
    app.state.templates = Jinja2Templates(directory='templates')
    return app
