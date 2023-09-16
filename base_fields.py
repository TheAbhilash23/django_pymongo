class MongoField:
    __label = ''
    __description = ''

    def __init__(self, *args, **kwargs):
        import ipdb
        # ipdb.set_trace()
        for kwarg in kwargs.keys():
            setattr(self, '__' + kwarg, kwargs.get(kwarg))

    @property
    def label(self):
        return self.__label

    @property
    def description(self):
        return self.__description

    def __str__(self):
        return f'{self.__label}'
