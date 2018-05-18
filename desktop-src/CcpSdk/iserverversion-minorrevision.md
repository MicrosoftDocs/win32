---
Description: 'Retrieves the low 16 bits of the Revision number.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '55711ed9-29a0-40fe-a77d-9652871e7d5a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IServerVersion::MinorRevision property'
---

# IServerVersion::MinorRevision property

Retrieves the low 16 bits of the [**Revision**](iserverversion-revision.md) number.

This property is read-only.

## Syntax


```C++
HRESULT get_MinorRevision(
  [out] long *pMinorRev
);
```



## Property value

The minor revision number.

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

 

 




