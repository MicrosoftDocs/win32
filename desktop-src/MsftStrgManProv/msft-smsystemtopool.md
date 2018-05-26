---
title: MSFT\_SMSystemToPool class
description: Represents a relationship between a system and a storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9ff710a-6de9-4b4f-a398-07288bb34a26
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToPool class
- MSFT_SMSystemToPool class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToPool
- MSFT_SMSystemToPool.Parent
- MSFT_SMSystemToPool.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystemToPool class

Represents a relationship between a system and a storage pool.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToPool
{
  MSFT_SMSystem REF Parent;
  MSFT_SMPool   REF Child;
};
```

## Members

The **MSFT\_SMSystemToPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToPool** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage pool in the relationship.

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

 

 





