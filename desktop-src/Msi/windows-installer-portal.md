---
description: Installer engine used to install applications or updates or services run on Windows. Configures and repairs installed applications. Write custom msi packages to create an exe setup installation or update or upgrade for an application.
ms.assetid: c90b8cbe-d7a1-44ad-ae65-80115bd55e4f
title: Windows Installer
ms.topic: article
ms.date: 05/19/2020
---

# Windows Installer

> [!NOTE]
> This documentation is intended for software developers who want to use Windows Installer to build installer packages for applications. If you're looking for a redistributable for Windows Installer 4.5 and earlier, see [this article](windows-installer-redistributables.md). Note that there is no redistributable for Windows Installer 5.0. This version is included with the OS in Windows 7, Windows Server 2008 R2, and later client and server releases (including Windows 10).

Microsoft Windows Installer is an installation and configuration service provided with Windows. The installer service enables customers to provide better corporate deployment and provides a standard format for component management. The installer also enables the advertisement of applications and features according to the operating system. For more information, see [Platform Support of Advertisement](platform-support-of-advertisement.md).

This documentation describes Windows Installer 5.0 and earlier versions. Not all the capabilities available in later Windows Installer versions are available in earlier versions. This documentation does not describe versions earlier than Windows Installer 2.0. Installation packages and patches that are created for Windows Installer 2.0 can still be installed by using Windows Installer 3.0 and later.

Windows Installer 3.0 and later, can install multiple patches with a single transaction that integrates installation progress, rollback, and reboots. The installer can apply patches in a specified order regardless of the order that the patches are provided to the system. Patching using Windows Installer 3.0 only updates files affected by the patch and can be significantly faster than earlier installer versions. Patches installed with Windows Installer 3.0 or later can be uninstalled in any order to leave the state of the product the same as if the patch was never installed. Accounts with administrator privileges can use the API of Windows Installer 3.0 and later to query and inventory product, feature, component, and patch information. The installer can be used to read, edit, and replace source lists for network, URL, and media sources. Administrators can enumerate across user and install contexts, and manage source lists from an external process.

Windows Installer 4.5 and later can install multiple installation packages using [*transaction processing*](t-gly.md). If all the packages in the transaction cannot be installed successfully, or if the user cancels the installation, the Windows Installer can roll back changes and restore the computer to its original state. The installer ensures that all the packages belonging to a multiple-package transaction are installed or none of the packages are installed.

Beginning with Windows Installer 5.0, a package can be authored to secure new accounts, Windows [Services](../services/services.md), files, folders, and registry keys. The package can specify a security descriptor that denies permissions, specifies inheritance of permissions from a parent resource, or specifies the permissions of a new account. For information, see [Securing Resources](securing-resources-.md). The Windows Installer 5.0 service can enumerate all components installed on the computer and obtain the key path for the component. For more information, see [Enumerating Components](enumerating-components-.md). By [Using Services Configuration](using-services-configuration.md), Windows Installer 5.0 packages can customize the services on a computer. Setup developers can use Windows Installer 5.0 and [Single Package Authoring](single-package-authoring.md) to develop single installation packages capable of installing an application in either the per-machine or per-user [installation context](installation-context.md).

## Where applicable

Windows Installer enables the efficient installation and configuration of your products and applications running on Windows. The installer provides new capabilities to advertise features without installing them, to install products on demand, and to add user customizations.

Windows Installer 5.0 running on Windows Server 2012 or Windows 8 supports the installation of approved apps on Windows RT. A Windows Installer package, patch, or transform that has not been signed by Microsoft cannot be installed on Windows RT. The [**Template Summary**](template-summary.md) property indicates the platform that is compatible with an installation database and in this case should include the value for Windows RT.

Windows Installer is intended for the development of desktop style applications.

## Developer audience

This documentation is intended for software developers who want to make applications that use Windows Installer. It provides general background information about installation packages and the installer service. It contains complete descriptions of the application programming interface and elements of the installer database. This documentation also contains supplemental information for developers who want to use a table editor or a package creation tool to make or maintain an installation.

## Run-time requirements

Windows Installer 5.0 is included with, Windows 7, Windows Server 2008 R2, and later releases. There is no redistributable for Windows Installer 5.0.

Versions earlier than Windows Installer 5.0 were released with Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000. [Windows Installer Redistributables](windows-installer-redistributables.md) are available for Windows Installer 4.5 and some earlier versions.

* Windows Installer 4.5 requires Windows Server 2008, Windows Vista, Windows XP with Service Pack 2 (SP2) and later, and Windows Server 2003 with Service Pack 1 (SP1) and later.

* Windows Installer 4.0 requires Windows Vista or Windows Server 2008. There is no redistributable for installing Windows Installer 4.0 on other operating systems. An updated version of Windows Installer 4.0, which does not add any new features, is available in Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.

* Windows Installer 3.1 requires Windows Server 2003, Windows XP, or Windows 2000 with Service Pack 3 (SP3).

* Windows Installer 3.0 requires Windows Server 2003, Windows XP, or Windows 2000 with SP3. Windows Installer 3.0 is included in Windows XP with Service Pack 2 (SP2). It is available as a redistributable for Windows 2000 Server with Service Pack 3 (SP3) and Windows 2000 Server with Service Pack 4 (SP4), Windows XP RTM and Windows XP with Service Pack 1 (SP1), and Windows Server 2003 RTM.

* Windows Installer 2.0 is contained in Windows Server 2003 and Windows XP.

* Windows Installer 2.0 is available as a package for installing or upgrading to Windows Installer 2.0 on Windows 2000. This package should not be used to install or upgrade Windows Installer 2.0 on Windows Server 2003 and Windows XP.

## In this section



| Topic                                                                                       | Description                                                  |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [Roadmap](roadmap-to-windows-installer-documentation.md)<br/>                        | A guide to Windows Installer documentation.<br/>       |
| [Overview](about-windows-installer.md)<br/>                                          | General information about the installer.<br/>          |
| [What's New in Windows Installer](what-s-new-in-windows-installer.md)<br/>           | Lists additions and changes to Windows Installer.<br/> |
| [Reference](installer-function-reference.md)<br/>                                    | Documentation of Windows Installer functions.<br/>     |
| [Windows Installer Scripting Examples](windows-installer-scripting-examples.md)<br/> | Windows Installer examples using script.<br/>          |



 

 

 
