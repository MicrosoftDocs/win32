---
title: MSFT\_SMPrimordialPoolToConcretePool class
description: Represents a relationship between a concrete storage pool and a primordial storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3793c452-5862-48eb-b0e4-4cae0cbb3515'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMPrimordialPoolToConcretePool class", "MSFT_SMPrimordialPoolToConcretePool class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMPrimordialPoolToConcretePool
- MSFT_SMPrimordialPoolToConcretePool.Parent
- MSFT_SMPrimordialPoolToConcretePool.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMPrimordialPoolToConcretePool class

Represents a relationship between a concrete storage pool and a primordial storage pool.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMPrimordialPoolToConcretePool
{
  MSFT_SMPool REF Parent;
  MSFT_SMPool REF Child;
};
```

## Members

The **MSFT\_SMPrimordialPoolToConcretePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMPrimordialPoolToConcretePool** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the concrete storage pool.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the primordial storage pool.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





