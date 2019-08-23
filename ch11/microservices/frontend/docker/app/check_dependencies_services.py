import os
import requests
from natsort import natsorted


VERSIONS = {
    'thoughts_backend': (f'{os.environ["THOUGHTS_BACKEND_URL"]}/admin/version',
                         'v1.6'),
}


def check_version(min_version, version):
    versions = natsorted([min_version, version])
    # Return the lower is the minimum version
    return versions[0] == min_version


def main():
    for service, (url, min_version) in VERSIONS.items():
        print(f'Checking minimum version for {service}')
        resp = requests.get(url)
        if resp.status_code != 200:
            print(f'Error connecting to {url}: {resp}')
            exit(-1)

        result = resp.json()
        version = result['version']
        print(f'Minimum {min_version}, found {version}')
        if not check_version(min_version, version):
            msg = f'Version {version} is incorrect (min {min_version})'
            print(msg)
            exit(-1)


if __name__ == '__main__':
    main()
