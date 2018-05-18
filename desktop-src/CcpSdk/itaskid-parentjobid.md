---
Description: 'Retrieves the identifier that identifies the parent job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4c50d741-0fb4-440e-b02e-c62c36278921'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskId::ParentJobId property'
---

# ITaskId::ParentJobId property

Retrieves the identifier that identifies the parent job.

This property is read-only.

## Syntax


```C++
HRESULT get_ParentJobId(
  [out] long *pParentId
);
```



## Property value

The identifier for the parent job.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITaskId**](itaskid.md)
</dt> </dl>

 

 




