# gcloud-tf-org-helper

Generates resource definitions and outputs for nodes in the resource hierarchy for Google Cloud.  This is merely a templating tool which outputs valid Terraform.

The intent is to visualize a hierarchy in YAML and reduce the need for boilerplate in Terraform.  

## Installation

pip from source:

```shell script
pip install git+https://github.com/angstwad/gcloud-tf-org-helper.git
```

pip from clone:

```shell script
git clone pip install https://github.com/angstwad/gcloud-tf-org-helper.git
cd gcloud-tf-org-helper
pip install .
```

## Use

This reads an input YAML file to read the org structure.  A sample file is provided in this repo, [sample_hierarchy.yaml](./sample_hierarchy.yaml)

```shell script
$ gcphc --help
usage: gcphc [-h] [-o OUTFILE] org_file

positional arguments:
  org_file              Org hierarchy YAML file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        File to write; default: organization.tf
```

## Disclaimer
This repository and its contents are not an official Google Product.
