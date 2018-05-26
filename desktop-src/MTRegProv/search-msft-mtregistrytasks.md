---
title: Search method of the MSFT\_MTRegistryTasks class
description: Searches the specified string in registry tree represented by the root registry key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b109dcd1-e0b7-46c4-9a6e-4c38d38e69a6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Search method
- Search method, MSFT_MTRegistryTasks class
- MSFT_MTRegistryTasks class, Search method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryTasks.Search
api_location:
- RegProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Search method of the MSFT\_MTRegistryTasks class

Searches the specified string in registry tree represented by the root registry key.

## Syntax


```mof
uint32 Search(
  [in]  string                Value,
  [in]  string                KeyName,
  [in]  uint8                 Options,
  [out] MSFT_MTRegistryObject Results[]
);
```



## Parameters

<dl> <dt>

*Value* \[in\]
</dt> <dd>

The text to search.

</dd> <dt>

*KeyName* \[in\]
</dt> <dd>

The name of root registry key to search under it.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Miscellaneous search options. At default, all options are enabled.

</dd> <dt>

*Results* \[out\]
</dt> <dd>

On success, returns a list of [**MSFT\_MTRegistryObject**](msft-mtregistryobject.md) embedded instances containing the search results.

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

[**MSFT\_MTRegistryTasks**](msft-mtregistrytasks.md)
</dt> </dl>

 

 





