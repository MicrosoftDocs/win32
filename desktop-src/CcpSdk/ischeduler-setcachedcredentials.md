---
Description: 'Sets the credentials for the specified user in the credential cache, so that the job scheduler can use the credentials for submitting jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cf424ec9-b7e1-441f-97d6-08d6ee71b688'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetCachedCredentials method'
---

# IScheduler::SetCachedCredentials method

Sets the credentials for the specified user in the credential cache, so that the job scheduler can use the credentials for submitting jobs.

## Syntax


```C++
HRESULT SetCachedCredentials(
  [in] BSTR UserName,
  [in] BSTR password
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The user name of the user for which you want the set the cached credentials, in the form *domain*\\*user*. The user name is limited to 80 characters.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password for the user for which you want the set the cached credentials.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 SP1 Client Utilities<br/>                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::DeleteCachedCredentials**](ischeduler-deletecachedcredentials.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::SubmitJobById**](ischeduler-submitjob-2.md)
</dt> <dt>

[**IRemoteCommand::StartWithCredentials**](iremotecommand-startwithcredentials.md)
</dt> </dl>

 

 




