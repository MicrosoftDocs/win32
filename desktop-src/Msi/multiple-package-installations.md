---
Description: Windows Installer can install multiple packages using transaction processing.
ms.assetid: c4a0f4d8-818d-4e60-908b-adaa2a54de95
title: Multiple-Package Installations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multiple-Package Installations

Windows Installer can install multiple packages using [*transaction processing*](t-gly.md#-msi-transaction-processing-gly). This capability is available beginning with Windows Installer 4.5. The installer will install all the packages belonging to a multiple-package transaction or none of the packages. If all the packages in the transaction cannot be installed successfully, or if the user cancels the installation, the Windows Installer can roll back changes and restore the computer to its original state.

A multiple-package installation package can contain a [MsiEmbeddedChainer table](msiembeddedchainer-table.md) that references a user-defined function that uses the [**MsiBeginTransaction**](/windows/win32/Msi/nf-msi-msibegintransactiona?branch=master), [**MsiJoinTransaction**](/windows/win32/Msi/nf-msi-msijointransaction?branch=master), and [**MsiEndTransaction**](/windows/win32/Msi/nf-msi-msiendtransaction?branch=master) functions.

The [MsiPackageCertificate Table](msipackagecertificate-table.md) lists digital signature certificates used to verify the identity of the installation packages that make a multiple-package installation. You can use this table to reduce the number of times your multiple-package installation displays a [*User Account Control*](u-gly.md#-msi-user-account-control-gly) (UAC) prompt that requires a response by an administrator.

The following Windows Installer functions can make changes to the user's computer when the Windows Installer installs, repairs, updates, or removes applications. Beginning with Windows Installer 4.5, the installer can roll back changes made by these functions during the [*transaction processing*](t-gly.md#-msi-transaction-processing-gly) of a multiple-package installation:

<dl>

[**MsiAdvertiseProduct**](/windows/win32/Msi/nf-msi-msiadvertiseproducta?branch=master)  
[**MsiAdvertiseProductEx**](/windows/win32/Msi/nf-msi-msiadvertiseproductexa?branch=master)  
[**MsiApplyMultiplePatches**](/windows/win32/Msi/nf-msi-msiapplymultiplepatchesa?branch=master)  
[**MsiApplyPatch**](/windows/win32/Msi/nf-msi-msiapplypatcha?branch=master)  
[**MsiConfigureFeature**](/windows/win32/Msi/nf-msi-msiconfigurefeaturea?branch=master)  
[**MsiConfigureProduct**](/windows/win32/Msi/nf-msi-msiconfigureproducta?branch=master)  
[**MsiConfigureProductEx**](/windows/win32/Msi/nf-msi-msiconfigureproductexa?branch=master)  
[**MsiInstallMissingComponent**](/windows/win32/Msi/nf-msi-msiinstallmissingcomponenta?branch=master)  
[**MsiInstallMissingFile**](/windows/win32/Msi/nf-msi-msiinstallmissingfilea?branch=master)  
[**MsiInstallProduct**](/windows/win32/Msi/nf-msi-msiinstallproducta?branch=master)  
[**MsiProvideAssembly**](/windows/win32/Msi/nf-msi-msiprovideassemblya?branch=master)  
[**MsiProvideComponent**](/windows/win32/Msi/nf-msi-msiprovidecomponenta?branch=master)  
[**MsiProvideQualifiedComponent**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponenta?branch=master)  
[**MsiProvideQualifiedComponentEx**](/windows/win32/Msi/nf-msi-msiprovidequalifiedcomponentexa?branch=master)  
[**MsiReinstallFeature**](/windows/win32/Msi/nf-msi-msireinstallfeaturea?branch=master)  
[**MsiReinstallProduct**](/windows/win32/Msi/nf-msi-msireinstallproducta?branch=master)  
[**MsiRemovePatches**](/windows/win32/Msi/nf-msi-msiremovepatchesa?branch=master)  
</dl>

There is an exception if the Windows Installer encounters a package belonging to a multiple-package installation that contains a [ForceReboot](forcereboot-action.md) or [ScheduleReboot](schedulereboot-action.md) action. In this case, Windows Installer does not install only that package. Other packages belonging to the multiple-package installation, that do not contain a ForceReboot or ScheduleReboot action, can be installed.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):  **[*Transaction processing*](t-gly.md#-msi-transaction-processing-gly) of multiple-package Windows Installer installations is not supported. These versions of the Windows Installer are unable to roll back the installation of multiple packages as a single transaction.

**Windows Server 2008 R2 with the [Remote Desktop Services](termserv.terminal_services_portal) role enabled:** Not supported. A multiple package installation using the [MsiEmbeddedChainer table](msiembeddedchainer-table.md) fails if the [Remote Desktop Services](termserv.terminal_services_portal) role is enabled.

 

 



