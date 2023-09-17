# Mention the app name followed by a '.' the model name.
# The logic is that it will iterate over the tuple and look for the app name and then the model class name in the models.py file.

import importlib
import json
import ipdb
from base_models import BaseModelCollection


MIGRATE_DEEZ = ('configurable_kyc.KYC',  # Yeah I am primeagenean...
                )


class MigrationHandler:
    # PLease do not remove the Todos, just add "#Done" when they're done.
    # TODO: Phase 1 is to only create a simple json schema for models that are listed in the MIGRATE_DEEZ tuple.
    # TODO: Phase 2 Figure out a way to handle migrations through SQLite3 database.
    #       This we can specify which schema should be strictly followed and which not.
    # TODO: Phase 3 to handle migration for nested fields.

    migration_set = MIGRATE_DEEZ

    def get_mongo_modules_models(self):
        mod = []
        for compound in self.migration_set:
            application, model = compound.split('.')
            try:
                mod.append((importlib.import_module(application+'.models'), model))
            except ImportError:
                print("Could not import")
                continue
        return mod

    def build_json_schema(self, model_dependency_injection: BaseModelCollection):
        json_schema = {'$jsonSchema': {}}
        json_schema = model_dependency_injection.extend_json_shema_validation(json_schema)
        return json.dumps(json_schema)

    def create_update_collection_validation(self, enforce_schema=True):
        mod = self.get_mongo_modules_models()
        for module, model in mod:
            print(getattr(module, model))
            validation = self.build_json_schema(getattr(module, model))
        ipdb.set_trace()

        return
