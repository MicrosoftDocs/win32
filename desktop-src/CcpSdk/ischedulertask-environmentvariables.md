---
Description: 'Retrieves the environment variables that were set for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a28ae3e6-bac4-4f05-a227-64bdffc45d98'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::EnvironmentVariables property'
---

# ISchedulerTask::EnvironmentVariables property

Retrieves the environment variables that were set for the task.

This property is read-only.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pEnvVariables
);
```



## Property value

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains the collection of variables. Each item in the collection is an [**INameValue**](inamevalue2.md) interface that contains the variable name and value. To retrieve the list of **INameValue** interfaces, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection2-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **INameValue** interface. The collection is empty if no variables have been set.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler.EnvironmentVariables**](ischeduler-environmentvariables.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask::SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md)
</dt> </dl>

 

 




