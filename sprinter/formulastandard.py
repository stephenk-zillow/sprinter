"""
Formula base is an abstract base class outlining the method required
and some documentation on what they should provide.
"""
import logging
import os

from sprinter import lib
from sprinter.formulabase import FormulaBase


class FormulaStandard(FormulaBase):

    def __init__(self, environment):
        self.environment = environment
        self.directory = environment.directory
        self.config = environment.config
        self.injections = environment.injections
        self.system = environment.system
        self.logger = logging.getLogger('sprinter')

    def setup(self, feature_name, config):
        """ Setup performs the setup required, with the config
        specified """
        install_directory = self.directory.install_directory(feature_name)
        cwd = install_directory if os.path.exists(install_directory) else None
        if 'rc' in config:
            self.directory.add_to_rc(config['rc'])
        if 'command' in config:
            self.logger.info(lib.call(config['command'],
                                      bash=True,
                                      cwd=cwd))

    def update(self, feature_name, source_config, target_config):
        """ Setup performs the setup required, and works with the old
        config is destruction is required """
        install_directory = self.directory.install_directory(feature_name)
        cwd = install_directory if os.path.exists(install_directory) else None
        if 'rc' in target_config:
            self.directory.add_to_rc(target_config['rc'])
        if 'command' in target_config:
            self.logger.info(lib.call(target_config['command'],
                                      bash=True,
                                      cwd=cwd))

    def destroy(self, feature_name, config):
        """ Destroys an old feature if it is no longer required """
