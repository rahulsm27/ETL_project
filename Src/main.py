import hydra
from omegaconf import DictConfig, OmegaConf
from config_schemas.config_schema import Config


@hydra.main(config_path = "configs", config_name ='config',version_base = None)
def main(config : DictConfig)-> None:
    #setup_config()
    print(OmegaConf.to_yaml(config))
    print(config.dvc.dvc_remote_name)


if __name__ == "__main__":
    main()