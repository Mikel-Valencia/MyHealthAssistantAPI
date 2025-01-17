# MyHealthAssistantAPI

MyHealthAssistantAPI forms the API Rest for MyHealthAssistant project.

API version: 0.1.0.

## Versioning

The project uses a 3-part version numbers, major.minor.patch, where it increments:

* major when they make incompatible API changes,
* minor when they add functionality in a backwards-compatible manner, and
* patch, when they make backwards-compatible bug fixes.

## Backend tests

To test the backend run:

```console
$ bash ./scripts/test.sh
```

The tests run with Pytest, modify and add tests to `./myhealthassistantapi/tests/`.

If you use GitHub Actions the tests will run automatically.

### Test Coverage

When the tests are run, a file `htmlcov/index.html` is generated, you can open it in your browser to see the coverage of the tests.

## Running the API

### Development mode

```console
$ bash ./scripts/dev.sh
```

```console
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/myHealthAssistant/myHealthAssistantAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Interactive API docs

Go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.
Provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>

## License

This project is licensed under the terms of the MIT license.

## Links

[Homepage](https://github.com/Mikel-Valencia/MyHealthAssistantAPI)
[Issues](https://github.com/Mikel-Valencia/MyHealthAssistantAPI/issues)