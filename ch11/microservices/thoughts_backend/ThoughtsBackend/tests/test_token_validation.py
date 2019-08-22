import delorean
from freezegun import freeze_time
from thoughts_backend import token_validation
from .constants import PRIVATE_KEY, PUBLIC_KEY


INVALID_PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsyJ9HXVEYdf5axky6jMr
asfhBM0OnlQqPQAuFm06LwQP4pci9OrEffgOivBiGcblJIgskTE8X0ShVikHAQKK
GWjmyjJuQ1QFVk5050zxDNh12WvIl0NG1PSjlhw9gVP7lJgxgLdfXARTQTgw2TF9
kjHfik1zFQwZLaYzSSbtL1OB+VpCzu02ZGW0RiTDu83IfoVjEEBkmJMyOpU7Mm6V
jzoLevtSLLPzFsTroMCI5KhxSyrfCD6bOsW/6hiU45i1yLucrqSKDi32FAfFU+Hr
jiNC+MHB7Qn4+X5FEKRqykOjiB4PzLrmNR1UEUnJT+PBUAaYUX9in+p2lVRJ/6qs
+wIDAQAB
-----END PUBLIC KEY-----
'''


def test_encode_and_decode():
    payload = {
        'example': 'payload',
    }

    token = token_validation.encode_token(payload, PRIVATE_KEY)
    assert payload == token_validation.decode_token(token, PUBLIC_KEY)


def test_invalid_token_header_invalid_format():
    header = 'bad header'
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


def test_invalid_token_header_bad_token():
    header = 'Bearer baddata'
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


def test_invalid_token_no_header():
    header = None
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


def test_invalid_token_header_not_expiry_time():
    payload = {
        'username': 'tonystark',
    }
    token = token_validation.encode_token(payload, PRIVATE_KEY)
    token = token.decode('utf8')
    header = f'Bearer {token}'
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


@freeze_time('2018-05-17 13:47:34')
def test_invalid_token_header_expired():
    expiry = delorean.parse('2018-05-17 13:47:33').datetime
    payload = {
        'username': 'tonystark',
        'exp': expiry,
    }
    token = token_validation.encode_token(payload, PRIVATE_KEY)
    token = token.decode('utf8')
    header = f'Bearer {token}'
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


@freeze_time('2018-05-17 13:47:34')
def test_invalid_token_header_no_username():
    expiry = delorean.parse('2018-05-17 13:47:34').datetime
    payload = {
        'exp': expiry,
    }
    token = token_validation.encode_token(payload, PRIVATE_KEY)
    token = token.decode('utf8')
    header = f'Bearer {token}'
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert None is result


def test_valid_token_header_invalid_key():
    header = token_validation.generate_token_header('tonystark', PRIVATE_KEY)
    result = token_validation.validate_token_header(header, INVALID_PUBLIC_KEY)
    assert None is result


def test_valid_token_header():
    header = token_validation.generate_token_header('tonystark', PRIVATE_KEY)
    result = token_validation.validate_token_header(header, PUBLIC_KEY)
    assert 'tonystark' == result
