---
Description: 'Retrieves a list of job objects based on the specified filters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dd0f6b57-8d62-48fe-a2d0-8cc00d87ed4a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetJobList method'
---

# IScheduler::GetJobList method

Retrieves a list of job objects based on the specified filters.

## Syntax


```C++
HRESULT GetJobList(
  [in]  IFilterCollection    *filterProperties,
  [in]  ISortCollection      *sortProperties,
  [out] ISchedulerCollection **list
);
```



## Parameters

<dl> <dt>

*filterProperties* \[in\]
</dt> <dd>

An [**IFilterCollection**](ifiltercollection.md) interface that contains one or more filter properties used to filter the list of jobs. If **NULL**, the method returns all jobs.

</dd> <dt>

*sortProperties* \[in\]
</dt> <dd>

An [**ISortCollection**](isortcollection.md) interface that contains one or more sort properties used to sort the list of jobs. If **NULL**, the list is not sorted.

</dd> <dt>

*list* \[out\]
</dt> <dd>

An [**ISchedulerCollection**](ischedulercollection.md) interface that contains a collection of job objects. Each item in the collection is a variant of type VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**ISchedulerJob**](ischedulerjob.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If you specify more than one filter, a logical **AND** is applied to the filters (for example, return jobs that are running and have exclusive access to the nodes).

## Examples

For an example, see Getting a [Getting a List of Jobs](getting-a-list-of-jobs.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetJobIdList**](ischeduler-getjobidlist.md)
</dt> </dl>

 

 




