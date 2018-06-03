---
title: Software Inventory Logging WMI Stream Provider Classes
description: The stream provider is the Software Inventory Logging Engine. It evaluates queries and method invocations that request Software Inventory Logging data and returns or publishes the results.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2828315D-9926-41E9-9716-43C4E0CA7F5F
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Software Inventory Logging WMI Stream Provider Classes

The stream provider is the Software Inventory Logging Engine. It evaluates queries and method invocations that request Software Inventory Logging data and returns or publishes the results. The classes are defined in MiStreamProv.mof. The Software Inventory Logging WMI stream provider provides the following classes.

## In this section

<dl> <dt>

[**Msft\_MiStream**](msft-mistream.md)
</dt> <dd>

The [**Msft\_MiStream**](msft-mistream.md) WMI class is an abstract base class that represents a data stream of command or query data sent from a Software Inventory Logging data provider to the Software Inventory Logging stream provider.

</dd> <dt>

[**Msft\_MiCompare**](msft-micompare.md)
</dt> <dd>

The [**Msft\_MiCompare**](msft-micompare.md) WMI class compares the current output of a stream identified by the given ID with the previous output of the input stream and, if identical, suppress the current output.

</dd> <dt>

[**Msft\_MiCompareSuppression**](msft-micomparesuppression.md)
</dt> <dd>

The [**Msft\_MiCompareSuppression**](msft-micomparesuppression.md) WMI class represents the output instance produced when the input of the output stream is suppressed.

</dd> <dt>

[**Msft\_MiCommand**](msft-micommand.md)
</dt> <dd>

The [**Msft\_MiCommand**](msft-micommand.md) WMI class encapsulates a command request from a Software Inventory Logging data provider, and exposes the method data in the request.

</dd> <dt>

[**Msft\_MiMerge**](msft-mimerge.md)
</dt> <dd>

The [**Msft\_MiMerge**](msft-mimerge.md) WMI class represents a merged data stream. A merged data stream contains a [**Msft\_MiQuery**](msft-miquery.md) object and a [**Msft\_MiCommand**](msft-micommand.md) object.

</dd> <dt>

[**Msft\_MiPipeline**](msft-mipipeline.md)
</dt> <dd>

The [**Msft\_MiPipeline**](msft-mipipeline.md) WMI class represents a pipeline that transports data streams throughout the Software Inventory Logging stream provider.

</dd> <dt>

[**Msft\_MiQuery**](msft-miquery.md)
</dt> <dd>

The [**Msft\_MiQuery**](msft-miquery.md) WMI class represents a data stream that encapsulates a query request from a Software Inventory Logging data provider, and exposes the query data in the stream.

</dd> <dt>

[**Msft\_MiStreamTasks**](msft-mistreamtasks.md)
</dt> <dd>

The [**Msft\_MiStreamTasks**](msft-mistreamtasks.md) WMI class evaluates queries of Software Inventory Logging data, and publishes the results.

</dd> </dl>

## Related topics

<dl> <dt>

[Software Inventory Logging Reference](https://msdn.microsoft.com/library/windows/desktop/dn440663)
</dt> </dl>

 

 




