from krausening.properties import PropertyManager
import os


class ConfigReader:
    def __init__(self) -> None:
        os.environ["KRAUSENING_BASE"] = "./src/resources/configurations/base"
        os.environ["KRAUSENING_EXTENSIONS"] = "./src/resources/configurations/ci"
        self.property_manager = PropertyManager.get_instance()

    def get(self, group_id: str, property_key: str) -> str:
        print(
            "krausening setting -----------------{}".format(
                os.environ.get("KRAUSENING_BASE")
            )
        )

        property = self.property_manager.get_properties(group_id + ".properties")
        return property.getProperty(property_key, None)
