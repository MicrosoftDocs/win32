---
Description: 'Retrieves counter values related to the status of tasks in the job (for example, the number of tasks that have finished).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7d89c45a-1da8-4a6d-b1fd-d8b7ccf8ed2c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IJobCounter interface
---

# IJobCounter interface

Retrieves counter values related to the status of tasks in the job (for example, the number of tasks that have finished).

To get this interface, call the [**ICluster::GetJobCounter**](icluster-getjobcounter.md) method.

## Members

The **IJobCounter** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IJobCounter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IJobCounter** interface has these methods.



| Method                                                                              | Description                                                            |
|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**get\_NumberOfCancelledTasks**](ijobcounter-get-numberofcancelledtasks.md)       | Retrieves the number of canceled tasks.<br/>                     |
| [**get\_NumberOfFailedTasks**](ijobcounter-get-numberoffailedtasks.md)             | Retrieves the number of failed tasks.<br/>                       |
| [**get\_NumberOfFinishedTasks**](ijobcounter-get-numberoffinishedtasks.md)         | Retrieves the number of finished tasks.<br/>                     |
| [**get\_NumberOfNotSubmittedTasks**](ijobcounter-get-numberofnotsubmittedtasks.md) | Retrieves the number of tasks that have not been submitted.<br/> |
| [**get\_NumberOfQueuedTasks**](ijobcounter-get-numberofqueuedtasks.md)             | Retrieves the number of queued tasks.<br/>                       |
| [**get\_NumberOfRunningTasks**](ijobcounter-get-numberofruntasks.md)               | Retrieves the number of running tasks.<br/>                      |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::get\_ClusterCounter**](icluster-get-clustercounter.md)
</dt> <dt>

[Jobs and Tasks](jobs-and-tasks.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




