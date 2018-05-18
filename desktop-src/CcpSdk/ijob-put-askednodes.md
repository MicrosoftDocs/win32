---
Description: 'Sets the list of nodes that are requested for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '77630f5a-bb9c-44f9-9cb4-5531ed35bcaf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_AskedNodes method'
---

# IJob::put\_AskedNodes method

Sets the list of nodes that are requested for the job.

## Syntax


```C++
HRESULT put_AskedNodes(
  [out] BSTR pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The comma-delimited list of node names. The nodes must exist in the cluster.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

This is the list of nodes that your job is capable of running on. For example, the nodes contain the required software for your job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_AskedNodes**](ijob-get-askednodes.md)
</dt> <dt>

[**ITask::put\_RequiredNodes**](itask-put-requirednodes.md)
</dt> </dl>

 

 




