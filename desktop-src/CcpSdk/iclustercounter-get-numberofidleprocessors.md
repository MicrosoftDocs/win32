---
Description: 'Retrieves the number of idle processors in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4f75975d-7a31-4503-8e2b-b53ed4e0c9bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfIdleProcessors method'
---

# IClusterCounter::get\_NumberOfIdleProcessors method

Retrieves the number of idle processors in the cluster.

## Syntax


```C++
HRESULT get_NumberOfIdleProcessors(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of idle processors.

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

 

 




