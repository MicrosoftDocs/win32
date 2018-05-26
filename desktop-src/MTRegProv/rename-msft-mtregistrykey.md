---
title: Rename method of the MSFT\_MTRegistryKey class
description: Renames the registry object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee653ac5-a819-428e-ba1a-915ae266eaa4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSFT_MTRegistryKey class
- MSFT_MTRegistryKey class, Rename method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryKey.Rename
api_location:
- RegProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the MSFT\_MTRegistryKey class

Renames the registry object.

## Syntax


```mof
uint32 Rename(
  [in]  string             NewName,
  [out] MSFT_MTRegistryKey Result
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

On success, returns an [**MSFT\_MTRegistryKey**](msft-mtregistrykey.md) embedded instance with the new path.

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

[**MSFT\_MTRegistryKey**](msft-mtregistrykey.md)
</dt> </dl>

 

 





