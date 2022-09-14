---
description: The following sections present an example of authoring an upgrade package for the application described in An Installation Example.
ms.assetid: 233302ea-abc3-4879-b868-425f2b10e02e
title: An Upgrade Example
ms.topic: article
ms.date: 05/31/2018
---

# An Upgrade Example

The following sections present an example of authoring an upgrade package for the application described in [An Installation Example](an-installation-example.md). An example of a minimal user interface for this sample is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) as the file Uisample.msi. If you have the SDK, you have access to all the tools and data necessary to reproduce the sample installation package, user interface, and sample upgrade package.

This example illustrates how to create a Windows Installer package that upgrades the hypothetical product MNP2000 to a new product called MNP2001. The example upgrade package applies a major upgrade to the product which requires changing the product code. For more information about major upgrades, see the topic on [Major Upgrades](major-upgrades.md) in the [Patching and Upgrades](patching-and-upgrades.md) section.

The sample upgrade package has the following specifications:

-   To qualify to receive this upgrade to MNP2001, a user must have previously installed the 1.0 to 1.4 (inclusive) versions of English language MNP2000 using Windows Installer.
-   When a user attempts to install the upgrade package, the upgrade functionality of Windows Installer searches the user's computer for any products that qualify for the upgrade.
-   Windows Installer migrates all the of the original product's feature settings to the upgraded product.
-   The installer removes all obsolete features from the user's computer.
-   The installer installs all new features belonging to the upgrade.
-   An uninstall of the upgrade package removes the product from the user's computer, and does not restore the earlier version of the product.
-   The sample upgrade updates shortcuts to new files and features.

    [Planning a Major Upgrade](planning-a-major-upgrade.md)

    [Importing Original Installation Database](importing-original-installation-database.md)

    [Updating Directory Structure for an Upgrade](updating-directory-structure-for-an-upgrade.md)

    [Updating Files and File Attributes for an Upgrade](updating-files-and-file-attributes-for-an-upgrade.md)

    [Updating Components for an Upgrade](updating-components-for-an-upgrade.md)

    [Updating Features for an Upgrade](updating-features-for-an-upgrade.md)

    [Updating Shortcuts for an Upgrade](updating-shortcuts-for-an-upgrade.md)

    [Updating Upgrade Table for an Upgrade](updating-upgrade-table-for-an-upgrade.md)

    [Updating Properties for an Upgrade](updating-properties-for-an-upgrade.md)

    [Updating Sequence Tables for an Upgrade](updating-sequence-tables-for-an-upgrade.md)

    [Updating Summary Information for an Upgrade](updating-summary-information-for-an-upgrade.md)

    [Validating an Installation Upgrade](validating-an-installation-upgrade.md)

 

 



