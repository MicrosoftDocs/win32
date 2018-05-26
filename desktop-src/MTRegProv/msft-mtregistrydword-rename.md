---
title: Rename method of the MSFT\_MTRegistryDword class
description: Renames the registry value object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62C10015-4D8B-4EB4-B8DC-4F76E6F4199D
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSFT_MTRegistryDword interface
- MSFT_MTRegistryDword interface, Rename method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryDword.Rename
api_location:
- RegProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the MSFT\_MTRegistryDword class

Renames the registry value object.

## Syntax


```mof
uint32 Rename(
  [in]  string               NewName,
  [out] MSFT_MTRegistryValue Result
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The fully qualified new name of the object.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

On success, returns an [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md) embedded instance containing the new object with the new path.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTRegistryDword**](msft-mtregistrydword.md)
</dt> </dl>

 

 





