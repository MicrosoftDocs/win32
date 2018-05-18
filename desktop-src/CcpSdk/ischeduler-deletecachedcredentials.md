---
Description: 'Deletes the credentials that were cached for the specified user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c5fa8fc5-56cf-4714-995a-fd548d53e6bd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::DeleteCachedCredentials method'
---

# IScheduler::DeleteCachedCredentials method

Deletes the credentials that were cached for the specified user.

## Syntax


```C++
HRESULT DeleteCachedCredentials(
  [in] BSTR UserName
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*username*. The user name is limited to 80 Unicode characters. If this parameter is **NULL** or empty, the method deletes all credentials that have been cached by the calling user.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Only the user that cached the credentials can delete the credentials.

Note that the name that you provide must match the name used to submit the job or command. For example, if the user specified *domain*\\*username*, you must specify *domain*\\*username* when calling this method. If the user specified *username*, you must specify *username* when calling this method.

The method succeeds regardless of whether it finds the specified user in the cache.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IRemoteCommand::StartWithCredentials**](iremotecommand-startwithcredentials.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::SubmitJobById**](ischeduler-submitjob-2.md)
</dt> </dl>

 

 




