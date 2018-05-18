---
Description: 'Sets the RunAs credentials for the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f0b80e77-1461-4f7b-84cd-c4502ce40b90'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::SetJobCredentials method'
---

# ICluster::SetJobCredentials method

Sets the RunAs credentials for the specified job.

## Syntax


```C++
HRESULT SetJobCredentials(
  [in] long jobId,
  [in] BSTR userName,
  [in] BSTR password
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*. The user name is limited to 80 Unicode characters.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The user password. The password is limited to 127 Unicode characters. Can be empty.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

You would call this method after submitting a job to change the credentials that the job uses.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md)
</dt> <dt>

[**ICluster::SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md)
</dt> </dl>

 

 




