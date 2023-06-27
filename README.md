# Demo Module

This is a custom module for Odoo 16 that adds a new object called "demo.demo" with a field "name" of type "char". It also includes separate menu, tree, and form views for the "demo.demo" object.

![Screenshot from 2023-06-27 09-57-52](https://github.com/manjustice/SmartTekSol_TT/assets/81980801/d9aa65e0-15c9-428e-bcb5-dcf677fcd729)

![Screenshot from 2023-06-27 09-58-04](https://github.com/manjustice/SmartTekSol_TT/assets/81980801/fec73d86-f8b9-4c9e-9cf3-4c4c44d4d6bb)

## Features

- Adds a new object "demo.demo" with a field "name" of type "char".
- Provides a separate menu, tree view, and form view for the "demo.demo" object.
- Allows users to manage and view records of the "demo.demo" object in Odoo.

## Installation

```
git clone https://github.com/manjustice/SmartTekSol_TT.git
python -m venv venv
venv\Scripts\activate (Windows)
. venv/bin/activate (Linux | MacOS)
cd task_3/odoo/
pip install -r requirements.txt
```

1. Install PostgreSQL as the database server for your Odoo instance. 
2. Start the PostgreSQL service.
3. Create a new superuser in PostgreSQL to be used by Odoo.

Before using this module, make sure to update the Odoo configuration file (odoo.conf) with the following variables:

- **admin_passwd**: Set this variable to your Odoo admin password.
- **db_host**: Set this variable to your database host.
- **db_port**: Set this variable to your database port.
- **db_user**: Set this variable to your database username.
- **db_password**: Set this variable to your database user password.


## Usage
```
python odoo-bin -c odoo.conf
```
Link to open odoo server: http://"Your host":8069
