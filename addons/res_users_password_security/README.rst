.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================
Password  Security
==================

This module allows admin to set company-level password security requirements
and enforces them on the user.

It contains features such as

* Password expiration days
* Password length requirement
* Password minimum number of lowercase letters
* Password minimum number of uppercase letters
* Password minimum number of numbers
* Password minimum number of special characters

Configuration
=============

* Navigate to company you would like to set requirements on
* Click the ``Password Policy`` page
* Set the policies to your liking.

Password complexity requirements will be enforced upon next password change for
any user in that company.


Settings & Defaults
-------------------

These are defined at the company level:

+---------------------+---------+------------------------------------------+
| Name                | Default |  Description                             |
+=====================+=========+==========================================+
| password_expiration | 60      | Days until passwords expire              |
+---------------------+---------+------------------------------------------+
| password_length     | 12      | Minimum number of characters in password |
+---------------------+---------+------------------------------------------+
| password_lower      | True    | Require lowercase letter in password     |
+---------------------+---------+------------------------------------------+
| password_upper      | True    | Require uppercase letters in password    |
+---------------------+---------+------------------------------------------+
| password_numeric    | True    | Require number in password               |
+---------------------+---------+------------------------------------------+
| password_special    | True    | Require special character in password    |
+---------------------+---------+------------------------------------------+


Known Issues / Roadmap
======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/LasLabs/odoo-base/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us to smash it by providing detailed and welcomed feedback.


Credits
=======

Images
------

* LasLabs: `Icon <https://repo.laslabs.com/projects/TEM/repos/odoo-module_template/browse/module_name/static/description/icon.svg?raw>`_.

Contributors
------------

* James Foster <jfoster@laslabs.com>
* Dave Lasley <dlasley@laslabs.com>

Maintainer
----------

.. image:: https://laslabs.com/logo.png
   :alt: LasLabs Inc.
   :target: https://laslabs.com

This module is maintained by LasLabs Inc.
