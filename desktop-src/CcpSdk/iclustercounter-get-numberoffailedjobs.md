---
Description: 'Retrieves the number of failed jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'afe601fb-3fe8-47e2-a31b-de30e8f3308e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfFailedJobs method'
---

# IClusterCounter::get\_NumberOfFailedJobs method

Retrieves the number of failed jobs.

## Syntax


```C++
HRESULT get_NumberOfFailedJobs(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of failed jobs (jobs with the status **JobStatus\_Failed**).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




