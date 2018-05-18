---
Description: 'Contains counter values related to the scheduling queue and cluster nodes (for example, the number of queued jobs and the number of idle nodes).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '311476ba-f2a0-40ff-9915-d57cb73b3dc8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IClusterCounter interface
---

# IClusterCounter interface

Contains counter values related to the scheduling queue and cluster nodes (for example, the number of queued jobs and the number of idle nodes).

To get this interface, call the [**ICluster::get\_ClusterCounter**](icluster-get-clustercounter.md) method.

## Members

The **IClusterCounter** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IClusterCounter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IClusterCounter** interface has these methods.



| Method                                                                                          | Description                                                                                                                   |
|:------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**Equals**](iclustercounter-equals.md)                                                        | Determines whether two instances of the ClusterCounter object are equal.<br/>                                           |
| [**get\_NumberOfBusyProcessors**](iclustercounter-get-numberofbusyprocessors.md)               | Retrieves the number of busy processors in the cluster.<br/>                                                            |
| [**get\_NumberOfCancelledJobs**](iclustercounter-get-numberofcancelledjobs.md)                 | Retrieves the number of canceled jobs.<br/>                                                                             |
| [**get\_NumberOfCancelledTasks**](iclustercounter-get-numberofcancelledtasks.md)               | Retrieves the number of canceled tasks.<br/>                                                                            |
| [**get\_NumberOfFailedJobs**](iclustercounter-get-numberoffailedjobs.md)                       | Retrieves the number of failed jobs.<br/>                                                                               |
| [**get\_NumberOfFailedTasks**](iclustercounter-get-numberoffailedtasks.md)                     | Retrieves the number of failed tasks.<br/>                                                                              |
| [**get\_NumberOfFinishedJobs**](iclustercounter-get-numberoffinishedjobs.md)                   | Retrieves the number of finished jobs.<br/>                                                                             |
| [**get\_NumberOfFinishedTasks**](iclustercounter-get-numberoffinishedtasks.md)                 | Retrieves the number of finished tasks.<br/>                                                                            |
| [**get\_NumberOfIdleNodes**](iclustercounter-get-numberofidlenodes.md)                         | Retrieves the number of idle nodes in the cluster.<br/>                                                                 |
| [**get\_NumberOfIdleProcessors**](iclustercounter-get-numberofidleprocessors.md)               | Retrieves the number of idle processors in the cluster.<br/>                                                            |
| [**get\_NumberOfNotSubmittedJobs**](iclustercounter-get-numberofnotsubmittedjobs.md)           | Retrieves the number of jobs that have not been submitted.<br/>                                                         |
| [**get\_NumberOfNotSubmittedTasks**](iclustercounter-get-numberofnotsubmittedtasks.md)         | Retrieves the number of tasks that have not been submitted.<br/>                                                        |
| [**get\_NumberOfPausedNodes**](iclustercounter-get-numberofpausednodes.md)                     | Retrieves the number of paused nodes in the cluster.<br/>                                                               |
| [**get\_NumberOfPendingNodes**](iclustercounter-get-numberofpendingnodes.md)                   | Retrieves the number of pending nodes in the cluster.<br/>                                                              |
| [**get\_NumberOfPendingProcessors**](iclustercounter-get-numberofpendingprocessors.md)         | Retrieves the number of pending processors in the cluster.<br/>                                                         |
| [**get\_NumberOfQueuedJobs**](iclustercounter-get-numberofqueuedjobs.md)                       | Retrieves the number of queued jobs.<br/>                                                                               |
| [**get\_NumberOfQueuedTasks**](iclustercounter-get-numberofqueuedtasks.md)                     | Retrieves the number of queued tasks.<br/>                                                                              |
| [**get\_NumberOfReadyNodes**](iclustercounter-get-numberofreadynodes.md)                       | Retrieves the number of ready nodes in the cluster.<br/>                                                                |
| [**get\_NumberOfRunningJobs**](iclustercounter-get-numberofrunningjobs.md)                     | Retrieves the number of running jobs.<br/>                                                                              |
| [**get\_NumberOfRunningTasks**](iclustercounter-get-numberofrunningtasks.md)                   | Retrieves the number of running tasks.<br/>                                                                             |
| [**get\_NumberOfUnreachableNodes**](iclustercounter-get-numberofunreachablenodes.md)           | Retrieves the number of nodes in the cluster that are not reachable.<br/>                                               |
| [**get\_NumberOfUnreachableProcessors**](iclustercounter-get-numberofunreachableprocessors.md) | Retrieves the number of processors in the cluster that are not reachable.<br/>                                          |
| [**get\_Timestamp**](iclustercounter-get-timestamp.md)                                         | Do not call this method. The time stamp is an opaque object that is used internally by the compute cluster server.<br/> |
| [**get\_TotalNumberOfJobs**](iclustercounter-get-totalnumberofjobs.md)                         | Retrieves the number of jobs in the cluster.<br/>                                                                       |
| [**get\_TotalNumberOfNodes**](iclustercounter-get-totalnumberofnodes.md)                       | Retrieves the number of nodes in the cluster.<br/>                                                                      |
| [**get\_TotalNumberOfProcessors**](iclustercounter-get-totalnumberofprocessors.md)             | Retrieves the number of processors in the cluster.<br/>                                                                 |
| [**get\_TotalNumberOfTasks**](iclustercounter-get-totalnumberoftasks.md)                       | Retrieves the number of tasks in the cluster.<br/>                                                                      |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




