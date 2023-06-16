ARG LAMBDA_TASK_ROOT='/var/task'

FROM python:3.9-bullseye as build-image

# RUN apt-get update && \
#     apt-get install -y \ 
#     g++ \
#     make \ 
#     cmake \ 
#     unzip 

# CREATE var/task and CD 
ARG LAMBDA_TASK_ROOT
RUN mkdir -p ${LAMBDA_TASK_ROOT}
WORKDIR ${LAMBDA_TASK_ROOT}

# PROJECT dir setup
RUN mkdir /model_predict
RUN mkdir /api_prod
COPY ./model_predict ${LAMBDA_TASK_ROOT}/model_predict
COPY ./api_prod ${LAMBDA_TASK_ROOT}/api_prod

# PACKAGE/LIB setup
COPY requirements.txt .
RUN pip install -r requirements.txt \
    --target "${LAMBDA_TASK_ROOT}"

# SETUP ECR image
FROM public.ecr.aws/lambda/python:3.8
# SET
WORKDIR ${LAMBDA_TASK_ROOT}
COPY --from=build-image ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}
EXPOSE 8000
# using
# CMD ["uvicorn", "api_prod.main_api:app", "--reload", "--host", "0.0.0.0"]

CMD ["app_prod.main_api.handler"]

# ARG LAMBDA_TASK_ROOT='/var/task'
# FROM python:3.9-bullseye
# ARG LAMBDA_TASK_ROOT 
# WORKDIR ${LAMBDA_TASK_ROOT}
# RUN mkdir /model_predict
# RUN mkdir /api_prod
# COPY ./model_predict/ ${LAMBDA_TASK_ROOT}/model_predict 
# COPY ./api_prod/ ${LAMBDA_TASK_ROOT}/api_prod 
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# ENV FASTAPI_APP=main_api.py
# WORKDIR ${LAMBDA_TASK_ROOT}
# EXPOSE 8000
# CMD [ "uvicorn", "api_prod.main_api:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
