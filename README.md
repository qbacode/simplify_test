
We are facing the error running any unit tests on a demo database. You don't need our modules, you can reproduce it even from within your unit tests instanciating a Form view.

To reproduce the error on a demo database, download this module and run the unit test with  --test-tags /simplify_test
 
Here is the command I ran to reproduce the error. The error will be triggered from https://github.com/qbacode/simplify_test/blob/main/tests/test_crm_form_creation.py#L11:
 
/home/developer_1/Documents/odoo17/odoo/odoo-bin --log-level=test --test-enable --test-tags /simplify_test -d demo -i advanced_web_domain_widget,simplify_access_management,simplify_test -c /home/developer_1/Documents/odoo17/odoo.conf --stop-after-init