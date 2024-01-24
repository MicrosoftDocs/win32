---
description: Windows Installer can install multiple packages using transaction processing.
ms.assetid: c4a0f4d8-818d-4e60-908b-adaa2a54de95
title: Multiple-Package Installations
ms.topic: article
ms.date: 05/31/2018
---

# Multiple-Package Installations

Windows Installer can install multiple packages using [*transaction processing*](t-gly.md). This capability is available beginning with Windows Installer 4.5. The installer will install all the packages belonging to a multiple-package transaction or none of the packages. If all the packages in the transaction cannot be installed successfully, or if the user cancels the installation, the Windows Installer can roll back changes and restore the computer to its original state.

A multiple-package installation package can contain a [MsiEmbeddedChainer table](msiembeddedchainer-table.md) that references a user-defined function that uses the [**MsiBeginTransaction**](/windows/desktop/api/Msi/nf-msi-msibegintransactiona), [**MsiJoinTransaction**](/windows/desktop/api/Msi/nf-msi-msijointransaction), and [**MsiEndTransaction**](/windows/desktop/api/Msi/nf-msi-msiendtransaction) functions.

The [MsiPackageCertificate Table](msipackagecertificate-table.md) lists digital signature certificates used to verify the identity of the installation packages that make a multiple-package installation. You can use this table to reduce the number of times your multiple-package installation displays a [*User Account Control*](u-gly.md) (UAC) prompt that requires a response by an administrator.

The following Windows Installer functions can make changes to the user's computer when the Windows Installer installs, repairs, updates, or removes applications. Beginning with Windows Installer 4.5, the installer can roll back changes made by these functions during the [*transaction processing*](t-gly.md) of a multiple-package installation:

<dl>

[**MsiAdvertiseProduct**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproducta)  
[**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa)  
[**MsiApplyMultiplePatches**](/windows/desktop/api/Msi/nf-msi-msiapplymultiplepatchesa)  
[**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha)  
[**MsiConfigureFeature**](/windows/desktop/api/Msi/nf-msi-msiconfigurefeaturea)  
[**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta)  
[**MsiConfigureProductEx**](/windows/desktop/api/Msi/nf-msi-msiconfigureproductexa)  
[**MsiInstallMissingComponent**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingcomponenta)  
[**MsiInstallMissingFile**](/windows/desktop/api/Msi/nf-msi-msiinstallmissingfilea)  
[**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta)  
[**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya)  
[**MsiProvideComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidecomponenta)  
[**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta)  
[**MsiProvideQualifiedComponentEx**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponentexa)  
[**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea)  
[**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta)  
[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)  
</dl>

There is an exception if the Windows Installer encounters a package belonging to a multiple-package installation that contains a [ForceReboot](forcereboot-action.md) or [ScheduleReboot](schedulereboot-action.md) action. In this case, Windows Installer does not install only that package. Other packages belonging to the multiple-package installation, that do not contain a ForceReboot or ScheduleReboot action, can be installed.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):  **[*Transaction processing*](t-gly.md) of multiple-package Windows Installer installations is not supported. These versions of the Windows Installer are unable to roll back the installation of multiple packages as a single transaction.

**Windows Server 2008 R2 with the [Remote Desktop Services](../termserv/terminal-services-portal.md) role enabled:** Not supported. A multiple package installation using the [MsiEmbeddedChainer table](msiembeddedchainer-table.md) fails if the [Remote Desktop Services](../termserv/terminal-services-portal.md) role is enabled.

 

 
