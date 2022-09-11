from odoo import models, fields, api


class MrpWorkcenterProductivityLossState(models.Model):
    """
    Definition of the state of the Workcenter associated to a Loss declaration.
    Because the 'Loss' term is quite reductive of a state of a Workcenter, and the Type
    category refears to OEE analisys, defining a State can be useful to identify some
    conditions like Maintenance or Sampling
    """
    _name = "mrp.workcenter.productivity.loss.state"
    _description = "Workcenter Productivity Losses States"
    _rec_name = 'loss_state'

    @api.depends('loss_state')
    def name_get(self):
        """ As 'category' field in form view is a Many2one, its value will be in
        lower case. In order to display its value capitalized 'name_get' is
        overrided.
        """
        result = []
        for rec in self:
            result.append((rec.id, rec.loss_state.title()))
        return result

    # fields
    # state name
    loss_state = fields.Selection([
            ('stopped', 'Stopped'),
            ('preparation', 'Preparation'),
            ('starting', 'Starting'),
            ('working', 'Working'),
            ('testing', 'Testing'),
            ('maintenance', 'Maintenance'),
            ],
            string='State',
            default='stopped',
            required=True)


class MrpWorkcenterProductivityLoss(models.Model):
    _inherit = "mrp.workcenter.productivity.loss"

    # new fields
    # loss state id
    loss_state_id = fields.Many2one(
        'mrp.workcenter.productivity.loss.state',
        string="State",
        )
    # loss state
    loss_state = fields.Selection(
        string='State',
        related='loss_state_id.loss_state',
        store=True,
        readonly=False,
        )
