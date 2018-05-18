---
Description: 'Sets the minimum number of processors that are required by the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f49559c3-ecc3-43a0-b38c-9605f2174cfc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_MinimumNumberOfProcessors method'
---

# IJob::put\_MinimumNumberOfProcessors method

Sets the minimum number of processors that are required by the job.

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

The value must be less than or equal to:

-   The number of processors in the cluster or the number of processors on the nodes that you requested (with the [**IJob::put\_AskedNodes**](ijob-put-askednodes.md) method).
-   The value of the [**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_MinimumNumberOfProcessors**](ijob-get-minimumnumberofprocessors.md)
</dt> <dt>

[**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md)
</dt> </dl>

 

 




