FROM python:3.14-slim
RUN pip install jupyterhub configurable-http-proxy jupyterlab
EXPOSE 8000
CMD ["jupyterhub", "--config", "jupyterhub_config.py"]
