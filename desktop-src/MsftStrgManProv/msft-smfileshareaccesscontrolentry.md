---
title: MSFT\_SMFileShareAccessControlEntry class
description: Represents an access control setting for a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b01d8f17-f28f-420c-9634-1d2ed8cd7b14
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMFileShareAccessControlEntry class
- MSFT_SMFileShareAccessControlEntry class, described
topic_type:
- apiref
api_name:
- MSFT_SMFileShareAccessControlEntry
- MSFT_SMFileShareAccessControlEntry.ObjectId
- MSFT_SMFileShareAccessControlEntry.Identifier
- MSFT_SMFileShareAccessControlEntry.AccountName
- MSFT_SMFileShareAccessControlEntry.AccessControlType
- MSFT_SMFileShareAccessControlEntry.AccessRight
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMFileShareAccessControlEntry class

Represents an access control setting for a file share. This security setting indicates whether the specified account has access to the file share.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage")]
class MSFT_SMFileShareAccessControlEntry : MSFT_SMStorageObject
{
  String ObjectId;
  String Identifier;
  string AccountName;
  uint16 AccessControlType;
  uint16 AccessRight;
};
```

## Members

The **MSFT\_SMFileShareAccessControlEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFileShareAccessControlEntry** class has these properties.

<dl> <dt>

**AccessControlType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An indicator of the type of the access control setting.

The possible values are.

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

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the extended permission granted to the account.

The possible values are.

<dt>

<span id="TBD"></span><span id="tbd"></span>

**TBD** (0)


</dt> <dd></dd> <dt>

<span id="TBD"></span><span id="tbd"></span>

**TBD** (1)


</dt> <dd></dd> <dt>

<span id="TBD"></span><span id="tbd"></span>

**TBD** (2)


</dt> <dd></dd> <dt>

<span id="TBD"></span><span id="tbd"></span>

**TBD** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the account that is assigned to the setting.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





