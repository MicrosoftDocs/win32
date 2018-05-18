---
Description: 'Retrieves the cluster-wide environment variables. The variables are available to all tasks on all nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a7b2c52c-07b6-468b-9791-425324c95546'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::EnvironmentVariables property'
---

# IScheduler::EnvironmentVariables property

Retrieves the cluster-wide environment variables. The variables are available to all tasks on all nodes.

This property is read-only.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pEnvVariables
);
```



## Property value

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains a collection of environment variables defined for the cluster. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue2.md) interface.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To set a cluster-wide environment variable, call the [**IScheduler::SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md)
</dt> </dl>

 

 




