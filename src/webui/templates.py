from functools import wraps
from typing import Any, Mapping

from starlette.background import BackgroundTask
from starlette.requests import Request


def with_template(name: str):
    def outer(func):
        @wraps(func)
        async def inner(request: Request, *args, **kwargs):
            templates = request.app.state.templates
            context = await func(request, *args, **kwargs)
            return templates.TemplateResponse(request, name, context)

        return inner

    return outer


def render_template(request: Request,
                    name: str,
                    context: dict[str, Any] | None = None,
                    status_code: int = 200,
                    headers: Mapping[str, str] | None = None,
                    media_type: str | None = None,
                    background: BackgroundTask | None = None, ):
    templates = request.app.state.templates
    return templates.TemplateResponse(request, name, context, status_code, headers, media_type, background)
