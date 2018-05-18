---
Description: 'Contains counter data information for the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e8b2a97e-00d4-4189-be56-c9e93e65cc7e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerNodeCounters interface
---

# ISchedulerNodeCounters interface

Contains counter data information for the node.

To get this interface, call the [**ISchedulerNode::GetCounters**](ischedulernode-getcounters.md) method.

## Members

The **ISchedulerNodeCounters** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerNodeCounters** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISchedulerNodeCounters** interface has these properties.



| Property                                                                       | Access type          | Description                                                                         |
|:-------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------|
| [**BusyCoreCount**](ischedulernodecounters-busycorecount.md)<br/>       | Read-only<br/> | Retrieves the number of cores on the node that are busy processing jobs.<br/> |
| [**IdleCoreCount**](ischedulernodecounters-idlecorecount.md)<br/>       | Read-only<br/> | Retrieves the number of cores on the node that are idle.<br/>                 |
| [**NumberOfCores**](ischedulernodecounters-numberofcores.md)<br/>       | Read-only<br/> | Retrieves the number of cores on the node.<br/>                               |
| [**NumberOfSockets**](ischedulernodecounters-numberofsockets.md)<br/>   | Read-only<br/> | Retrieves the number of sockets on the node.<br/>                             |
| [**OfflineCoreCount**](ischedulernodecounters-offlinecorecount.md)<br/> | Read-only<br/> | Retrieves the number of cores on the node that are offline.<br/>              |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




