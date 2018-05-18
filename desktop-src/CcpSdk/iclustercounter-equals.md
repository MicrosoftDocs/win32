---
Description: 'Determines whether two instances of the ClusterCounter object are equal.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e8a216eb-54aa-45eb-b172-fcad049fe7ae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::Equals method'
---

# IClusterCounter::Equals method

Determines whether two instances of the ClusterCounter object are equal.

## Syntax


```C++
HRESULT Equals(
  [in]  IClusterCounter *counter,
  [out] VARIANT_BOOL    *pRetVal
);
```



## Parameters

<dl> <dt>

*counter* \[in\]
</dt> <dd>

An instance of the ClusterCounter object that you want to compare with this instance.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if the specified instance is the same as this instance; otherwise, VARIANT\_FALSE.

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

 

 




