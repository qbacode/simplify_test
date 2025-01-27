from odoo.tests import common, tagged, Form


@tagged('post_install', '-at_install')
class TestCrmFormCreation(common.TransactionCase):

    def setUp(self):
        super().setUp()

    def test_crm_form_creation(self):
        crm_lead_form = Form(self.env['crm.lead'])
        crm_lead_form.name = "Test Lead Form"
        lead = crm_lead_form.save()
        self.assertEqual(lead.name, "Test Lead Form")
