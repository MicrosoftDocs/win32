---
Description: 'Retrieves an enumerator used to enumerate the tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7c54e834-1a59-4b7e-bc44-940efe368a1c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::GetEnumerator method'
---

# IJob::GetEnumerator method

Retrieves an enumerator used to enumerate the tasks in the job.

## Syntax


```C++
HRESULT GetEnumerator(
  [out] IEnumVARIANT **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the tasks in the job. The items of the enumeration are variants whose type is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**ITask**](itask.md) interface.

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

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::GetTask**](ijob-gettask.md)
</dt> </dl>

 

 




