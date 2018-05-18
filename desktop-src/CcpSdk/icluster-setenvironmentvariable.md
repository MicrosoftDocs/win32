---
Description: 'Sets a cluster-wide environment variable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5b726a02-4bf6-4deb-8e48-9f8c19064df8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::SetEnvironmentVariable method'
---

# ICluster::SetEnvironmentVariable method

Sets a cluster-wide environment variable.

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

The value of the environment variable. If **NULL** or an empty string, the variable is deleted.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The sum of all environment variables is limited to 2,048 Unicode characters.

You can use this method to add, delete, or update an environment variable. However, you cannot delete or update the value of a CCP defined environment variables, such as CCP\_CLUSTER\_NAME. If you try to update the value of a CCP variable, you will get a duplicate entry.

To retrieve the cluster-wide environment variables, call the [**ICluster::get\_EnvironmentVariables**](icluster-get-environmentvariables.md) method.

To set task-specific environment variables, call the [**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md) method.

To retrieve the variable from within a task, call the Win32 function [**GetEnvironmentVariable**](https://msdn.microsoft.com/library/windows/desktop/ms683188).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::get\_EnvironmentVariables**](icluster-get-environmentvariables.md)
</dt> <dt>

[**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md)
</dt> </dl>

 

 




