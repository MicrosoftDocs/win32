---
Description: 'Retrieves a line of output from the command or an error message string.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e9727f4e-f232-4465-b906-580cf9806d0b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandOutputEventArg::Message property'
---

# ICommandOutputEventArg::Message property

Retrieves a line of output from the command or an error message string.

This property is read-only.

## Syntax


```C++
HRESULT get_Message(
  [out] BSTR *pMessage
);
```



## Property value

A line of output. The [**ICommandOutputEventArg::Type**](icommandoutputeventarg-type.md) property determines if the output is from the command or is message text from an HPC or system error.

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

[**ICommandOutputEventArg**](icommandoutputeventarg.md)
</dt> </dl>

 

 




