from brightway_projects.peewee import JSONField
from peewee import TextField, Model, fn


class UncertaintyType(Model):
    label = TextField()

    def __str__(self):
        return "Uncertainty Type {}".format(self.label)

    def __repr__(self):
        return "Uncertainty Type {}:{}".format(self.id, self.label)


class DataModel(Model):
    """Class that stores extra attributes and values in ``.data``."""
    data = JSONField(default={})

    def __getitem__(self, key):
        if key in self._meta.sorted_field_names:
            return getattr(self, key)
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        if key in self._meta.sorted_field_names:
            setattr(self, key, value)
        else:
            self.data[key] = value

    @classmethod
    def span(cls):
        return (cls.select(fn.MIN(cls.id)).scalar(), cls.select(fn.MAX(cls.id)).scalar())
