from universal_config.config_reader import ConfigReader


def test_read():
    config_reader = ConfigReader()
    print("--------------- in test")
    print(
        "------------------{}".format(
            config_reader.get("aws-credentials", "AWS_ACCESS_KEY_ID")
        )
    )
    print("----------------- finished")
