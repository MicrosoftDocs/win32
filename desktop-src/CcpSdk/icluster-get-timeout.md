---
Description: 'Retrieves the maximum time that the application will wait for a response from the cluster when making synchronous calls.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7c74077a-631c-4f57-b462-35c2bb45ca6d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_Timeout method'
---

# ICluster::get\_Timeout method

Retrieves the maximum time that the application will wait for a response from the cluster when making synchronous calls.

## Syntax


```C++
HRESULT get_Timeout(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time to wait, in milliseconds. The value can be 0 or –1 (infinite) if there is no time-out limit.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::put\_Timeout**](icluster-put-timeout.md)
</dt> </dl>

 

 




