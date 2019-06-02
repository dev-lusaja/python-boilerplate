from core.schemas.health import HealthSchema, HealthSchemaException


class HealthService:

    __schema = HealthSchema()

    def get_status(self):
        schema = self.__schema.load({'status': 'Ok!'})
        if schema.errors:
            raise HealthSchemaException(schema.errors)
        return schema.data
