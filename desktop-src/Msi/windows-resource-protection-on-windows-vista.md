---
description: Windows Installer adheres to Windows Resource Protection (WRP) when installing essential system files, folders, and registry information in Windows Server 2008 and later and Windows Vista and later.
ms.assetid: 38865ee1-22ef-430b-99ce-1c6983c3b51f
title: Using Windows Installer and Windows Resource Protection
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Installer and Windows Resource Protection

Windows Installer adheres to Windows Resource Protection (WRP) when installing essential system files, folders, and registry information in Windows Server 2008 and later and Windows Vista and later.

WRP in Windows Server 2008 and Windows Vista replaces Windows File Protection (WFP) in Windows Server 2003, Windows XP, and Windows 2000. Windows Installer developers should note the following changes in how the installer handles protected resources in Windows Server 2008 and later and Windows Vista and later:

-   When running on Windows Server 2008 and later or Windows Vista and later, the Windows Installer skips the installation of any file that is protected by WRP, the installer enters a warning in the log file, and continues with the remainder of the installation without an error. In Windows Server 2003, Windows XP, and Windows 2000, when the Windows Installer encountered a WFP-protected file, the installer would request that WFP install the file.
-   WRP on Windows Server 2008 and later or Windows Vista and later can protect registry keys in addition to files. If the Windows Installer encounters a WRP-protected registry key, the installer skips the installation of that registry key, the installer enters a warning in the log file, and continues with the remainder of the installation without an error.
-   Note that if a Windows Installer component contains a file or registry key that is protected by WRP, this resource must be used as the KeyPath for the component. In this case, Windows Installer does not install, update, or remove the component. You should not include any protected resources in an installation package. Instead, you should use the [supported resource replacement mechanisms](../wfp/supported-file-replacement-mechanisms.md) for [Windows Resource Protection](../wfp/windows-resource-protection-portal.md).

For more information about WRP, see [Windows Resource Protection](../wfp/windows-resource-protection-portal.md) and information that is provided on [Microsoft Technet](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc709691(v=ws.10)).

## WFP for Windows Server 2003 and Windows XP/2000

Windows Installer adheres to Windows File Protection (WFP) when installing essential system files on Windows Server 2003, Windows XP and Windows 2000. If a protected system file is modified by an unattended installation of an application, WFP restores the file to the verified file version.

Windows Installer never attempts to install or replace a protected file. When the [InstallFiles](installfiles-action.md) action or any other action scheduled before InstallFiles attempts to install a file protected on Windows Server 2003, Windows XP or Windows 2000, the installer calls WFP with a request to install or replace the protected file. The installer requests the file installation from WFP immediately after executing the InstallFiles action. WFP installs or replaces the file on the user's system with a cached version of the protected file. Note that this does not guarantee that the version of the file installed from the cache is the version required by the application. After WFP has installed the file, the installer determines whether this version matches the version in the package. If the file version in the package is greater than the installed version, the installer informs the user that it cannot update the system and that an update of the operating system may be required for the application.

If any action sequenced after [InstallFiles](installfiles-action.md) attempts to install or replace a protected file not already installed on the system, the installer cannot call WFP to install the file. In this case, the installer informs the user that it cannot update the system and that an update of the operating system may be required for the application.

The installer also checks with WFP when removing files and never attempts to remove protected system files.

## Component Key Files Protected by WFP

Note that if a Windows Installer component contains a WFP file, this file must be specified as the key path for the component.

When the installer attempts to install a component's key file on Windows Server 2003, Windows XP or Windows 2000, it first calls WFP to determine if the key file is protected. When the key file of a component is protected by WFP, and that key file is already installed, the installer updates the component only if the version of the key file in the package is greater than the installed version. If the installation package specifies that a component be installed, and the key file of the component is not currently installed, then regardless of whether the key file is protected the installer installs the component. Once any component having a key file protected by WFP is installed, it is permanently installed, and the installer never removes or replaces the component.

## Installation of Assemblies by WFP

WFP for assemblies differs from WFP for system files.

WFP protects Windows Server 2003, Windows XP and Windows 2000 system files by detecting attempts to replace protected system files. This protection is triggered after WFP receives a directory change notification for a file in a protected directory. When WFP receives this notification, it determines which file has changed. If the file is protected, WFP looks up the file signature in a static catalog file to determine if the new file is the correct version. If the file version is not correct, the system replaces the file with the correct version from either the cache or distribution media.

In contrast, WFP of assemblies is dynamic. WFP is extended to files as they are added to the shared side-by-side assembly cache. If an assembly becomes corrupted, WFP will request that the installer replace the file. Windows Installer may or may not be able to replace the file depending on whether the source package is accessible. If the source package is inaccessible, WFP will put up a dialog box stating that it is unable to restore the file.

Note that unmanaged shared side-by-side assemblies, installed in %windir%\\winsxs, are protected by WFP. Unmanaged private assemblies, installed in the application directory, are not protected by WFP. Managed global assemblies installed in the application directory or %windir%\\assembly\\gac are not protected by WFP.

## Related topics

<dl> <dt>

[Windows Resource Protection](../wfp/windows-resource-protection-portal.md)
</dt> </dl>

 

 
