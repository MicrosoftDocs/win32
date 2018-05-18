---
Description: 'Retrieves a list of task identifiers based on the specified filters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '08b9793d-dd16-475b-a45d-1cab8ac7a1d5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::GetTaskIdList method'
---

# ISchedulerJob::GetTaskIdList method

Retrieves a list of task identifiers based on the specified filters.

## Syntax


```C++
HRESULT GetTaskIdList(
  [in]  IFilterCollection    *filterProperties,
  [in]  ISortCollection      *sortProperties,
  [in]  VARIANT_BOOL         expandParametric,
  [out] ISchedulerCollection **taskIds
);
```



## Parameters

<dl> <dt>

*filterProperties* \[in\]
</dt> <dd>

An [**IFilterCollection**](ifiltercollection.md) interface that contains one or more filter properties used to filter the list of tasks. If **NULL**, the method returns all tasks.

</dd> <dt>

*sortProperties* \[in\]
</dt> <dd>

An [**ISortCollection**](isortcollection.md) interface that contains one or more sort properties used to sort the list of tasks. If **NULL**, the list is not sorted.

</dd> <dt>

*expandParametric* \[in\]
</dt> <dd>

Set to VARIANT\_TRUE to include parametric instances in the results; otherwise, VARIANT\_FALSE.

</dd> <dt>

*taskIds* \[out\]
</dt> <dd>

An [**ISchedulerCollection**](ischedulercollection.md) interface that contains one or more task identifiers that match the specified filter criteria. Each item in the collection is a VARIANT of type VT\_DISPATCH. Query the **pdispVal** member for the [**ITaskId**](itaskid.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

If you specify more than one filter, a logical **AND** is applied to the filters (for example, return tasks that are running and have exclusive access to the nodes).

Only the job owner or administrator can list the tasks in a job. The job must have been added to the scheduler before calling this method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::GetTaskList**](ischedulerjob-gettasklist.md)
</dt> <dt>

[**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md)
</dt> </dl>

 

 




