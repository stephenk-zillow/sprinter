"""
Recipe base is an abstract base class outlining the method required
and some documentation on what they should provide.
"""


class RecipeBase(object):

    def __init__(self, environment):
        self.environment = environment

    def setup(self, feature_name, config):
        """ Setup performs the setup required, with the config
        specified """
        pass

    def update(self, feature_name, config):
        """ Setup performs the setup required, and works with the old
        config is destruction is required """
        pass

    def destroy(self, feature_name, old_config):
        """ Destroys an old feature if it is no longer required """
        pass

    def activate(self, feature_name, config):
        """ function to run when activating """
        pass

    def deactivate(self, feature_name, config):
        """ tasks to run when deactivating """
        pass

    def reload(self, feature_name, config):
        """ tasks to call when reloading """
        pass