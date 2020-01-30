import json
import botocore

from av_agent_utils import okta_login


def check_sts_token_by_config(config_file):
    try:
        with open(config_file) as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(config_file, encoding='utf-16') as f:
            content = f.read()

    data = json.loads(content)

    opt = data['options']
    return check_sts_token_by_key(
        aws_access_key_id=opt['aws_access_key_id'],
        aws_secret_access_key=opt['aws_secret_access_key'],
        aws_session_token=opt['aws_session_token']
    )


def check_sts_token_by_key(aws_access_key_id, aws_secret_access_key, aws_session_token):
    session = okta_login()
    this_client = session.client(
        'sts',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
    )

    try:
        identity = this_client.get_caller_identity()
        return {
            'response': identity,
            'status': 'success',
        }

    except botocore.exceptions.ClientError as e:
        return {
            'status': 'error',
            'detail': str(e),
            'response': None,
        }
