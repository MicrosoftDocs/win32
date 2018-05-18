---
Description: 'Retrieves or sets the preference given to the order in which the job is scheduled on nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9405346a-1e43-4910-b3b9-55d969c2cdce'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::OrderBy property'
---

# ISchedulerJob::OrderBy property

Retrieves or sets the preference given to the order in which the job is scheduled on nodes.

This property is read/write.

## Syntax


```C++
HRESULT put_OrderBy(
  [in]  BSTR OrderBy
);

HRESULT get_OrderBy(
  [out] BSTR *pOrderBy
);
```



## Property value

A comma-delimited string that contains the preference given to the order in which the job is scheduled on nodes.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The string can contain a maximum of two delimited items. The items must be distinct. The format for each item is "(–)?(Cores\|Memory)\[, (–)?(Cores\|Memory)\]". Use the negative sign (–) before Cores or Memory to specify that the scheduler sort the nodes (based on cores or memory) in ascending order. If the negative sign is not specified, the scheduler sorts the nodes in descending order. If you do not set this property, the scheduler uses the preference, "Cores, Memory" (which means to schedule the job on nodes with the most number of cores and memory first before scheduling on nodes with less resources).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




