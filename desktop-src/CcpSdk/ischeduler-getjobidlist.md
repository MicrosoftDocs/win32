---
Description: 'Retrieves a list of job identifiers based on the specified filters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'de719264-48ef-45f9-afeb-4b57cc080819'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetJobIdList method'
---

# IScheduler::GetJobIdList method

Retrieves a list of job identifiers based on the specified filters.

## Syntax


```C++
HRESULT GetJobIdList(
  [in]  IFilterCollection *filterProperties,
  [in]  ISortCollection   *sortProperties,
  [out] IIntCollection    **jobIds
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

*jobIds* \[out\]
</dt> <dd>

An [**IIntCollection**](iintcollection.md) interface that contains one or more job identifiers that match the specified filter criteria.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If you specify more than one filter, a logical **AND** is applied to the filters (for example, return jobs that are running and have exclusive access to the nodes).

If you use the enumerator to enumerate each item in the *jobIds* collection, the item is a VARIANT of type VT\_I4. Query the **lVal** member for the job identifier.

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

[**IScheduler::GetJobList**](ischeduler-getjoblist.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




