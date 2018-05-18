---
Description: 'Retrieves the name of the user who created, submitted, or queued the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '84f7f1ba-9b46-4b79-a923-75c90162a0b2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Owner property'
---

# ISchedulerJob::Owner property

Retrieves the name of the user who created, submitted, or queued the job.

This property is read-only.

## Syntax


```C++
HRESULT get_Owner(
  [out] BSTR *pOwner
);
```



## Property value

The user name.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




