# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from museudigital.tema.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of museudigital.tema into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if museudigital.tema is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('museudigital.tema'))

    def test_uninstall(self):
        """Test if museudigital.tema is cleanly uninstalled."""
        self.installer.uninstallProducts(['museudigital.tema'])
        self.assertFalse(self.installer.isProductInstalled('museudigital.tema'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IMuseudigitalTemaLayer is registered."""
        from museudigital.tema.interfaces import IMuseudigitalTemaLayer
        from plone.browserlayer import utils
        self.failUnless(IMuseudigitalTemaLayer in utils.registered_layers())
