from five import grok
from plone.supermodel import model
from plone.directives import form

from zope import schema
from z3c.form import button

from Products.CMFCore.interfaces import ISiteRoot
from Products.statusmessages.interfaces import IStatusMessage

from example.dexterityforms.interfaces import MessageFactory as _
import formhandler

class IPizzaOrder(model.Schema):

    name = schema.TextLine(
            title=_(u"Your full name"),
        )

    address1 = schema.TextLine(
            title=_(u"Address line 1"),
        )

    address2 = schema.TextLine(
            title=_(u"Address line 2"),
            required=False,
        )

    postcode = schema.TextLine(
            title=_(u"Postcode"),
        )

    telephone = schema.ASCIILine(
            title=_(u"Telephone number"),
            description=_(u"We prefer a mobile number"),
        )

    orderItems = schema.Set(
            title=_(u"Your order"),
            value_type=schema.Choice(values=[_(u'Margherita'), _(u'Pepperoni'), _(u'Hawaiian')])
        )
		
class OrderForm(form.SchemaForm):
    grok.name('order-pizza')
    grok.require('zope2.View')
    grok.context(ISiteRoot)

    schema = IPizzaOrder
    ignoreContext = True

    label = _(u"Order your pizza")
    description = _(u"We will contact you to confirm your order and delivery.")

    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)

        # call the base class version - this is very important!
        super(OrderForm, self).update()

    @button.buttonAndHandler(_(u'Order'))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
			
		# give data to formhandler, to proceed data (SAP etc.)
        fh = formhandler.FormHandler()
        if fh.handleForm(data):
		    msg = _(u"Thank you for your order. We will contact you shortly")
        else:
		    msg = _(u"An error occurred")
		
        IStatusMessage(self.request).addStatusMessage(
            msg,
            "info"
        )
		# Redirect back to the front page with a status message
        # contextURL = self.context.absolute_url()
        # self.request.response.redirect(contextURL)

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)
