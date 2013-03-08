"""
Installs a package from whatever the native package manager is
(apt-get for debian-based, brew for OS X)
[env]
recipe = sprinter.recipes.package
debian = git
brew = git
"""

from sprinter.recipestandard import RecipeStandard
from sprinter import lib


class PackageRecipe(RecipeStandard):

    def __init__(self, environment):
        super(PackageRecipe, self).__init__(environment)
        self.package_manager = self.__get_package_manager()

    def setup(self, feature_name, config):
        if self.package_manager in config:
            package = config[self.package_manager]
            self.logger.info("Installing %s..." % package)
            lib.call("sudo %s install %s" % (self.package_manager, package))

    def __get_package_manager(self):
        if self.environment.isOSX():
            return "brew"
        elif self.environment.isDebianBased():
            return "apt-get"
        elif self.environment.isFedoraBased():
            return "yum"