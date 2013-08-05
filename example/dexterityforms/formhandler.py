class FormHandler(object):
    """ handles request """
    formState = 0
    def handleForm(self, request):
        self.formState = 1
        
        print u"Order received:"
        print u"  Customer: ", request['name']
        print u"  Telephone:", request['telephone']
        print u"  Address:  ", request['address1']
        print u"            ", request['address2']
        print u"            ", request['postcode']
        print u"  Order:    ", ', '.join(request['orderItems'])
        print u""
        
        if self.formState == 1:
            return True
        else:
            return False
        
