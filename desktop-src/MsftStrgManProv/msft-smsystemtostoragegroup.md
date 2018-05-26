---
title: MSFT\_SMSystemToStorageGroup class
description: Represents a relationship between a system and a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e358a124-6607-4f58-92b9-e396c0e20003
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToStorageGroup class
- MSFT_SMSystemToStorageGroup class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToStorageGroup
- MSFT_SMSystemToStorageGroup.Parent
- MSFT_SMSystemToStorageGroup.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystemToStorageGroup class

Represents a relationship between a system and a storage group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToStorageGroup
{
  MSFT_SMSystem       REF Parent;
  MSFT_SMStorageGroup REF Child;
};
```

## Members

The **MSFT\_SMSystemToStorageGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToStorageGroup** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage group in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





