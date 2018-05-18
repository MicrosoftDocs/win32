---
Description: 'Retrieves the environment variables that were set for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b7ab0722-9a88-433a-8f4c-464ac841f4d5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_EnvironmentVariables method'
---

# ITask::get\_EnvironmentVariables method

Retrieves the environment variables that were set for the task.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains the environment variables that were set using the [**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md) method. To retrieve the list, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection-getenumerator.md) method. The variant type for each item in the collection is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue.md) interface. The collection is empty if no variables have been set.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::get\_EnvironmentVariables**](icluster-get-environmentvariables.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md)
</dt> </dl>

 

 




