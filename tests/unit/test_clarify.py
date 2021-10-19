# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import print_function, absolute_import

from mock import patch, Mock, MagicMock
import pytest

from sagemaker.clarify import (
    SageMakerClarifyProcessor,
    BiasConfig,
    DataConfig,
    ModelConfig,
    ModelPredictedLabelConfig,
    SHAPConfig,
)
from sagemaker import image_uris

JOB_NAME_PREFIX = "my-prefix"
TIMESTAMP = "2021-06-17-22-29-54-685"
JOB_NAME = "{}-{}".format(JOB_NAME_PREFIX, TIMESTAMP)


def test_uri():
    uri = image_uris.retrieve("clarify", "us-west-2")
    assert "306415355426.dkr.ecr.us-west-2.amazonaws.com/sagemaker-clarify-processing:1.0" == uri

