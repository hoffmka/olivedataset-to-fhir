# OPHTHAL-TO-FHIR
## Description
This work is intended to contribute to the standardization of ophthalmological data. This study describes the process of mapping ophthalmologic data from source systems to FHIR. Ophthalmology experts defined the following clinical parameters that are relevant for a clinical dashboard to be developed: Visual acuity, intraocular pressure and the OCT biomarkers retinal thickness, DRIL, HIF, VMT and PET detachment.

Two data sets were used for the mapping process:
1) the freely available [OLIVES dataset](https://doi.org/10.48550/arXiv.2209.11195) and
2) Real-world data from the clinical information system "Turbomed" of the non-university hospital in Chemnitz.

After ophthalmologists and FHIR specialists discussed the content of the data to be mapped, FHIR specialists developed sample ETL processes taking into account existing specifications such as the [Eyes on FHIR project](https://build.fhir.org/ig/HL7/fhir-eyecare-ig/index.html). The resulting FHIR resources are intended to improve interoperability and compatibility within the Medical Informatics Initiative (MII). The evaluation and validation by experts underlines the effectiveness and benefits of the mapping process.

## Quickstart
To bootstrap the project, create a virtual environment and install the requirements from ``requirements.txt``:

```shell
virtualenv env
source path/to/env/bin/activate
cd path/to/ophthal-to-fhir/repository
pip install -r requirements.txt
```

## Project structure
1. Directory `resources` contains classes for setting up FHIR resources.

2. Directory `examples`  contains resources for the ETL processes that can be used to map the data from the OLIVES dataset to FHIR (dir `olivesdataset`) and resources for mapping real world data from the clinical information system Turbomed (dir `skc`).

3. Directory `docs` contains further documentation of the resources and the mapping processes.

## Mapping of the OLIVES dataset

After installation of the requirements (see section Quickstart), move to the directory `examples/olivesdataset` and execute the python script `olivesdataset_etl.py`. A directory `output` with subdirectories will be created that contains the constructed FHIR resources in Form of json files. Example FHIR resources can be viewed section [OLIVES dataset example resources](docs/olivesdataset_example_resources.md).

```shell
cd path/to/ophthal-to-fhir/examples/olivesdataset
python olivesdataset_etl.py
```

For additional information and tools, see section [Auximiliary](docs/auximiliary.md)

## Authors and acknowledgment
- Katja Hoffmann
- Holger Langner
- Yuan Peng
- Arunodhayan Sampath Kumar
- Danny Kowerko