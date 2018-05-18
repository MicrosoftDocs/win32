---
Description: 'Implement this interface if you want to receive event notification when the state of the job changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cf7d1f99-d53c-417c-9db4-c7c86f0e271e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerJobEvents interface
---

# ISchedulerJobEvents interface

Implement this interface if you want to receive event notification when the state of the job changes.

## Members

The **ISchedulerJobEvents** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerJobEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISchedulerJobEvents** interface has these methods.



| Method                                                 | Description                                                       |
|:-------------------------------------------------------|:------------------------------------------------------------------|
| [**OnJobState**](ischedulerjobevents-onjobstate.md)   | Is called when the state of the job changes.<br/>           |
| [**OnTaskState**](ischedulerjobevents-ontaskstate.md) | Is called when the state of a task in the job changes.<br/> |



 

## Remarks

You must implement all methods in this interface. You will receive notification for each event—you cannot specify the types of events you want to receive.

## Examples

For an example, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




