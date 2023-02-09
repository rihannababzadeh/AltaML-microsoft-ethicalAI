

setup-environment:
	@echo "setting up the virtual environment"
	@conda env create -f environment.yaml

predict-emotion-data-pipeline:
	@echo "Recognizing emotion from speech for data pipeline..."
	@python ./workflow/app.py \
		--config_path=config.yaml \

predict-emotion-file:
	@echo "Recognizing emotion from speech for the file..."
	@python ./workflow/app.py \
		--config_path=config.yaml \
		--input_file=data/*.wav

remove-environment:
	@conda env remove -n hackathon2022-scale