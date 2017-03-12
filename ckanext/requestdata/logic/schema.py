from ckan.plugins import toolkit

from ckanext.requestdata.logic import validators


not_missing = toolkit.get_validator('not_missing')
not_empty = toolkit.get_validator('not_empty')
package_id_exists = toolkit.get_validator('package_id_exists')
email_validator = validators.email_validator


def request_create_schema():
    return {
        'sender_name': [not_empty, unicode],
        'organization': [not_empty, unicode],
        'email_address': [not_empty, email_validator],
        'message_content': [not_empty, unicode],
        'package_id': [not_empty, package_id_exists]
    }


def request_show_schema():
    return {
        'id': [not_empty, unicode],
        'package_id': [not_empty, package_id_exists]
    }
