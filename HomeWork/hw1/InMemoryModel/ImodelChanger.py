import zope.interface


class IModelChanger(zope.interface.Interface):

    def notifyChange(self, sender):
        pass
