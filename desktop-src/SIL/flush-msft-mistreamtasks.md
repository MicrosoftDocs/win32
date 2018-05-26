---
title: Flush method of the Msft\_MiStreamTasks class
description: Publishes any query results that were saved by the Push method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 59c82a61-9238-4211-b609-d024d8293617
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Flush method Software Inventory Logging
- Flush method Software Inventory Logging , Msft_MiStreamTasks class
- Msft_MiStreamTasks class Software Inventory Logging , Flush method
topic_type:
- apiref
api_name:
- Msft_MiStreamTasks.Flush
api_location:
- MiStreamProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Flush method of the Msft\_MiStreamTasks class

Publishes any query results that were saved by the [**Push**](push-msft-mistreamtasks.md) method. The **Flush** method can publish query results to an HTTPS endpoint, or the key/value pair exchange of a virtual machine.

**Note**  For information on retrieving or updating the HTTPS endpoint, see [**MsftSil\_ManagementTasks**](msftsil-managementtasks.md).

## Syntax


```mof
uint32 Flush();
```



## Parameters

This method has no parameters.

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

 

 





