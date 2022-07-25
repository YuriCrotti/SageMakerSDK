# SageMakerSDK - Example Aplication 

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
------------

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