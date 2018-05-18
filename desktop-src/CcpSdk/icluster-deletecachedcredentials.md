---
Description: 'Deletes the credentials that were cached for the specified user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '26efade6-2509-4cec-afc8-e07f6e053bc3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::DeleteCachedCredentials method'
---

# ICluster::DeleteCachedCredentials method

Deletes the credentials that were cached for the specified user.

## Syntax


```C++
HRESULT DeleteCachedCredentials(
  [in] BSTR userName
);
```



## Parameters

<dl> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*. The user name is limited to 80 Unicode characters. If this parameter is **NULL** or empty, the method deletes all credentials that have been cached by the calling user.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Only the user that cached the credentials can delete the credentials.

To add credentials to the cache, use the [**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md) method.

The method does not return an error if the name is not found.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




