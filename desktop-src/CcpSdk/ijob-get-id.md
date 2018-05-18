---
Description: 'Retrieves the job identifier.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '198ad69f-d858-4cb0-830b-b5c74bbc525a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_Id method'
---

# IJob::get\_Id method

Retrieves the job identifier.

## Syntax


```C++
HRESULT get_Id(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The job identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The identifier is generated when you call the [**ICluster::AddJob**](icluster-addjob.md) or [**ICluster::QueueJob**](icluster-queuejob.md) method to add the job to the cluster.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> </dl>

 

 




