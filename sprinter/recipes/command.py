"""
Runs a command
"""

from sprinter.recipebase import RecipeBase


class CommandRecipe(RecipeBase):

    def setup(self, feature_name, config):
        super(CommandRecipe, self).setup(feature_name, config)

    def update(self, feature_name, config):
        super(CommandRecipe, self).update(feature_name, config)

    def destroy(self, feature_name, config):
        super(CommandRecipe, self).destroy(feature_name, config)
