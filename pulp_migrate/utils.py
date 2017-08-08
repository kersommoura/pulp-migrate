"""Tools shared by pulp_migrate tests."""
from urllib.parse import urljoin

from pulp_smash import api, config, utils
from pulp_smash.constants import (
    REPOSITORY_PATH,
    ORPHANS_PATH
)

# these tools share namespace so these imports
# disambiguate and allow modules to use tools for all plugins
from pulp_smash.tests.rpm.api_v2.utils import (  # noqa # pylint: disable=unused-import
    gen_distributor as gen_rpm_distributor,
    gen_repo as gen_rpm_repo,
)

from pulp_smash.tests.python.api_v2.utils import (  # noqa # pylint: disable=unused-import
    gen_repo as gen_python_repo,
)

from pulp_smash.tests.puppet.api_v2.utils import (  # noqa # pylint: disable=unused-import
    gen_repo as gen_puppet_repo,
    gen_distributor as gen_puppet_distributor,
)

from pulp_smash.tests.docker.api_v2.utils import (  # noqa # pylint: disable=unused-import
    gen_repo as gen_docker_repo,
)


def gen_docker_distributor():
    """Return a semi-random dict for use in creating a docker distributor."""
    return {
        'auto_publish': False,
        'distributor_id': utils.uuid4(),
        'distributor_type_id': 'docker_distributor_web',
        'distributor_config': {
            'http': True,
            'https': True,
        },
    }

def gen_python_distributor():
    """Return a semi-random dict for use in creating a Python distributor."""
    return {
        'distributor_id': utils.uuid4(),
        'distributor_type_id': 'python_distributor',
        'distributor_config': {
            'http': True,
            'https': True,
            'relative_url': utils.uuid4() + '/',
        }
    }

def clean_repo(repo_id):
    """Delete the repo with given id and any content left orphaned by it.

    Calls to clean_repo will only attempt to delete the repo
    if a repository with given id exists.

    This also makes a call to delete all orphaned content units.
    """
    client = api.Client(config.get_config(), api.json_handler)
    repos = client.get(REPOSITORY_PATH)
    for repo in repos:
        if urljoin(REPOSITORY_PATH, repo_id) in repo['_href']:
            client.delete(repo['_href'])
    client.delete(ORPHANS_PATH)


def download_rpm(repo_name, rpm_name):
    """Download an rpm from a published repo."""
    download_path = '/pulp/repos/{}/{}'.format(
        repo_name,
        rpm_name
    )
    return api.Client(config.get_config()).get(download_path)
