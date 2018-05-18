---
Description: 'Sets an application-defined property on the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6cf09f68-b905-423f-afe6-fac05007666c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SetCustomProperty method'
---

# ISchedulerJob::SetCustomProperty method

Sets an application-defined property on the job.

## Syntax


```C++
HRESULT SetCustomProperty(
  [in] BSTR name,
  [in] BSTR value
);
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The property name. The name is limited to 80 Unicode characters.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The property value as a string. The name is limited to 1,024 Unicode characters.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Use this method to define your own properties that are passed to the submission and activation filters. If the property exists, the value of the property is updated. If *value* is null, the property is deleted.

To retrieve the application-defined properties, call the [**ISchedulerJob::GetCustomProperties**](ischedulerjob-getcustomproperties.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::GetCustomProperties**](ischedulerjob-getcustomproperties.md)
</dt> </dl>

 

 




