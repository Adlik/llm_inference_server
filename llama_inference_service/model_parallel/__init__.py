# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.
#
# This source code is licensed under the BSD license found in the
# LICENSE file in the root directory of this source tree.

import importlib.util

def is_torch_gcu_available():
    if importlib.util.find_spec("torch_gcu") is None:
        return False
    if importlib.util.find_spec("torch_gcu.core") is None:
        return False
    return importlib.util.find_spec("torch_gcu.core.model") is not None
from typing import List

from .cross_entropy import vocab_parallel_cross_entropy
# from .utils import ensure_divisibility
from .initialize import (
    destroy_model_parallel,
    get_data_parallel_group,
    get_data_parallel_rank,
    get_data_parallel_world_size,
    get_model_parallel_group,
    get_model_parallel_rank,
    get_model_parallel_src_rank,
    get_model_parallel_world_size,
    get_pipeline_parallel_group,
    get_pipeline_parallel_ranks,
    initialize_model_parallel,
)
from .layers import ColumnParallelLinear, RowParallelLinear, VocabParallelEmbedding
from .mappings import copy_to_model_parallel_region, gather_from_model_parallel_region
from .random import get_cuda_rng_tracker, model_parallel_cuda_manual_seed

__all__: List[str] = []
