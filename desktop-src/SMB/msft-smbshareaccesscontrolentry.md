---
title: MSFT\_SmbShareAccessControlEntry class
description: Represents the access permissions that have been granted to a share's users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6812e57-2757-48ab-a61c-beee50332e56
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbShareAccessControlEntry class SMB
- MSFT_SmbShareAccessControlEntry class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbShareAccessControlEntry
- MSFT_SmbShareAccessControlEntry.Name
- MSFT_SmbShareAccessControlEntry.ScopeName
- MSFT_SmbShareAccessControlEntry.AccountName
- MSFT_SmbShareAccessControlEntry.AccessControlType
- MSFT_SmbShareAccessControlEntry.AccessRight
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SmbShareAccessControlEntry class

Represents the access permissions that have been granted to a share's users.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("7"), DisplayName("Smb Share Access Control Entry"), AMENDMENT]
class MSFT_SmbShareAccessControlEntry
{
  string Name;
  string ScopeName;
  string AccountName;
  uint32 AccessControlType;
  uint32 AccessRight;
};
```

## Members

The **MSFT\_SmbShareAccessControlEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SmbShareAccessControlEntry** class has these properties.

<dl> <dt>

**AccessControlType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

<dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** (0)


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**AccessRight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SMB-style access right that is granted to the trustee. **Custom** is returned when a share ACE is encountered that does not specify a set of access rights that correspond to one of the SMB-style access rights.

<dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>

**Full** (0)


</dt> <dd></dd> <dt>

<span id="Change"></span><span id="change"></span><span id="CHANGE"></span>

**Change** (1)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (2)


</dt> <dd></dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

**Custom** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the account to which the access right is granted.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the share.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the endpoint to which the share is scoped.

</dd> </dl>

## Remarks

There will be one instance of this class per share per ACL entry in the share's security descriptor.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





