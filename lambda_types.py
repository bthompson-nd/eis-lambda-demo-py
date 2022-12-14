""" Note: this code is used only by the static type checker! """
from typing import Dict, Any

LambdaDict = Dict[str, Any]


class LambdaCognitoIdentity(object):
    """Lambda object"""

    cognito_identity_id: str
    cognito_identity_pool_id: str


class LambdaClientContextMobileClient(object):
    """Lambda object"""

    installation_id: str
    app_title: str
    app_version_name: str
    app_version_code: str
    app_package_name: str


class LambdaClientContext(object):
    """Lambda object"""

    client: LambdaClientContextMobileClient
    custom: LambdaDict
    env: LambdaDict


class LambdaContext(object):
    """Lambda object"""

    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    identity: LambdaCognitoIdentity
    client_context: LambdaClientContext

    @staticmethod
    def get_remaining_time_in_millis() -> int:
        """Lambda object"""
        return 0
