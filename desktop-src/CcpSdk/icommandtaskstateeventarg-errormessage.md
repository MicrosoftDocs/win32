---
Description: 'Retrieves the error message for the error that occurred while running the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cf69c9c7-2022-4d24-8515-8d08e443af30'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandTaskStateEventArg::ErrorMessage property'
---

# ICommandTaskStateEventArg::ErrorMessage property

Retrieves the error message for the error that occurred while running the command.

This property is read-only.

## Syntax


```C++
HRESULT get_ErrorMessage(
  [out] BSTR *pMessage
);
```



## Property value

The message text.

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

 

 




