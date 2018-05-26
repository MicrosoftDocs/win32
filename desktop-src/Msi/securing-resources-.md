---
Description: The capability of the Windows Installer to set access permissions on services, files, created folders, and registry entries can help make installation applications more secure.
ms.assetid: a25fcecf-f15f-4772-8f41-d03864484cc9
title: Securing Resources
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Securing Resources

The capability of the Windows Installer to set access permissions on services, files, created folders, and registry entries can help make installation applications more secure. The use of the [MsiLockPermissionsEx](msilockpermissionsex-table.md) or [LockPermissions](lockpermissions-table.md) tables to secure resources is one of the recommended [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md). The MsiLockPermissionsEx table can enable a package author to secure a resource without having to write a [custom action](custom-actions.md).

Beginning with packages developed for Windows Installer 5.0, the [MsiLockPermissionsEx](msilockpermissionsex-table.md) table should replace the use of the [LockPermissions](lockpermissions-table.md) table. The extended functionality provided by the MsiLockPermissionsEx table enables a package to secure Windows [Services](base.services), files, folders, and registry keys. A package should not contain both the MsiLockPermissionsEx and the LockPermissions tables.

Windows Installer 4.5 and earlier ignores the [MsiLockPermissionsEx table](msilockpermissionsex-table.md). Beginning with Windows Installer 5.0, the installation fails with an error message 1941 if the package contains both a [LockPermissions table](lockpermissions-table.md) and MsiLockPermissionsEx table. Existing installation packages that contain only the LockPermissions table can be still be installed using Windows Installer 5.0.

Windows Installer 5.0 processes the information in the [MsiLockPermissionsEx](msilockpermissionsex-table.md) table when it runs the [InstallFiles](installfiles-action.md), [InstallServices](installservices-action.md), [WriteRegistryValues](writeregistryvalues-action.md) and [CreateFolders](createfolders-action.md) standard actions. A securable object must be installed or reinstalled to be secured and it is not possible to append an [Access Control List](security.access_control_lists) (ACL) to an existing object without reinstalling that object.

To specify the service, file, directory, or registry key that is to be secured, enter the identifying information in the LockObject and Table fields of the [MsiLockPermissionsEx](msilockpermissionsex-table.md) table. An object is identified by it's primary key in the [ServiceInstall Table](serviceinstall-table.md), [File Table](file-table.md), [Registry Table](registry-table.md), or [CreateFolder Table](createfolder-table.md).

To request that specified permissions apply to an object, enter a valid security descriptor string in the SDDLText field of the [MsiLockPermissionsEx](msilockpermissionsex-table.md) table using valid [security descriptor definition language](security.security_descriptor_definition_language) (SDDL.) The MsiLockPermissionsEx table can specify a security descriptor that denies permissions, specifies inheritance of permissions from a parent resource, or specifies the permissions of a new account. For a list of all the permissions that can be granted, denied, or inherited see [ACE Strings](security.ace_strings). Windows Installer 5.0 extends the set of available security identifiers (SIDs.) For a list of the valid SIDs, see [SID Strings](security.sid_strings).

Beginning with Windows Installer 5.0, the [FormattedSDDLText](formattedsddltext.md) data type extends the [Formatted](formatted.md) data type. The Windows Installer validates that the FormattedSDDLText string entered in the SDDLText column of the [MsiLockPermissionsEx](msilockpermissionsex-table.md) table conforms to the [Security Descriptor String Format](security.security_descriptor_string_format).

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. The [MsiLockPermissionsEx](msilockpermissionsex-table.md) table and [FormattedSDDLText](formattedsddltext.md) data type are available beginning with Windows Installer 5.0.

 

 



