# polars


# Covid-19 Data Lake
https://aws.amazon.com/covid-19-data-lake/


# AWS free public datasets
https://registry.opendata.aws/nyc-tlc-trip-records-pds/
https://aws.amazon.com/marketplace/pp/prodview-okyonroqg5b2u?sr=0-1&ref_=beagle&applicationId=AWSMPContessa#overview
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
https://github.com/aws-samples/cloud-experiments/tree/master/experiments/notebooks/exploring-data


# Installing environment using mamba:

## If not already installed, install mamba:
```bash
brew install micromamba
```

Update mamba
```bash
micromamba self-update
```

Create the mamba environment using this file by running the following command in your terminal:
```bash
mamba env create -f environment.yaml
```

This will create a new mamba environment named polars with Python 3.10, pip, pandas, and Faker, and more installed. You can activate the environment with the command:
```bash
mamba activate polars
```

To update a mamba environment based on an updated environment.yaml file, you can use the following command:
```bash
mamba env update --file environment.yaml --prune
```

To list all installed packages in the current environment:
```bash
mamba list
```


# Installing environment using conda:

You can use the same commands as above, but replace mamba with conda.



# Running the synthetic data generation program

```bash
python generate_data.py 100 --seed 42
```

To get help, run:
```bash 
python generate_data.py --help
```