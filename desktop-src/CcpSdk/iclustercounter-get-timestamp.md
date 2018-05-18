---
Description: 'Do not call this method. The time stamp is an opaque object that is used internally by the compute cluster server.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8152d6c-e464-4d74-9cda-1ff1f201a306'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_Timestamp method'
---

# IClusterCounter::get\_Timestamp method

Do not call this method. The time stamp is an opaque object that is used internally by the compute cluster server.

## Syntax


```C++
HRESULT get_Timestamp(
  [out] SAFEARRAY **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

Reserved.

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

 

 




