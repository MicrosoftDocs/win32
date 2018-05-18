---
Description: 'Gets or sets the name of the SOA service that the service tasks in the job use, if the job contains service tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ADFAA6E6-725D-4081-9E5D-A073286EB3E2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ServiceName property'
---

# ISchedulerJob::ServiceName property

Gets or sets the name of the SOA service that the service tasks in the job use, if the job contains service tasks.

This property is read/write.

## Syntax


```C++
HRESULT put_ServiceName(
  [in]          BSTR pRetVal
);

HRESULT get_ServiceName(
  [out, retval] BSTR *pRetVal
);
```



## Property value

A string that specifies the name of the SOA service that the service tasks in the job use, if the job contains service tasks.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




