---
Description: 'Retrieves the job error message.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e0be6df4-85cf-4983-ad2e-52939bb2a869'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_ErrorMessage method'
---

# IJob::get\_ErrorMessage method

Retrieves the job error message.

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

The job error message.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The message contains the last message that has been set for the job. The message can be a run-time error message or the message passed to the [**ICluster::CancelJob**](icluster-canceljob.md) method.

Check the message if the job status is JobStatus\_Failed or JobStatus\_Cancelled.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::CancelJob**](icluster-canceljob.md)
</dt> <dt>

[**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md)
</dt> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**ITask::get\_ErrorMessage**](itask-get-errormessage.md)
</dt> </dl>

 

 




