---
Description: 'Retrieves the cluster's configuration parameters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3278ca0d-664b-4f3c-b841-c11866857d73'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_Parameters method'
---

# ICluster::get\_Parameters method

Retrieves the cluster's configuration parameters.

## Syntax


```C++
HRESULT get_Parameters(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains a collection of configuration parameters for the cluster. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

To set the configuration parameters, call the [**ICluster::SetClusterParameter**](icluster-setclusterparameter.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




