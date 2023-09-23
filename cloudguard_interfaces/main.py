from cloudguard_interfaces.providers import provider_modules
from cloudguard_interfaces.providers.gcp.config import GCPConfig

class MainInterface:
    def __init__(self, provider: str, config_path: str) -> None:
        self.provider = provider
        self.config_path = config_path
    
    def config(self):
        if self.provider == "gcp":
            gcp_config = GCPConfig(config_path=self.config_path)

        if self.provider == "aws":
            pass

        if self.provider == "azure":
            pass

    def run(
            self,
            is_all_selected: bool = False,
            export_json: str = "output.json",
            is_list_resources: bool = False,
            module: str = None 
        ):

        if self.provider == "gcp":
            pass

        if self.provider == "aws":
            pass

        if self.provider == "azure":
            pass

    def list_providers(self) -> list(str):
        providers = []
        for idx,provider in enumerate(provider_modules.keys()):
            providers.append(provider)

        return providers

        