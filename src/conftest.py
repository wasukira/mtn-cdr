import pytest
import logging
from utils.utils import Utils

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def utils():
    return Utils()