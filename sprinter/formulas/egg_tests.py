from mock import Mock
from sprinter.testtools import FormulaTest

source_config = """
"""

target_config = """
[simple_example]
formula = sprinter.formulas.egg
egg = jedi

[simple_multiple_eggs]
formula = sprinter.formulas.egg
eggs = jedi, epc=0.5
       pelican

[simple_multiple_and_single_eggs]
formula = sprinter.formulas.egg
egg = sprinter
eggs = jedi, epc=0.5
       pelican
"""


class TestEggFormula(FormulaTest):
    """ Tests for the unpack formula """

    def setup(self):
        super(TestEggFormula, self).setup(source_config=source_config,
                                             target_config=target_config)

    def test_simple_example(self):
        """ The egg formula should install a single egg """
        self.environment.install_feature("simple_example")
        self.lib.call.assert_has_call("pip install jedi")

    def test_simple_multiple_eggs(self):
        """ The egg formula should install multiple eggs """
        self.environment.install_feature("simple_multiple_eggs")
        self.lib.call.assert_has_call("pip install jedi")
        self.lib.call.assert_has_call("pip install epc=0.5")
        self.lib.call.assert_has_call("pip install pelican")

    def test_simple_multiple_and_single_eggs(self):
        """ The egg formula should install single and multiple eggs """
        self.environment.install_feature("simple_multiple_eggs")
        self.lib.call.assert_has_call("pip install jedi")
        self.lib.call.assert_has_call("pip install epc=0.5")
        self.lib.call.assert_has_call("pip install pelican")
        self.lib.call.assert_has_call("pip install sprinter")