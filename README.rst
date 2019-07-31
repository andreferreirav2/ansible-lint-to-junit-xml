=============================
Ansible Lint to jUnit XML
=============================

.. image:: https://badge.fury.io/py/ansible-lint-to-junit-xml.png
    :target: http://badge.fury.io/py/ansible-lint-to-junit-xml

.. image:: https://travis-ci.org/andreferreirav2/ansible-lint-to-junit-xml.png?branch=master
    :target: https://travis-ci.org/andreferreirav2/ansible-lint-to-junit-xml

Convert ansible-lint outputs to a jUnit valid xml tests result file.

Quickstart
----------

Install ``ansible-lint-to-junit-xml`` in your preferred Python env

.. code-block:: bash

    pip install ansible-lint-to-junit-xml

Run ``ansible-lint`` on the desired files and pipe to ``ansible-lint-to-junit-xml``

.. code-block:: bash

    ansible-lint -q -p <file or directly> | ansible-lint-to-junit-xml > results/ansible-lint-results.xml

Alternatively you can run ``ansible-lint`` separately from ``ansible-lint-to-junit-xml`` and use a file to pass the output

.. code-block:: bash

    ansible-lint -q -p <file or directly> > ansible-lint-results.txt
    ansible-lint-to-junit-xml ansible-lint-results.txt > results/ansible-lint-results.xml


**Note:** ``ansible-lint`` must run with ``-p`` for the output to be machine parsable

Features
--------

* Pipe output directly from ``ansible-lint`` call
* Output XML file is compliant with `jenkins junit5 Schema <https://github.com/junit-team/junit5/blob/master/platform-tests/src/test/resources/jenkins-junit.xsd/>`_.
* Built using `Nekroze/cookiecutter-pypackage <https://github.com/Nekroze/cookiecutter-pypackage/>`_
* This project appeared as an alternative to `wasilak's ansible-lint-junit <https://github.com/wasilak/ansible-lint-junit/>`_.

Example
-------------

Running ``ansible-lint`` on a file results in:
::  

    playbooks/test_playbook.yml:41: [E303] curl used in place of get_url or uri module
    playbooks/tasks/example_task.yml:28: [E601] Don't compare to literal True/False

Running ``ansible-lint`` and piping the output to ``ansible-lint-to-junit-xml`` looks line this:

.. code-block:: bash

    ansible-lint -q -p playbooks/test_playbook.yml | ansible-lint-to-junit-xml

Would result in:

.. code-block:: xml

    <?xml version="1.0" ?>
    <testsuites>
        <testsuite errors="2" name="ansible-lint" tests="2">
            <testcase name="[E303] curl used in place of get_url or uri module">
                <failure message="playbooks/test_playbook.yml:41: [E303] curl used in place of get_url or uri module" type="ansible-lint">
                ansible-lint error: [E303] curl used in place of get_url or uri module
                ansible-lint error description: [E303] curl used in place of get_url or uri module
                filename: playbooks/test_playbook.yml
                line nr: 41
                </failure>
            </testcase>
            <testcase name="[E601] Don't compare to literal True/False">
                <failure message="playbooks/tasks/example_task.yml:28: [E601] Don't compare to literal True/False" type="ansible-lint">
                ansible-lint error: [E601] Don't compare to literal True/False
                ansible-lint error description: [E601] Don't compare to literal True/False
                filename: playbooks/tasks/example_task.yml
                line nr: 28
                </failure>
            </testcase>
        </testsuite>
    </testsuites>
