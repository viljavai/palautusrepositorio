from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        result = toml.loads(content, _dict=dict)
        
        name = result["tool"]["poetry"]["name"]
        description = result["tool"]["poetry"]["description"]
        license = result["tool"]["poetry"]["license"]
        authors = result["tool"]["poetry"]["authors"]
        dependencies = result["tool"]["poetry"]["dependencies"]
        dev_dependencies = result["tool"]["poetry"]["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
