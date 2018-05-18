---
Description: 'Sets the minimum number of processors required by the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7b5b338e-52af-44a2-9828-a41e67602986'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_MinimumNumberOfProcessors method'
---

# ITask::put\_MinimumNumberOfProcessors method

Sets the minimum number of processors required by the task.

## Syntax


```C++
HRESULT put_MinimumNumberOfProcessors(
  [in] long Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The minimum number of processors. The default is 1.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

This value cannot exceed the value for the [**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_MinimumNumberOfProcessors**](itask-get-minimumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MaximumNumberOfProcessors**](itask-put-maximumnumberofprocessors.md)
</dt> </dl>

 

 




