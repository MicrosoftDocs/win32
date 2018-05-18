---
Description: 'Retrieves the number of processors in the cluster that are not reachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '57c5870f-299d-4d96-a6d2-2a5ca71a3993'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfUnreachableProcessors method'
---

# IClusterCounter::get\_NumberOfUnreachableProcessors method

Retrieves the number of processors in the cluster that are not reachable.

## Syntax


```C++
HRESULT get_NumberOfUnreachableProcessors(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of processors in the cluster that are not reachable.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

A processor can be unreachable if the node to which it belongs is offline or there is a network connection problem.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




