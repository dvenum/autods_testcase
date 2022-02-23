FROM python:3.7-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


FROM base AS python-deps

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

ENV USERNAME=autods
RUN useradd --create-home ${USERNAME}
WORKDIR /home/${USERNAME}
USER ${USERNAME}

COPY . ${APP_DIR}

EXPOSE 80

ENTRYPOINT [ "/usr/bin/env", "sh", "-c", "docker/app/run_app.sh" ]
