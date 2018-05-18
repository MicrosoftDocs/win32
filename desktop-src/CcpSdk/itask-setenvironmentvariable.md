---
Description: 'Sets the task-specific environment variable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '04bcb160-5e8b-4364-b80b-b90a84f7ee9c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::SetEnvironmentVariable method'
---

# ITask::SetEnvironmentVariable method

Sets the task-specific environment variable.

## Syntax


```C++
HRESULT SetEnvironmentVariable(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the environment variable.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value of the environment variable.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The length of all environment variables specified for the task is limited to 2,048 Unicode characters.

To set cluster-wide environment variables, call the [**ICluster::SetEnvironmentVariable**](icluster-setenvironmentvariable.md) method.

The environment variables that are made available to the task include variables set using this method, those set using the [**SetEnvironmentVariable**](icluster-setenvironmentvariable.md) method, and the cluster-wide environment variables that are defined in the "Use Environment Variables" section of the [Compute Cluster Server User Operations](http://go.microsoft.com/fwlink/p/?linkid=64128).

To retrieve this variable from inside your task, call the Win32 function [**GetEnvironmentVariable**](https://msdn.microsoft.com/library/windows/desktop/ms683188).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::SetEnvironmentVariable**](icluster-setenvironmentvariable.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_EnvironmentVariables**](itask-get-environmentvariables.md)
</dt> </dl>

 

 




