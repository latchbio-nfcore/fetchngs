# nf-core/fetchngs

![nf-core/fetchngs](https://latch-public.s3.amazonaws.com/test-data/35446/images/nf-core-fetchngs_logo_light.png)
## Introduction

**nf-core/fetchngs** is a bioinformatics pipeline to fetch metadata and raw FastQ files from public databases. It currently supports SRA / ENA / DDBJ / GEO IDs ([see usage docs](https://nf-co.re/fetchngs/usage#introduction)).

![nf-core/fetchngs metro map](https://latch-public.s3.amazonaws.com/test-data/35446/images/nf-core-fetchngs_metro_map_grey.png)

## Usage

Prepare a samplesheet like:

`ids.csv`:

```csv
SRR9984183
SRR13191702
ERR1160846
ERR1109373
DRR028935
DRR026872
