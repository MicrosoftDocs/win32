---
title: Msft\_MiStreamTasks class
description: The Msft\_MiStreamTasks WMI class evaluates queries of Software Inventory Logging data, and publishes the results.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 42343b12-3b06-4310-ac18-48f0b33ebcdd
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiStreamTasks class Software Inventory Logging
- Msft_MiStreamTasks class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiStreamTasks
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiStreamTasks class

The **Msft\_MiStreamTasks** WMI class evaluates queries of Software Inventory Logging data, and publishes the results.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.1"), dynamic, provider("mistreamprov"), AMENDMENT]
class Msft_MiStreamTasks
{
};
```

## Members

The **Msft\_MiStreamTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msft\_MiStreamTasks** class has these methods.



| Method                                        | Description                                                                                                                                                                                                                                                                                                                            |
|:----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Collect**](collect-msft-mistreamtasks.md) | Evaluates a list of queries of Software Inventory Logging data, and then returns an instance of the query results.<br/>                                                                                                                                                                                                          |
| [**Flush**](flush-msft-mistreamtasks.md)     | Publishes any query results that were saved by the [**Push**](push-msft-mistreamtasks.md) method. The [**Flush**](flush-msft-mistreamtasks.md) method can publish query results to the HTTPS endpoint or the key/value pair exchange of a virtual machine.<br/>                                                                |
| [**Push**](push-msft-mistreamtasks.md)       | Evaluates a list of queries of Software Inventory Logging data, and then publishes the results to an HTTPS endpoint or the key/value pair exchange of a virtual machine. If this method cannot publish the results, it saves them so they can be published later with the [**Flush**](flush-msft-mistreamtasks.md) method.<br/> |



 

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

[Software Inventory Logging WMI Stream Provider Classes](software-inventory-logging-wmi-stream-provider-classes.md)
</dt> </dl>

 

 





