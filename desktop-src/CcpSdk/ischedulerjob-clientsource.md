---
Description: 'Retrieves or sets the name of the process that created the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd901551e-7f04-4f01-8d1a-32d216d8ad7a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ClientSource property'
---

# ISchedulerJob::ClientSource property

Retrieves or sets the name of the process that created the job.

This property is read/write.

## Syntax


```C++
HRESULT put_ClientSource(
  [in]  BSTR pSource
);

HRESULT get_ClientSource(
  [out] BSTR *pSource
);
```



## Property value

The client process that created the job.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 Client Utilities, HPC Pack 2008 R2 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




