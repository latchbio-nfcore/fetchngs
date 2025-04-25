from pathlib import Path

from latch.types.directory import LatchDir
from latch.types.metadata import (
    Fork,
    ForkBranch,
    LatchAuthor,
    LatchRule,
    NextflowMetadata,
    NextflowParameter,
    NextflowRuntimeResources,
    Params,
    Section,
    Spoiler,
    Text,
)

from .parameters import generated_parameters

flow = [
    # Input Options Section
    Section(
        "Input Options",
        Params("input"),
    ),
    Section(
        "Download Options",
        Params(
            "download_method",
            "skip_fastq_download",
            "dbgap_key",
        ),
    ),
    Section(
        "Output Directory",
        Params("run_name"),
        Text("Parent directory for outputs"),
        Params("outdir"),
    ),
    Section(
        "Additional Options",
        Spoiler(
            "Metadata Options",
            Params(
                "ena_metadata_fields",
                "sample_mapping_fields",
            ),
        ),
        Spoiler(
            "Pipeline Options",
            Params("nf_core_rnaseq_strandedness", "nf_core_pipeline"),
        ),
    ),
]

NextflowMetadata(
    display_name="nf-core/fetchngs",
    author=LatchAuthor(
        name="nf-core",
    ),
    about_page_path=Path("docs/about.md"),
    parameters=generated_parameters,
    runtime_resources=NextflowRuntimeResources(
        cpus=4,
        memory=8,
        storage_gib=100,
    ),
    log_dir=LatchDir("latch:///your_log_dir"),
    flow=flow,
)
