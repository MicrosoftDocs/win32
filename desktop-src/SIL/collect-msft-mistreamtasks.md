---
title: Collect method of the Msft\_MiStreamTasks class
description: Evaluates a list of queries of Software Inventory Logging data, and then returns an instance of the query results.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '580cb170-7c97-41dd-9698-b26c1e4b622e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Collect method Software Inventory Logging", "Collect method Software Inventory Logging , Msft_MiStreamTasks class", "Msft_MiStreamTasks class Software Inventory Logging , Collect method"]
topic_type:
- apiref
api_name:
- Msft_MiStreamTasks.Collect
api_location:
- MiStreamProv.dll
api_type:
- COM
---

# Collect method of the Msft\_MiStreamTasks class

Evaluates a list of queries of Software Inventory Logging data, and then returns an instance of the query results.

## Syntax


```mof
uint32 Collect(
  [in]  string Filename,
  [out] object Results[]
);
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

**Windows Server 2012 R2:** The parameter name is *filename*.

The name of the file that contains the queries.

</dd> <dt>

*Results* \[out\]
</dt> <dd>

On success, streams a list of objects that receive the instance of the query results.

</dd> </dl>

## Return value

If this method succeeds, it returns 0. If this method fails, it returns 1. For a complete list of return values, see [**MI\_Result**](https://msdn.microsoft.com/library/hh437490) enumeration.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msft\_MiStreamTasks**](msft-mistreamtasks.md)
</dt> </dl>

 

 





