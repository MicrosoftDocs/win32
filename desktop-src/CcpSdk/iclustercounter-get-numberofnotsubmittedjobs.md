---
Description: 'Retrieves the number of jobs that have not been submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '46171328-49df-4ff8-b961-df7ba7719562'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfNotSubmittedJobs method'
---

# IClusterCounter::get\_NumberOfNotSubmittedJobs method

Retrieves the number of jobs that have not been submitted.

## Syntax


```C++
HRESULT get_NumberOfNotSubmittedJobs(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of jobs that have been added to the cluster but have not been submitted to the scheduling queue (jobs with the status **JobStatus\_NotSubmitted**).

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

 

 




