# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dakhli.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dakhli.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dakhli.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dakhli.sitecontent'))

    def test_uninstall(self):
        """Test if dakhli.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['dakhli.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('dakhli.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IdakhliSitecontentLayer is registered."""
        from dakhli.sitecontent.interfaces import IdakhliSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IdakhliSitecontentLayer in utils.registered_layers())
