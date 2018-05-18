---
Description: 'Refreshes this copy of the job with the contents from the server.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'acd940bc-9b6a-4ead-9593-dc6d6bfba7bd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Refresh method'
---

# ISchedulerJob::Refresh method

Refreshes this copy of the job with the contents from the server.

## Syntax


```C++
HRESULT Refresh();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::Commit**](ischedulerjob-commit.md)
</dt> </dl>

 

 




