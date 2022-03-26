from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  first_name = fields.Str()
  last_name = fields.Str()
  phone_number = fields.Str(required=True)
  pin_number = fields.Str(required=True)