---
Description: 'Retrieves the exit code that the command set.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c7606bcd-7d38-4c4d-9af4-de5eed05334d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandTaskStateEventArg::ExitCode property'
---

# ICommandTaskStateEventArg::ExitCode property

Retrieves the exit code that the command set.

This property is read-only.

## Syntax


```C++
HRESULT get_ExitCode(
  [out] long *pExitCode
);
```



## Property value

The exit code that the command set.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Implementing the Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICommandTaskStateEventArg**](icommandtaskstateeventarg.md)
</dt> </dl>

 

 




