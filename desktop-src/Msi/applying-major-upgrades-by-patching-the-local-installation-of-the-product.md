---
description: A major upgrade can be applied to an application by patching the local installation of the application from the command line or by using an executable.
ms.assetid: be651457-5c66-478b-89d5-3d7607702b8e
title: Applying Major Upgrades by Patching the Local Installation of the Product
ms.topic: article
ms.date: 05/31/2018
---

# Applying Major Upgrades by Patching the Local Installation of the Product

A major upgrade can be applied to an application by patching the local installation of the application from the command line or by using an executable.

> [!Note]  
> Providing a major upgrade as a patch package is not recommended because a major upgrade patch package cannot be sequenced with other updates and because the patch is not an [uninstallable patch](uninstallable-patches.md). The [Msimsp.exe](msimsp-exe.md) utility cannot be used to generate a patch package that applies a major upgrade. Instead, apply major upgrades as described in [Applying Major Upgrades by Installing the Product](applying-major-upgrades-by-installing-the-product.md).

 

**To apply a major upgrade patch to a local installation of the product**

1.  Launch the installation of the patch from the command line or by using an executable. To launch from the command line, use msiexec /p patch.msp. To launch from an executable, call [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha) or the [**ApplyPatch Method**](installer-applypatch.md) and provide the same command line arguments.
2.  When patching a client installation, the installer ignores the installation source and proceeds to patch the files that are already installed on the user's computer.
3.  The installer changes any patched components marked as run-from-source to run-locally. Users are unable to run these components from the source as long as the patch remains on the computer.
4.  The installer adds any transforms used to update the .msi file or adds patch-specific information to the user's profile.
5.  The installer caches the .msi file on the user's computer so that it can perform installation-on-demand, reinstall, and repair of the application. After a patch is applied to a stand alone installation, the installer references two or more source lists to external files: one for the original source and one for each patch that has been applied.

 

 



