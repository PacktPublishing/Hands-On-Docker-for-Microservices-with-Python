import delorean
from freezegun import freeze_time
from thoughts_backend import token_validation

PRIVATE_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxF2uf9o4z4Wsg1sMHQeNlSNoz09CV6psTgKOuUH5jyzzqP/D
d2WSfEzFu965dh1nT2Q8Pc+g8nu8y0Fbuh4zdCDAHXJg629VYxTNQDjBXNsDeMB1
x3APGGLCkTnNnm4AVL5c2/+ZqmpX52rmqV0cVR8QJ7L2hsTsHsNPGtbx8UMLIX+h
kocneqP33vxFk5hlLpIsERFtRXPDAWhF+/7AamCRD3puUxE0P35eRt5kel3H6wXo
pwH9Jq6SS44NPu5EjuTR/Ne2oVYWfRUq1CP1iKUI0u2y+aro9HRMqtNSASPxxDbc
sadEhYqVB+7ak3X9qpTLM/dGy9vb8ZuizbwZKwIDAQABAoIBACw6UXhYhV0wZXe8
hRDwx5HkxNGUr4OhTf2QE+dkFbqKzGKvIK5+wSyf+hVjh/AzlTZLhEoDvuN+vTom
gWt9K+enDL5VKcE9dUT4xXYGkn7AkZqb9qsx8SRz8hDVrRtW+Voc+jtO6aR5iU0F
Rei1oREHCxN1+pLGPcx7/xAzg5DsPMiTqucqCe+o2tPRmYGZQNoDF6wUke5HLGr1
l1uMbNgfp2SdEJM8UfSX1RnzT7FqX97t1RFROG4BFqTXAt9NjKujH8OFP52cnPEE
quRondNp1ZkzhpNJaVF05Gt95sVibGMUIVfdPKPMoUa8hnbsRjGCfadtO+M9eTUU
pPbJGXECgYEA5efctQsDsRP6f43nKQuTwom4BbAEqF4e6GzW3og4aYeNsOO+9RPl
qnuSFyOZiIdUXNx0s1Wn5x4+GWpEYy9yd00KA0BVKezOyLUK5POZ6QLGkRrgU7QT
Hy53rXzVHxfmsDi/JdlA4PQfDaRqdVHlyw+EyF3aXhgWXhNW/3PjUkMCgYEA2qdJ
0xuAmWMXzDXhmNweVHCU0W4a3mr2h9E3XwD3xwifcdjtzLsR/RSWw82R8AmL/RjW
5Hq+oLiVTCdXlBBprcbGZ74SE/LEwgDT8FuCd0kxFujjUbrvldVZW2EUcgRuAtvG
Kql1sa4nF5JzZVo2UwGVHaH7WEdjh9kjHQEwMvkCgYEA0dqTtlmodAFlfPrdTrT3
mfI1nFNv3POUyNlYRGYZABKwfg9UpcYUtEn5Ls/a/ClzExRUHcII8cjELFS4ucR8
enNCuXcGha9XjRLcL+I/0dYrxBXBQAY2EhdLPHue2bPqaV5S9ExbkTqkAcLbPd2U
oIa40GACzDK2cAa9OY3hqJsCgYAsfyjV7l3gWTspkrmDWyBM/NA8QpTzOH9NKnWD
PvYtqgKQr53NMTC6+SqpVDdjyv2TFy/8NUKAALBZXBRFjIWFGNOdnx+csaX6+SIo
YucNEXcM+33vTwSc0Fsr7nizr1UX/dO5MN1DuHY6JNKZCJ/Pip3m9uTolTabGcQ8
jdZaOQKBgFN6TqCCvx5KBBadRuEp4Vgi9v5LnjaEuFgzPqgesDZu1Y+c3D11QiOx
JgHfsq7b9NbpsCBo5EILcUHAHnwDaudoY7r602OpJsug3aOG/P8NXIuFjrnaysnn
BUn6ko1X1zLJ6xcVELnUo11lmovLWnsnEC1YHj+4tHXLk1lerpdU
-----END RSA PRIVATE KEY-----
'''
PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxF2uf9o4z4Wsg1sMHQeN
lSNoz09CV6psTgKOuUH5jyzzqP/Dd2WSfEzFu965dh1nT2Q8Pc+g8nu8y0Fbuh4z
dCDAHXJg629VYxTNQDjBXNsDeMB1x3APGGLCkTnNnm4AVL5c2/+ZqmpX52rmqV0c
VR8QJ7L2hsTsHsNPGtbx8UMLIX+hkocneqP33vxFk5hlLpIsERFtRXPDAWhF+/7A
amCRD3puUxE0P35eRt5kel3H6wXopwH9Jq6SS44NPu5EjuTR/Ne2oVYWfRUq1CP1
iKUI0u2y+aro9HRMqtNSASPxxDbcsadEhYqVB+7ak3X9qpTLM/dGy9vb8ZuizbwZ
KwIDAQAB
-----END PUBLIC KEY-----
'''

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
