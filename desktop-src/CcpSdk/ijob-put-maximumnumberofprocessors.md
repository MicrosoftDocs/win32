---
Description: 'Sets the maximum number of processors that are required by the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c1333c60-32f9-4338-98ce-0369912947a3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_MaximumNumberOfProcessors method'
---

# IJob::put\_MaximumNumberOfProcessors method

Sets the maximum number of processors that are required by the job.

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

The value cannot be less than the value of the [**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_MaximumNumberOfProcessors**](ijob-get-maximumnumberofprocessors.md)
</dt> <dt>

[**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MaximumNumberOfProcessors**](itask-put-maximumnumberofprocessors.md)
</dt> </dl>

 

 




