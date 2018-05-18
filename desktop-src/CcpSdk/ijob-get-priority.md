---
Description: 'Retrieves the job priority.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5d1263a4-cf4d-4056-ad75-9e9de69131f2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_Priority method'
---

# IJob::get\_Priority method

Retrieves the job priority.

## Syntax


```C++
HRESULT get_Priority(
  [out] JobPriority *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The job priority. For a list of values, see [**JobPriority**](jobpriority.md).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To set the job priority, call the [**IJob::put\_Priority**](ijob-put-priority.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::put\_Priority**](ijob-put-priority.md)
</dt> </dl>

 

 




