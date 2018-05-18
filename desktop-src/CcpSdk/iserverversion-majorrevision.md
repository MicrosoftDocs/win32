---
Description: 'Retrieves the high 16 bits of the Revision number.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c44b721f-00ce-45eb-b7ed-e34cf44d4fd5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IServerVersion::MajorRevision property'
---

# IServerVersion::MajorRevision property

Retrieves the high 16 bits of the [**Revision**](iserverversion-revision.md) number.

This property is read-only.

## Syntax


```C++
HRESULT get_MajorRevision(
  [out] long *pMajorRev
);
```



## Property value

The major revision number.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IServerVersion**](iserverversion.md)
</dt> </dl>

 

 




