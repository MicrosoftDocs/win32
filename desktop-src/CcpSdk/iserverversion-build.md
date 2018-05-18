---
Description: 'Retrieves the build component of the version number.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9cb8dad0-aa65-47db-a6fd-7b58780f9cc8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IServerVersion::Build property'
---

# IServerVersion::Build property

Retrieves the build component of the version number.

This property is read-only.

## Syntax


```C++
HRESULT get_Build(
  [out] long *pBuild
);
```



## Property value

The build number. Is –1 if undefined.

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

 

 




