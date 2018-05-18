---
Description: 'Contains information about a compute node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a1bf4155-534e-4014-90ce-6a8cb9bfb1a5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerNode interface
---

# ISchedulerNode interface

Contains information about a compute node.

To get this interface, call one of the following methods:

-   [**IScheduler::OpenNode**](ischeduler-opennode.md)
-   [**IScheduler::OpenNodeByName**](ischeduler-opennode-2.md)

## Members

The **ISchedulerNode** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerNode** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISchedulerNode** interface has these methods.



| Method                                            | Description                                                                          |
|:--------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**GetCores**](ischedulernode-getcores.md)       | Retrieves the state information for each core on the node.<br/>                |
| [**GetCounters**](ischedulernode-getcounters.md) | Retrieves the counter data for the node.<br/>                                  |
| [**Refresh**](ischedulernode-refresh.md)         | Refreshes this copy of the node object with the contents from the server.<br/> |



 

### Properties

The **ISchedulerNode** interface has these properties.



| Property                                                             | Access type          | Description                                                                                          |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------|
| [**CpuSpeed**](ischedulernode-cpuspeed.md)<br/>               | Read-only<br/> | Retrieves the processor speed of the node.<br/>                                                |
| [**Guid**](ischedulernode-guid.md)<br/>                       | Read-only<br/> | Retrieves the globally unique identifier that uniquely identifies the node in the system.<br/> |
| [**Id**](ischedulernode-id.md)<br/>                           | Read-only<br/> | Retrieves the identifier that uniquely identifies the node in the cluster.<br/>                |
| [**JobType**](ischedulernode-jobtype.md)<br/>                 | Read-only<br/> | Retrieves the types of jobs that this node is configured to run.<br/>                          |
| [**MemorySize**](ischedulernode-memorysize.md)<br/>           | Read-only<br/> | Retrieves the size of memory.<br/>                                                             |
| [**MoveToOffline**](ischedulernode-movetooffline.md)<br/>     | Read-only<br/> | Determines if a user requested that the node go offline.<br/>                                  |
| [**Name**](ischedulernode-name.md)<br/>                       | Read-only<br/> | Retrieves the computer name of the node.<br/>                                                  |
| [**NodeGroups**](ischedulernode-nodegroups.md)<br/>           | Read-only<br/> | Retrieves the node groups to which this node belongs.<br/>                                     |
| [**NumberOfCores**](ischedulernode-numberofcores.md)<br/>     | Read-only<br/> | Retrieves the number of cores on the node.<br/>                                                |
| [**NumberOfSockets**](ischedulernode-numberofsockets.md)<br/> | Read-only<br/> | Retrieves the number of sockets on the node.<br/>                                              |
| [**OfflineTime**](ischedulernode-offlinetime.md)<br/>         | Read-only<br/> | Retrieves the date and time that the node last went offline.<br/>                              |
| [**OnlineTime**](ischedulernode-onlinetime.md)<br/>           | Read-only<br/> | Retrieves the date and time that the node last came online.<br/>                               |
| [**Reachable**](ischedulernode-reachable.md)<br/>             | Read-only<br/> | Determines whether the server thinks the node is reachable.<br/>                               |
| [**State**](ischedulernode-state.md)<br/>                     | Read-only<br/> | Retrieves the current state of the node.<br/>                                                  |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**ISchedulerCore**](ischedulercore.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerNodeCounters**](ischedulernodecounters.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




