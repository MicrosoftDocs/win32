---
Description: 'Retrieves the task error message.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5c22844f-358a-477f-9088-698eee01e7d9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_ErrorMessage method'
---

# ITask::get\_ErrorMessage method

Retrieves the task error message.

## Syntax


```C++
HRESULT get_ErrorMessage(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The task error message.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The message contains the last message that was set for the task. The message can be a run-time error message or the message passed to the [**ICluster::CancelTask**](icluster-canceltask.md) method.

Check the message if the task status is TaskStatus\_Failed or TaskStatus\_Cancelled.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::CancelTask**](icluster-canceltask.md)
</dt> <dt>

[**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md)
</dt> <dt>

[**IJob::get\_ErrorMessage**](ijob-get-errormessage.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> </dl>

 

 




