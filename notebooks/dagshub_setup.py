import mlflow
import dagshub

mlflow.set_tracting_uri('https://github.com/AmanGupta8423/yt_chrome_plugin.git')
dagshub.init(repo_name = 'yt_chrome_plugin', repo_owner = 'Aman', mlflow = True)

with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name')