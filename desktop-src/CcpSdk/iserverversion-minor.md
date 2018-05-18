---
Description: 'Retrieves the minor component of the version number.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cfbd2a03-4315-46b6-b325-4538e9ba40a8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IServerVersion::Minor property'
---

# IServerVersion::Minor property

Retrieves the minor component of the version number.

This property is read-only.

## Syntax


```C++
HRESULT get_Minor(
  [out] long *pMinor
);
```



## Property value

The minor number.

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

 

 




