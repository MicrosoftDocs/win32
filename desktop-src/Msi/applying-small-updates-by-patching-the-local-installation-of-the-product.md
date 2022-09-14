---
description: A small update can be applied to an application by patching the local installation of the application.
ms.assetid: 2a04ffd0-d5b6-44f3-bef2-73f59179aed1
title: Applying Small Updates by Patching the Local Installation of the Product
ms.topic: article
ms.date: 05/31/2018
---

# Applying Small Updates by Patching the Local Installation of the Product

A small update can be applied to an application by patching the local installation of the application.

**To apply a small update patch to a local installation of the product**

1.  Launch the installation of the patch from the command line or by using an executable. To launch from the command line, use **msiexec /p patch.msp REINSTALL=\[***Feature list***\] REINSTALLMODE=omus**. To launch from an executable, call [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha) or the [**ApplyPatch Method**](installer-applypatch.md) and provide the same command line arguments.
2.  When patching a client installation, the installer ignores the installation source and proceeds to patch the files that are already installed on the user's computer.
3.  The installer changes any patched components marked as run-from-source to run-locally. Users are unable to run these components from the source as long as the patch remains on the computer.
4.  The installer adds any transforms used to update the .msi file or adds patch-specific information to the user's profile.
5.  The installer caches the .msi file on the user's computer so that it can perform installation-on-demand, reinstall, and repair of the application. After a patch is applied to a standalone installation, the installer references two or more source lists to external files: one for the original source and one for each patch that has been applied.

 

 



