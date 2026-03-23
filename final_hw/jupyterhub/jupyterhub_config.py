c = get_config()
c.JupyterHub.authenticator_class = 'dummy'
c.DummyAuthenticator.password = 'admin'
c.Spawner.cmd = ['jupyter-lab']
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
