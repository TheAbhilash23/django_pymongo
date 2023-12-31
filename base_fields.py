import attrs
import ipdb

from base_validations import BASE_VALIDATIONS


class MongoField:
    __attri_label = ''
    __attri_description = ''

    def __init__(self, *args, **kwargs):
        import ipdb
        # ipdb.set_trace()
        for kwarg in kwargs.keys():
            if kwarg not in BASE_VALIDATIONS:
                continue
            setattr(self, '__attri_' + kwarg, kwargs.get(kwarg))

    @property
    def label(self):
        return self.__attri_label

    @property
    def description(self):
        return self.__attri_description

    def __str__(self):
        return f'{self.__attri_label}'

    def get_field_validation_data(self):
        # Used in dependency injection be careful
        validation_data = {}
        for attr in vars(self):
            if attr.startswith('__attri_'):
                validation_data[str(attr.replace('__attri_', ''))] = vars(self)[attr]
        return validation_data


class FileMongoField(MongoField):
    pass


class ArrayMongoField(MongoField):
    pass


class NestedMongoField(MongoField):
    pass


class MultiNestedMongoField(MongoField):
    pass
