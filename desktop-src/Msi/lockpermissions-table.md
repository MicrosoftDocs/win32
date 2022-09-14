---
description: Used to secure individual portions of an application in a locked-down environment. It can be used with the installation of files, registry keys, and created folders.
ms.assetid: 7c20e211-7704-49c2-a0c5-aaa695a09764
title: LockPermissions Table
ms.topic: article
ms.date: 05/31/2018
---

# LockPermissions Table

The LockPermissions Table is used to secure individual portions of an application in a locked-down environment. It can be used with the installation of files, registry keys, and created folders.

A package intended for installation in Windows Server 2008 R2 or Windows 7 should use the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) rather than the LockPermissions Table. Windows Installer versions earlier than Windows Installer 5.0 ignore the MsiLockPermissionsEx Table. Windows Installer 5.0 can install an package that contains the LockPermissions Table. Beginning with Windows Installer 5.0, installation of a package that contains both the MsiLockPermissionsEx Table and the LockPermissions Table fails and returns Windows Installer error message 1941.

The LockPermissions Table has the following columns.



| Column     | Type                               | Key | Nullable |
|------------|------------------------------------|-----|----------|
| LockObject | [Identifier](identifier.md)       | Y   | N        |
| Table      | [Text](text.md)                   | Y   | N        |
| Domain     | [Formatted](formatted.md)         | Y   | Y        |
| User       | [Formatted](formatted.md)         | Y   | N        |
| Permission | [DoubleInteger](doubleinteger.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="LockObject"></span><span id="lockobject"></span><span id="LOCKOBJECT"></span>LockObject
</dt> <dd>

This column and the Table column together specify the file, directory, or registry key that is to be secured. The LockObject column is a foreign key that points to the primary key of the table specified by the Table column.

</dd> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

This column and the LockObject column specify the file, directory, or registry key that is to be secured. In the Table column, enter File, Registry, or CreateFolder to specify a LockObject listed in the [File Table](file-table.md), [Registry Table](registry-table.md), or [CreateFolder Table](createfolder-table.md).

</dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>Domain
</dt> <dd>

The column that identifies the domain of the user for which permissions are to be set. This is the name of a stand-alone machine or a domain name. The column data type is [Formatted](formatted.md), and you may use the string \[%USERDOMAIN\] in this field to get the value of the USERDOMAIN environment variable for the current domain. To get any other domain requires using [Custom Actions](custom-actions.md). For more information, see the Custom Action Table.

</dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>User
</dt> <dd>

The column that identifies the localized name of the user for which permissions are to be set. This name must be located on the machine or domain. The installation fails if the machine or domain controller does not recognize the domain and user combination or if the user's security identifier (SID) cannot be retrieved. Multiple users can be specified for a single LockObject.

The common user names "Everyone" and "Administrators" may be entered in English and are mapped to well-known SIDs. LocalSystem is given full control in all security descriptors created through the LockPermissions Table. You can use the [**ComputerName Property**](computername.md), [**LogonUser Property**](logonuser.md) or [**USERNAME Property**](username.md) in this field to get the current user. A custom action is required to enter the localized name of any other user or group.

You can use multiple records with identical LockObject and Table entries (but different User entries) to specify access control lists for multiple users.

</dd> <dt>

<span id="Permission"></span><span id="permission"></span><span id="PERMISSION"></span>Permission
</dt> <dd>

The column that identifies the integer description of system privileges. The following gives the most commonly used values (a complete list exists in Winnt.h).



| Privilege                                                              | Description                     |
|------------------------------------------------------------------------|---------------------------------|
| GENERIC\_ALL<br/> 0X10000000<br/> 268435456<br/>     | Read, write, and execute access |
| GENERIC\_EXECUTE<br/> 0X20000000<br/> 536870912<br/> | Execute access                  |
| GENERIC\_WRITE<br/> 0X40000000<br/> 1073741824<br/>  | Write access                    |



 

You cannot specify GENERIC\_READ in the Permission column. Attempting to do so will fail. Instead, you must specify a value such as KEY\_READ or FILE\_GENERIC\_READ.

Null entered in this column is reserved for future use.

</dd> </dl>

## Remarks

The [InstallFiles](installfiles-action.md), [WriteRegistryValues](writeregistryvalues-action.md), and [CreateFolders](createfolders-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

Permission can only be set in the LockPermissions Table for users that already exist on the computer or domain. An attempt to set permissions for an unknown user causes the installation to fail, even if that user account is created during the installation by a deferred custom action.

It is recommended that the system administrator's local group be included in all access control lists (ACL). This ensures that the system administrator can access and maintain objects.

Every file, registry key, or directory that is listed in the LockPermissions Table receives an explicit security descriptor, whether it replaces an existing object or not. The Windows Installer attempts to preserve the security on objects that already exist on the system. If an object is not listed in the LockPermissions Table, and replaces an existing object, the replacement gets the security settings of the object that it replaces.

If an object is not listed in the LockPermissions Table, and does not replace an existing object, it receives no explicit security descriptor. The access to the new object is based on the attributes of its parent or container object. If an object is not listed in the table, and replaces an object with no explicit security descriptor, the access to the new object is based on the attributes of its parent or container object.

The Windows Installer sets the [**UserSID**](usersid.md) property to the security identifier (SID) or the user running the installation.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
[ICE55](ice55.md)  
</dl>

 

 




