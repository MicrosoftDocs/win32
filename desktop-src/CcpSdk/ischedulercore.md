---
Description: 'Provides information about a core on a node such as its state and the task currently running on it.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1e8355cf-40ca-4ccb-8a0a-f2d57e2de086'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerCore interface
---

# ISchedulerCore interface

Provides information about a core on a node such as its state and the task currently running on it.

To get this interface, call the [**ISchedulerNode::GetCores**](ischedulernode-getcores.md) method.

## Members

The **ISchedulerCore** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerCore** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISchedulerCore** interface has these properties.



| Property                                           | Access type          | Description                                                            |
|:---------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**Id**](ischedulercore-id.md)<br/>         | Read-only<br/> | Retrieves the identifier that uniquely identifies the core.<br/> |
| [**JobId**](ischedulercore-jobid.md)<br/>   | Read-only<br/> | Retrieves the identifier of the job running on the core.<br/>    |
| [**State**](ischedulercore-state.md)<br/>   | Read-only<br/> | Retrieves the state of the core.<br/>                            |
| [**TaskId**](ischedulercore-taskid.md)<br/> | Read-only<br/> | Retrieves the identifier of the task running on the core.<br/>   |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> </dl>

 

 




