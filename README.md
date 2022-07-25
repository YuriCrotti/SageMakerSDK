# SageMakerSDK - Example Aplication 

The files must be run in SAGEMAKER notebook Instances.

# Project Organization
------------

    ├── README.md           <- The top-level README for developers using this project.
	│
    ├── requirements.txt    <- The requirements file to reproduce the development or production environment.
    │
    ├── Data                <- Data for use in this project.
	│	│
	│	├── bytebank_credito.csv        <- Complete csv file.
	│	├── df_bytebank_teste.csv       <- Test csv file.
	│	├── df_bytebank_treino.csv      <- Train csv file.
	│	└── ddf_bytebank_validacao.csv  <- Validation csv file.
	│  
    └─── src                <- Source code for use in this project.
		│
		├── DataExploration.ipynb       	<- Simple exploratory analysis.
		├── SageMakerSDK.ipynb          	<- Building a machine learning model in the SageMaker SDK.
		├── SageMakerSDKTuningHyper.ipynb	<- Building a Machine Learning Model with hyperparameter tuning in the SageMaker SDK.
		└── lambda_function.py      		<- Lambda function for model access.
		
# Project instructions


In this project is carried out:

	* Variable preparation and data loading in S3
	* Defining object paths and training parameters
	* Configuring training job settings
	* Preparation for Training
	* Model training and Hyperparameter Tuning 
	* Endpoint configuration
	* Model Logs and Created Artifacts
	* Deploying the model to the endpoint
	* Model call on endpoint
	* Checking information in Cloudwatch
	* Destruction of built artifacts

		
# Tools used

	
	SageMaker
		* Notebook instances
		* Pre-built images
		* Processing jobs
		* Training jos
		* Hyperparameter tuning jobs
	
	S3:
		* Bucket for storing training, testing and validation data.
		* Bucket for storage relating to models.
		
		
# References

- [Pricing SageMaker](https://aws.amazon.com/sagemaker/pricing/)  

- [Instancias do tipo M5](https://aws.amazon.com/ec2/instance-types/m5/)  

- [Instancias do tipo C5](https://aws.amazon.com/ec2/instance-types/c5/)  

- [Instancias do tipo P3](https://aws.amazon.com/ec2/instance-types/p3/)  

- [AWS Pricing Calculator](https://calculator.aws)  

- [Default of Credit Card Clients Dataset](https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset)  

- [Arquitetura do SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)  

- [Sage Maker e containers Docker](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)  

- [Imagens disponiveis para o AWS Sage Maker](https://github.com/aws/deep-learning-containers/blob/master/available_images.md)  

- [Containers Docker pre-feitos para Deep Learning](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html)  

- [Containers Docker pre-feitos para Scikit-Learn e SparkML](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-docker-containers-scikit-learn-spark.html)  

- [Extensão dos containers Docker](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/pytorch_extending_our_containers/pytorch_extending_our_containers.ipynb)  

- [Imagens para o Sage Maker para treinamento de Deep Learning](https://github.com/aws/deep-learning-containers/blob/master/available_images.md)  

- [Imagem de container do Sage Maker para o XGBoost](https://github.com/aws/sagemaker-xgboost-container)  

- [Imagens para o SparkML e Scikit-Learn](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-docker-containers-scikit-learn-spark.html)   

- [Scikit-learn-Container](https://github.com/aws/sagemaker-scikit-learn-container)  

- [Dockerfile do Scikit-Learn](https://github.com/aws/sagemaker-scikit-learn-container/blob/master/docker/0.23-1/base/Dockerfile.cpu)  

- [SageMaker Inference Toolkit](https://github.com/aws/sagemaker-inference-toolkit)  

- [SageMaker Training Toolkit](https://github.com/aws/sagemaker-training-toolkit)  

- [S3DataSource](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3DataSource.html)  

- [Sage Maker Python SDK:](https://sagemaker.readthedocs.io/en/stable/overview.html)  

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  