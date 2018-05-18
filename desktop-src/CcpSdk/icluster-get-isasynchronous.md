---
Description: 'Determines whether calls to the server are executed asynchronously.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e6504c21-b3db-4da1-bfbc-3399169d6af5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_IsAsynchronous method'
---

# ICluster::get\_IsAsynchronous method

Determines whether calls to the server are executed asynchronously.

## Syntax


```C++
HRESULT get_IsAsynchronous(
  [out] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if calls to the cluster are executed asynchronously. The value is VARIANT\_FALSE if the calls are executed synchronously.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

By default, calls to the cluster are executed synchronously. The default behavior is the best choice for most applications. To execute calls asynchronously, call the [**ICluster::put\_IsAsynchronous**](icluster-put-isasynchronous.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




