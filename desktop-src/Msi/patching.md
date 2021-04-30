---
description: These sections describe patching a Windows Installer installation.
ms.assetid: 'e3c233bc-4344-449e-9e79-1a3b96ad2d08'
title: Patching
ms.topic: article
ms.date: 05/31/2018
---

# Patching

An application that has been installed using the Microsoft Windows Installer can be upgraded by reinstalling an updated installation package (.msi file), or by applying a Windows Installer patch (an .msp file) to the application.

A Windows Installer patch (.msp file) is a self-contained package that contains the updates to the application and describes which versions of the application can receive the patch. Patches contain at a minimum, two database transforms and can contain patch files that are stored in the cabinet file stream of the patch package. For more information about the parts of a Windows Installer patch package, see [Patch Packages](patch-packages.md).

Servicing applications by delivering a Windows Installer patch, rather than a complete installation package for the updated product can have advantages. A patch can contain an entire file or only the file bits necessary to update part of the file. This can enable the user to download an upgrade patch that is much smaller than the installation package for the entire product. An update using a patch can preserve a user customization of the application through the upgrade.

**Windows Installer 4.5 and later:  **

Beginning with Windows Installer 4.5, developers can mark components in a patch with the **msidbComponentAttributesUninstallOnSupersedence** value in the [Component table](component-table.md). If a subsequent patch is installed, marked with the **msidbPatchSequenceSupersedeEarlier** value in its [MsiPatchSequence table](msipatchsequence-table.md) to supersede the first patch, Windows Installer 4.5 and later can unregister and uninstall components marked **msidbComponentAttributesUninstallOnSupersedence** to prevent leaving behind unused components on the computer. If the component is not marked with with this bit, installation of the superseding patch can leave an unused component on the computer. Setting the **MSIUNINSTALLSUPERSEDEDCOMPONENTS** property has the same effect as setting this bit for all components.

**Windows Installer 3.0 and later:  **

Developers who use Windows Installer 3.0, and author patch packages that have the [MsiPatchSequence table](msipatchsequence-table.md) can create patch packages that do the following:

-   Use the product baseline cached by the installer to more easily service applications with smaller delta patches. For more information about using the product baseline, see [Reducing Patch Size](reducing-patch-size.md).
-   Skip actions associated with specific tables that are unmodified by the patch. This can significantly reduce the time required to install the patch. For more information about which tables can be skipped, see [Patch Optimization](patch-optimization.md).
-   Create and install patches that can be uninstalled singly, and in any order, without having to uninstall and reinstall the entire application and other patches. For more information about uninstalling patches, see [Removing Patches](removing-patches.md).
-   Apply patches in a constant order regardless of the order that the patches are provided to the system. For more information about how the Windows Installer determines the sequence used to apply patches, see [Sequencing Patches](sequencing-patches.md).
-   Apply patches to an application that has been installed in a per-user-managed context. For more information, see [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).

**Windows Installer 2.0:  **

The [MsiPatchSequence table](msipatchsequence-table.md) is not supported. Beginning with Windows Installer 3.0, patch packages can contain information that describes the patching sequence for the patch relative to other updates and additional descriptive information.

The recommended method for creating a patch package is to use patch creation tools such as [Msimsp.exe](msimsp-exe.md) and [Patchwiz.dll](patchwiz-dll.md). Developers can generate a patch creation file as described in the section: [Creating a Patch Package](creating-a-patch-package.md). The creation of a small update patch is described in the section: [A Small Update Patching Example](a-small-update-patching-example.md).

Microsoft Windows Installer accepts a Uniform Resource Locator (URL) as a valid source for a patch. For more information about how to install a patch located on a Web server, see [Downloading and Installing a Patch From the Internet](downloading-and-installing-a-patch-from-the-internet.md).

A single Windows Installer patch (.msp file) can be applied to the installation package when installing an application for the first time. For more information, see [Patching Initial Installations](patching-initial-installations.md).

It is not possible to eliminate all circumstances when the application of a patch may require access to the original installation source. However, to minimize the possibility that your patch will require access to the original source, adhere to the points listed in the following section: [Preventing a Patch from Requiring Access to the Original Installation Source](preventing-a-patch-from-requiring-access-to-the-original-installation-source.md).

To minimize the possibility that your patch is not broken by a subsequent customization transform, typically the patch is installed first, followed by the customization. Installing customization transforms first, and then the patch, may break the customization. For more information about patching customized applications, see [Patching Customized Applications](patching-customized-applications.md).

 

 



