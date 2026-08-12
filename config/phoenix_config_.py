from phoenix.otel import register
 
tracer_provider = register(
    project_name="langchain-academy",
    auto_instrument=True,
)