---
Description: 'Determines whether the user is a member of the cluster's Administrators group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b1560ea5-d851-4588-b8aa-164508b37cce'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::IsAdmin method'
---

# ICluster::IsAdmin method

Determines whether the user is a member of the cluster's Administrators group.

## Syntax


```C++
HRESULT IsAdmin(
  [out] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if the user is a member of the Administrators group on the head node; otherwise, VARIANT\_FALSE.

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
</dt> </dl>

 

 




