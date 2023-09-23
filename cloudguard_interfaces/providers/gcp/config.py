from cloudguard_interfaces.utils.json import load_json, save_json


class GCPConfig:

    def __init__(self, config_path:str):
        self.project_id = input("Enter your GCP project_id: ")
        self.credential_json = input("Enter your GCP service account json key path(absolute path): ")
        self.service_account_id = input("Enter your corresponding GCP service account id: ")
        self.set_credentials(config_path)

    @staticmethod
    def get_credentials(config_path):
        pass

    def set_credentials(self, config_path):
        credentials = load_json(filename=config_path)

        credentials["gcp"]["project_id"] = self.project_id
        credentials["gcp"]["credential_json"] = self.credential_json
        credentials["gcp"]["service_account_id"] = self.service_account_id

        save_json(filename=config_path, data=credentials)

