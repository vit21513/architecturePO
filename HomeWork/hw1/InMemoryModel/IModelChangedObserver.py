import zope.interface


class IModelChangedObserver(zope.interface.Interface):

    def applyUpdateModel(self):
        pass