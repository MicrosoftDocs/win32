---
Description: 'Sets the maximum number of processors required by the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4a4f884c-4789-4b93-8dd5-0ca28966eead'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_MaximumNumberOfProcessors method'
---

# ITask::put\_MaximumNumberOfProcessors method

Sets the maximum number of processors required by the task.

## Syntax


```C++
HRESULT put_MaximumNumberOfProcessors(
  [in] long Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The maximum number of processors. The default is 1.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

This value cannot:

-   Exceed the value for the [**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md) method.
-   Be less than the [**ITask::put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_MaximumNumberOfProcessors**](itask-get-maximumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md)
</dt> </dl>

 

 




