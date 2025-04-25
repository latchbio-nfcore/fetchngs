import typing
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import typing_extensions
from flytekit.core.annotation import FlyteAnnotation
from latch.types.directory import LatchDir, LatchOutputDir
from latch.types.file import LatchFile
from latch.types.metadata import LatchRule, NextflowParameter

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters


class Download(Enum):
    ftp = "ftp"
    aspera = "aspera"
    sratools = "sratools"


generated_parameters = {
    "input": NextflowParameter(
        display_name="Input File",
        type=LatchFile,
        default=None,
        description="File containing SRA/ENA/GEO/DDBJ identifiers one per line to download their associated metadata and FastQ files.",
    ),
    "ena_metadata_fields": NextflowParameter(
        display_name="ENA Metadata Fields",
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description="Comma-separated list of ENA metadata fields to fetch before downloading data.",
    ),
    "sample_mapping_fields": NextflowParameter(
        display_name="Sample Mapping Fields",
        type=typing.Optional[str],
        default="experiment_accession,run_accession,sample_accession,experiment_alias,run_alias,sample_alias,experiment_title,sample_title,sample_description",
        section_title=None,
        description="Comma-separated list of ENA metadata fields used to create a separate 'id_mappings.csv' and 'multiqc_config.yml' with selected fields that can be used to rename samples in general and in MultiQC.",
    ),
    "nf_core_pipeline": NextflowParameter(
        display_name="nf-core Pipeline",
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description="Name of supported nf-core pipeline e.g. 'rnaseq'. A samplesheet for direct use with the pipeline will be created with the appropriate columns.",
    ),
    "nf_core_rnaseq_strandedness": NextflowParameter(
        display_name="nf-core rnaseq Strandedness",
        type=typing.Optional[str],
        default="auto",
        section_title=None,
        description="Value for 'strandedness' entry added to samplesheet created when using '--nf_core_pipeline rnaseq'.",
    ),
    "download_method": NextflowParameter(
        display_name="Download Method",
        type=Download,
        default="ftp",
        section_title=None,
        description="Method to download FastQ files. Available options are 'aspera', 'ftp' or 'sratools'. Default is 'ftp'.",
    ),
    "skip_fastq_download": NextflowParameter(
        display_name="Skip FASTQ Download",
        type=bool,
        default=None,
        section_title=None,
        description="Only download metadata for public data database ids and don't download the FastQ files.",
    ),
    "dbgap_key": NextflowParameter(
        display_name="dbGaP Repository Key",
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description="dbGaP repository key.",
    ),
    "outdir": NextflowParameter(
        display_name="Output Directory",
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({"output": True})],
        section_title=None,
        default=LatchOutputDir("latch:///fetchngs"),
        description="The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.",
    ),
    "email": NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description="Email address for completion summary.",
    ),
    "run_name": NextflowParameter(
        type=str,
        display_name="Run Name",
        description="Name of run",
        batch_table_column=True,
        rules=[
            LatchRule(
                regex=r"^[a-zA-Z0-9_-]+$",
                message="Run name must contain only letters, digits, underscores, and dashes. No spaces are allowed.",
            )
        ],
    ),
}
