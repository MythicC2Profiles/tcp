from mythic_container.C2ProfileBase import *
from pathlib import Path
import os


class TCP(C2Profile):
    name = "tcp"
    description = "Communication over TCP sockets with a specific packet structure.\nCheck out the docs for more information."
    author = "@djhohnstein, @its_a_feature_"
    is_p2p = True
    is_server_routed = True
    server_binary_path = Path(os.path.join(".", "c2_code"))
    server_folder_path = Path(os.path.join(".",  "c2_code"))
    parameters = [
        C2ProfileParameter(
            name="port",
            description="Port for the agent to bind to",
            format_string="[0-65535]{1}",
            randomize=True,
            required=False,
        ),
        C2ProfileParameter(
            name="killdate",
            description="Kill Date",
            parameter_type=ParameterType.Date,
            default_value=365,
            required=False,
        ),
        C2ProfileParameter(
            name="encrypted_exchange_check",
            description="Perform Key Exchange",
            default_value=True,
            required=False,
            parameter_type=ParameterType.Boolean,
        ),
        C2ProfileParameter(
            name="AESPSK",
            description="Crypto type",
            default_value="aes256_hmac",
            parameter_type=ParameterType.ChooseOne,
            choices=["aes256_hmac", "none"],
            required=False,
            crypto_type=True
        ),
    ]
