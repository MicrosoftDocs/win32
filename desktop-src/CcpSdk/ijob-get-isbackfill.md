---
Description: 'Checks whether the job is running as a backfill job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ab0b68c0-8b39-4e29-97e1-9ba91f2fc247'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_IsBackfill method'
---

# IJob::get\_IsBackfill method

Checks whether the job is running as a backfill job.

## Syntax


```C++
HRESULT get_IsBackfill(
  [out] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if the job is running as a backfill job; otherwise, VARIANT\_FALSE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

A backfill job is a lower priority job that runs before a higher priority job. This ensures that a resource-intensive application will not delay other applications that are ready to run. The job scheduler will schedule a lower priority job if a higher priority job is waiting for resources to become available and the lower priority job can finish with the available resources without delaying the start time of the higher priority job.

For more information, see the BackfillLookahead configuration parameter in the Remarks section of [**ICluster::SetClusterParameter**](icluster-setclusterparameter.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> </dl>

 

 




