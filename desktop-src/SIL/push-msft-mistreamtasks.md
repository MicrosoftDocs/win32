---
title: Push method of the Msft\_MiStreamTasks class
description: Evaluates a list of queries of Software Inventory Logging data, and then publishes the results to an HTTPS endpoint or the key/value pair exchange of a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5cb46df2-3446-4b6e-a916-95cd4fa4e963
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Push method Software Inventory Logging
- Push method Software Inventory Logging , Msft_MiStreamTasks class
- Msft_MiStreamTasks class Software Inventory Logging , Push method
topic_type:
- apiref
api_name:
- Msft_MiStreamTasks.Push
api_location:
- MiStreamProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Push method of the Msft\_MiStreamTasks class

Evaluates a list of queries of Software Inventory Logging data, and then publishes the results to an HTTPS endpoint or the key/value pair exchange of a virtual machine. If this method cannot publish the results, it saves them so they can be published later with the [**Flush**](flush-msft-mistreamtasks.md) method.

**Note**  For information on retrieving or updating the HTTPS endpoint or the key/value pair exchange, see [**MsftSil\_ManagementTasks**](msftsil-managementtasks.md).

## Syntax


```mof
uint32 Push(
  [in] string  Filename,
  [in] boolean CheckCollectionHistory
);
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

**Windows Server 2012 R2:** The parameter name is *filename*.

The name of the file that contains the queries.

</dd> <dt>

*CheckCollectionHistory* \[in\]
</dt> <dd>

Set **true** to suppress the output based on the previous collection history; otherwise, **false**.

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

</dd> </dl>

## Return value

If this method succeeds, it returns 0. If this method fails, it returns 1. For a complete list of return values, see [**MI\_Result**](https://msdn.microsoft.com/library/hh437490) enumeration.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msft\_MiStreamTasks**](msft-mistreamtasks.md)
</dt> </dl>

 

 





