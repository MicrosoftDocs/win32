---
Description: Represents a Work Folders sync share, which is a file share that is managed by Work Folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7ad4d727-ab5e-43d1-9797-354256d5a867
ms.prod: windows-server-dev
ms.technology:
- work-folders
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Msft\_SyncShare class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_SyncShare class

Represents a Work Folders sync share, which is a file share that is managed by Work Folders.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("SyncShareServerWmiProvider")]
class Msft_SyncShare
{
  string  Name;
  string  Description;
  string  Type;
  string  Path;
  string  UserFolderName;
  string  User[];
  boolean InheritParentFolderPermission;
  boolean Enabled;
  string  StagingFolder;
  uint64  MaxUploadFile;
  boolean RequireEncryption;
  boolean RequirePasswordAutoLock;
  string  FallbackEnterpriseID;
  string  PasswordAutolockExcludeDomain[];
};
```

## Members

The **Msft\_SyncShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msft\_SyncShare** class has these methods.



| Method                                    | Description                                                                    |
|:------------------------------------------|:-------------------------------------------------------------------------------|
| [**Disable**](disable-msft-syncshare.md) | Disables the Work Folders share.<br/>                                    |
| [**Enable**](enable-msft-syncshare.md)   | Enables the Work Folders share.<br/>                                     |
| [**Repair**](repair-msft-syncshare.md)   | Resets the Work Folders sync share metadata for the specified user.<br/> |



 

### Properties

The **Msft\_SyncShare** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets the description of the Work Folders sync share.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the Work Folders sync share is enabled. **True** if the Work Folders sync share is enabled; otherwise **false**.

</dd> <dt>

**FallbackEnterpriseID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the fallback Enterprise ID that the sync share uses if it cannot successfully query Active Directory Domain Services (AD DS). If the server cannot successfully query AD DS, the server uses the fully qualified domain name (FQDN) of the sync server as the fallback Enterprise ID unless you specify a different Enterprise ID by using this property. The Enterprise ID is issued by the Work Folders client to encrypt data on the PC or device. The Enterprise ID is typically constructed by querying AD DS for the primary SMTP address of the user, removing the username and ampersand (user@), and sending the remainder to the client as the Enterprise ID. For example, "EvanNarvaez@Contoso.com" yields the "contoso.com" Enterprise ID.

</dd> <dt>

**InheritParentFolderPermission**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates that the sync share inherits the permissions of the parent folder. If you specify this property, the user folder inherits permissions from the parent folder of the sync share, and administrators can access the data. If you do not specify this property, by default each user is granted exclusive access to their user folder, and administrators have no access rights.

</dd> <dt>

**MaxUploadFile**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets the maximum file size for an upload to the Work Folders sync share, in bytes.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the name of the Work Folders sync share. The **Name** property has the following requirements:

-   Must be unique on the sync server.
-   Can have a maximum of 75 characters.
-   Cannot start or end a name with a space.
-   Cannot end a name with a period.
-   Cannot use a reserved name, such as COM1, LPT1, NUL, etc.
-   Cannot contain the following characters: &lt;&gt;:\\"/\\\\\|?\*.

</dd> <dt>

**PasswordAutolockExcludeDomain**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies a list of domain names in fully qualified domain name (FQDN) format whose clients are to be exempted from the password policy. If the **RequirePasswordAutoLock** property on the sync share is **False**, then this property has no effect. If the **RequirePasswordAutoLock** property is **True**, then clients that are members of the specified domains are not requested by Work Folders to enforce password length and lock policies on the device. It is assumed that their security is managed by the Group Policy of their domain.

**Windows 8.1 and Windows Server 2012 R2:** This property is not supported before Windows 8.1 Update and Windows Server 2012 R2 Update.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the path to the Work Folders sync share. Once the sync share is created the path cannot be changed.

</dd> <dt>

**RequireEncryption**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a value that indicates whether this Work Folders sync share requires encryption. **True** if the Work Folders sync share requires encryption; otherwise **false**.

</dd> <dt>

**RequirePasswordAutoLock**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the device meets the following policies:

-   Password minimum length of six characters.
-   Lock screen activates after a maximum of 15 minutes.
-   User account lockout after a maximum of 10 failed sign-in attempts.

</dd> <dt>

**StagingFolder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the path to the staging directory for the Work Folders sync share.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Retrieves the type of the Work Folders sync share.

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies an array of user names or security groups who are allowed to sync data with this sync share. Add accounts or security groups in Security Accounts Manager (SAM) account format.

</dd> <dt>

**UserFolderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies a folder-naming format for the user folder on the sync share. To maintain compatibility with existing user folders that use aliases for their names, specify *user*, which is required, or omit this property. To eliminate conflicts between identical user aliases in different domains, specify *user*@*domain*. You can also specify a relative path under the sync share root; for example, UserData\\*user*. Sync share creates each user folder during the first sync operation, if it doesn t already exist. If the user folder exists, confirm that the user has Read/Write or Full Control permissions and is the owner of their folder, unless the folder is owned by an Administrators group.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\Microsoft\\Windows\\SyncShareServer<br/>                                        |
| MOF<br/>                      | <dl> <dt>ECSServer.Mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>SyncShareSvc.dll</dt> </dl> |



## See also

<dl> <dt>

[Work Folders Management Classes](sync-share-server-management-classes.md)
</dt> </dl>

 

 




