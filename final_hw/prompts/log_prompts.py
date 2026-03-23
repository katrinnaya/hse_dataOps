import mlflow

# Установить URI трекинга
mlflow.set_tracking_uri("http://localhost:5000")

# Создать эксперимент
mlflow.set_experiment("prompt-experiments")

with mlflow.start_run():
    # Версия 1 промпта
    mlflow.prompts.log_prompt(
        name="summarization_prompt",
        prompt="Summarize the following text: {text}",
        template_format="f-string",
        metadata={"version": "1.0", "author": "admin"}
    )
    
    # Версия 2 промпта
    mlflow.prompts.log_prompt(
        name="summarization_prompt_v2",
        prompt="Provide a brief summary for: {text}",
        template_format="f-string",
        metadata={"version": "2.0", "author": "admin"}
    )
    
    # Версия 3 промпта
    mlflow.prompts.log_prompt(
        name="summarization_prompt_v3",
        prompt="Create a concise summary of: {text}",
        template_format="f-string",
        metadata={"version": "3.0", "author": "admin"}
    )

print("Prompts successfully logged to MLflow!")
