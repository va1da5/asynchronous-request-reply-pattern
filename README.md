# Asynchronous Request-Reply Pattern

This is a small project to tests [asynchronous request-reply pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply) using [FastAPI](https://fastapi.tiangolo.com/) and [Celery](https://docs.celeryproject.org/en/stable/).

## Conclusion

`Retry-After` HTTP header does not seem to properly instruct the browsers (Chrome,Firefox) to wait the predefined time period before retrying. It attempts to redirect multiple times until error gets presented about infinite redirect loop. Event though it does not work natively, such functionality could be implemented in the frontend part of the solution using [Javascript](https://medium.com/javascript-everyday/http-requests-polling-like-a-hero-with-rxjs-474a2e1fa057). Lastly, it is still a viable option when implementing integration or automation/orchestration projects.

## References

 - [Asynchronous Request-Reply pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/async-request-reply)
 - [MDN: Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After)
 - [Retry-after HTTP response header - does it affect anything?](https://stackoverflow.com/questions/3764075/retry-after-http-response-header-does-it-affect-anything)
