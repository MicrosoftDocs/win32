---
Description: 'Sets the email credentials by using the specified username and password.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '70792661-523B-499C-8401-25E1256AB653'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetEmailCredentials method'
---

# IScheduler::SetEmailCredentials method

Sets the email credentials by using the specified username and password.

## Syntax


```C++
HRESULT SetEmailCredentials(
  [in] BSTR *userName,
  [in] BSTR *password
);
```



## Parameters

<dl> <dt>

*userName* \[in\]
</dt> <dd>

The user name.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password.

</dd> </dl>

## Return value

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Email credentials use the username and password of the email account as credentials for submitting jobs. To delete the email credentials, use the [**IScheduler::DeleteEmailCredentials**](ischeduler-deleteemailcredentials.md) method.

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Microsoft HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



 

 




