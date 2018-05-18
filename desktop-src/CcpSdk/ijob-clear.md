---
Description: 'Removes all tasks from the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '35ae0133-1d1a-4f24-a4a7-d20dd88ec792'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::Clear method'
---

# IJob::Clear method

Removes all tasks from the job.

## Syntax


```C++
HRESULT Clear();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this method to remove tasks from a job that has not been [added](icluster-addjob.md) to the cluster. After the job is added to the cluster, you cannot remove tasks from the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> </dl>

 

 




