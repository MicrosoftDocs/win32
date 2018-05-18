---
title: MSFT\_FileShareAccessControlEntry class
description: Models the subsystem's concept of an access control entry for a file share.
ms.assetid: '0F2A94A2-BFA9-4895-B93F-71A502850F1E'
keywords: ["MSFT_FileShareAccessControlEntry class Windows Storage Management API", "MSFT_FileShareAccessControlEntry class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_FileShareAccessControlEntry
- MSFT_FileShareAccessControlEntry.AccountName
- MSFT_FileShareAccessControlEntry.AccessControlType
- MSFT_FileShareAccessControlEntry.AccessRight
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_FileShareAccessControlEntry class

Models the subsystem's concept of an access control entry for a file share.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileShareAccessControlEntry
{
  String AccountName;
  UInt16 AccessControlType;
  UInt16 AccessRight;
};
```

## Members

The **MSFT\_FileShareAccessControlEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FileShareAccessControlEntry** class has these properties.

<dl> <dt>

**AccessControlType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Denotes the access type:

<dl> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (0)
</dt> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>**Deny** (1)
</dt> </dl>

</dd> <dt>

**AccessRight**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Denotes the access right:

<dl> <dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>**Full** (0)
</dt> <dt>

<span id="Modify"></span><span id="modify"></span><span id="MODIFY"></span>**Modify** (1)
</dt> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>**Read** (2)
</dt> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** (3)
</dt> </dl>

</dd> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the account to which the access right is granted.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





