---
Description: 'Retrieves or sets the RunAs user for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '81470c34-24cd-4b78-9ef5-97ff0ead174c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::UserName property'
---

# ISchedulerJob::UserName property

Retrieves or sets the RunAs user for the job.

This property is read/write.

## Syntax


```C++
HRESULT put_UserName(
  [in]  BSTR name
);

HRESULT get_UserName(
  [out] BSTR *pName
);
```



## Property value

The user name in the form, *domain*\\*username*.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

You do not need to set this property. The RunAs user defaults to the owner of the job if you do not set this property or specify the RunAs user when calling the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




