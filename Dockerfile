ARG LAMBDA_TASK_ROOT='/var/task'

FROM python:3.8-buster as build-image

RUN apt-get update && \
    apt-get install -y \ 
    g++ \
    make \ 
    cmake \ 
    unzip 

ARG LAMBDA_TASK_ROOT 
RUN mkdir -p ${LAMBDA_TASK_ROOT}

# PROJECT dir setup
COPY ./model_predict ${LAMBDA_TASK_ROOT}
COPY ./api_prod ${LAMBDA_TASK_ROOT}

# PACKAGE/LIB setup
COPY requirements.txt .
RUN pip3 install -r requirements.txt \
    --target "${LAMBDA_TASK_ROOT}"

# SETUP ECR image
FROM public.ecr.aws/lambda/python:3.8

# SET work directory
WORKDIR ${LAMBDA_TASK_ROOT}

# SET
COPY --from=build-image ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# using
CMD ["uvicorn", "api_prod.main_api:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["app_prod.main_api.handler"]