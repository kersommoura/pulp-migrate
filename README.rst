Pulp Migrate
==========

**WARNING: Use at your own risk. No garuntee of saftey or function expressed or implied.**

Pulp Migrate is a suite of tests and tools for performing systems level
integration tests for for `Pulp`_.

Pulp Migrate is a GPL-licensed Python library.

Pulp Migrate depends on tools in Pulp Smash. Its requirements are frozen at a
certain version because these tools are not garunteed for backwards
compatiblity.

Install Pulp Migrate like this:

.. code-block:: sh

    python3 -m venv ~/migrate_env
    source ~/migrate_env/bin/activate
    git clone https://github.com/PulpQE/pulp-migrate
    cd pulp-migrate
    python setup.py install


Then, you must point pulp-smash at your pulp install by creating a settings file:

.. code-block:: sh

    pulp-smash settings create
    ... output ommitted ...
    # create repos on your pulp install
    python -m unittest pulp_migrate.populate
    # Do stuff .... then test that they are still there
    python -m unittest pulp_migrate.test-restore
    # Clean up the repos you created
    python -m unittest pulp_migrate.clean


* `Source code`_ and the issue tracker are available on GitHub.


.. _Pulp: http://www.pulpproject.org
.. _Source code: https://github.com/PulpQE/pulp-migrate/
