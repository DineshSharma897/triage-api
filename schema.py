from marshmallow import Schema, fields, validates_schema, ValidationError
import re

class PredictRequestSchema(Schema):
    name = fields.Str(required=True)
    mobile = fields.Str(required=True)
    message = fields.Str(required=True)

    @validates_schema
    def validate_all(self, data, **kwargs):
        errors = {}

        if not data.get("name", "").strip():
            errors["name"] = ["Name must not be empty."]

        mobile = data.get("mobile", "").strip()
        if not re.fullmatch(r"\d{10}", mobile):
            errors["mobile"] = ["Mobile number must be 10 digits."]

        if not data.get("message", "").strip():
            errors["message"] = ["Message must not be empty."]

        if errors:
            raise ValidationError(errors)
