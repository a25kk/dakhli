# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dakhli.dakhli.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dakhli.dakhli into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dakhli.dakhli is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dakhli.dakhli'))

    def test_uninstall(self):
        """Test if dakhli.dakhli is cleanly uninstalled."""
        self.installer.uninstallProducts(['dakhli.dakhli'])
        self.assertFalse(self.installer.isProductInstalled('dakhli.dakhli'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDakhlidakhliLayer is registered."""
        from dakhli.dakhli.interfaces import IDakhlidakhliLayer
        from plone.browserlayer import utils
        self.failUnless(IDakhlidakhliLayer in utils.registered_layers())
