---
Description: 'Retrieves the startup directory for the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7bf96e3f-4817-47c7-ba56-ea51c8309392'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandInfo::WorkingDirectory property'
---

# ICommandInfo::WorkingDirectory property

Retrieves the startup directory for the command.

This property is read-only.

## Syntax


```C++
HRESULT get_WorkingDirectory(
  [out] BSTR *pWorkDirectory
);
```



## Property value

The startup directory for the command.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICommandInfo**](icommandinfo.md)
</dt> </dl>

 

 




