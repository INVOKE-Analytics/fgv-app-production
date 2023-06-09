# Details

## Local development
1. `best.pt` (model inference file) saved in `/model_output` directory locally.
2. Inference output saved in `/inference_out` directory locally. 

## Cloud development
1. `best.pt` model artifact should be store in S3.
2. Inference output (image with bbox) artifact should be store in S3. 
3. Project container would be push to ECR. 
4. The container then will be connected to Lambda (host) and API Gateway (API).

# Todo
* [ ] Full Cloud Deployment
    ##  Next Sprint
    * [ ] Storing model artifact in S3 
    * [ ] Storing inference output in S3 
    * [ ] Setup container 
    * [ ] Setup API Gateway 
    * [ ] Setup Lambda  