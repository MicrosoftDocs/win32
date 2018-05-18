---
Description: 'Retrieves the revision component of the version number.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd14c4579-7487-4b91-8ca3-ba72e8e56230'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IServerVersion::Revision property'
---

# IServerVersion::Revision property

Retrieves the revision component of the version number.

This property is read-only.

## Syntax


```C++
HRESULT get_Revision(
  [out] long *pRevision
);
```



## Property value

The revision number. Is –1 if undefined.

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

 

 




