---
Description: 'Represents the resource usage of a job or task. The resource information is available only after the job or task has started.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cd25e65b-b463-484a-a471-b617951c743f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IResourceUsage interface
---

# IResourceUsage interface

Represents the resource usage of a job or task. The resource information is available only after the job or task has started.

The following methods return this interface:

-   [**ICluster::GetJobResourceUsage**](icluster-getjobresourceusage.md)
-   [**ICluster::GetTaskResourceUsage**](icluster-gettaskresourceusage.md)

## Members

The **IResourceUsage** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IResourceUsage** also has these types of members:

-   [Methods](#methods)

### Methods

The **IResourceUsage** interface has these methods.



| Method                                                                     | Description                                                                                           |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**get\_AllocatedNodes**](iresourceusage-get-allocatednodes.md)           | Retrieves the list of nodes that are allocated to the job or task.<br/>                         |
| [**get\_KernelProcessorTime**](iresourceusage-get-kernelprocessortime.md) | Retrieves the kernel-mode processor time that is used by the job or task, in milliseconds.<br/> |
| [**get\_NumberOfProcesses**](iresourceusage-get-numberofprocesses.md)     | Retrieves the number of processes being used by the job or task.<br/>                           |
| [**get\_Processes**](iresourceusage-get-processes.md)                     | Retrieves the list of processes being used by the job or task.<br/>                             |
| [**get\_UserProcessorTime**](iresourceusage-get-userprocessortime.md)     | Retrieves the user-mode processor time that is used by the job or task, in milliseconds.<br/>   |
| [**get\_WorkingSet**](iresourceusage-get-workingset.md)                   | Retrieves the size of the process working set, in bytes.<br/>                                   |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




