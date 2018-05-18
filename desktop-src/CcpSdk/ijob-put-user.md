---
Description: 'Sets the RunAs user for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e7f3cf3a-75cd-4c75-966e-774eb6093d8d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_User method'
---

# IJob::put\_User method

Sets the RunAs user for the job.

## Syntax


```C++
HRESULT put_User(
  [in] BSTR pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[in\]
</dt> <dd>

The name of the user, in the form *domain*\\*user*.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

You do not need to call this method. The initial value is set to the user that added the job to the cluster. You can use the following methods to change the value of the RunAs user:

-   [**ICluster::QueueJob**](icluster-queuejob.md)
-   [**ICluster::SubmitJob**](icluster-submitjob.md)
-   [**ICluster::SetJobCredentials**](icluster-setjobcredentials.md)
-   [**ICluster::SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md)

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_User**](ijob-get-user.md)
</dt> </dl>

 

 




