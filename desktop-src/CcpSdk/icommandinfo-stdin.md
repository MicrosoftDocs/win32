---
Description: 'Retrieves the path to the standard input file used by the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3a401036-aae5-41af-beff-4852b4c1e1f6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandInfo::StdIn property'
---

# ICommandInfo::StdIn property

Retrieves the path to the standard input file used by the command.

This property is read-only.

## Syntax


```C++
HRESULT get_StdIn(
  [out] BSTR *pStdIn
);
```



## Property value

The path to the standard input file used by the command.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Header<br/>       | <dl> <dt>Corecrt\_wstdio.h</dt> </dl>           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICommandInfo**](icommandinfo.md)
</dt> </dl>

 

 




