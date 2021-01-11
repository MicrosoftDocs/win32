---
description: The MsiLockPermissionsEx Table can be used to secure services, files, registry keys, and created folders.
ms.assetid: c642f02d-07fa-463f-8151-769c28a71a5c
title: MsiLockPermissionsEx Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiLockPermissionsEx Table

The MsiLockPermissionsEx Table can be used to secure services, files, registry keys, and created folders.

A package should not contain both the MsiLockPermissionsEx Table and the [LockPermissions Table](lockpermissions-table.md).

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This table is recommended for packages intended for installation with Windows Installer 5.0 or later.

The MsiLockPermissionsEx Table has the following columns.



| Column               | Type                                       | Key | Nullable |
|----------------------|--------------------------------------------|-----|----------|
| MsiLockPermissionsEx | [Text](text.md)                           | Y   | N        |
| LockObject           | [Identifier](identifier.md)               | N   | N        |
| Table                | [Text](text.md)                           | N   | N        |
| SDDLText             | [FormattedSDDLText](formattedsddltext.md) | N   | N        |
| Condition            | [Condition](condition.md)                 | N   | Y        |



 

## Columns

<dl> <dt>

<span id="MsiLockPermissionsEx"></span><span id="msilockpermissionsex"></span><span id="MSILOCKPERMISSIONSEX"></span>MsiLockPermissionsEx
</dt> <dd>

This is the primary key of this table.

</dd> <dt>

<span id="LockObject"></span><span id="lockobject"></span><span id="LOCKOBJECT"></span>LockObject
</dt> <dd>

This column and the Table column together specify the file, directory, registry key, or service that is to be secured. The LockObject column is a foreign key that points to the primary key of the table specified by the Table column.

</dd> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

This column and the LockObject column specify the file, directory, registry key, or service that is to be secured. In the Table column, enter File, Registry, CreateFolder, or ServiceInstall to specify a LockObject listed in the [File Table](file-table.md), [Registry Table](registry-table.md), [CreateFolder Table](createfolder-table.md), or [ServiceInstall Table](serviceinstall-table.md).

</dd> <dt>

<span id="SDDLText"></span><span id="sddltext"></span><span id="SDDLTEXT"></span>SDDLText
</dt> <dd>

Enter the SDDL string to indicate permissions to apply to selected object. The SDDL must be provided in [Security Descriptor String Format](../secauthz/security-descriptor-string-format.md).

This does not support private or public properties.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

This column contains a conditional expression used to determine whether to apply the specified permission. If the condition evaluates to **FALSE**, the permission is not applied. If the condition evaluates to **TRUE**, the permission is applied.

</dd> </dl>

## Remarks

See [Securing Resources](securing-resources-.md)for more information about securing services, files, registry keys, and created folders.

Use the MsiLockPermissionsEx Table to secure objects for a user account that is being created during the installation. The user account must already exist when the installation secures the object. Create the user account before installing the file, registry key, folder or service being secured.

If a LockObject and Table pair in this table has more than one conditional expression that evaluates to true, the installation fails and Windows Installer returns an error message 1942.

If the [FormattedSDDLText](formattedsddltext.md) string in the SDDLText field cannot be resolved into a valid SDDL string, the installation fails and Windows Installer returns an error message 1943.

If the user does not have sufficient privileges to set the security descriptor specified by the SDDLText field on a file or folder, the installation fails and Windows Installer returns an error message 1926.

If the user does not have sufficient privileges to set the security descriptor specified by the SDDLText field on a registry key, the installation fails and Windows Installer returns an error message 1401.

If the user does not have sufficient privileges to set the security descriptor specified by the SDDLText field on a service, the installation fails and Windows Installer returns an error message 1944.

## Validation

<dl>

[ICE104](ice-104.md)  
[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 
