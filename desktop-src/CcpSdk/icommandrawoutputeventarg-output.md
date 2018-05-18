---
Description: 'Retrieves the output from the command as a byte blob.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '290cd8ec-bb13-4a8d-ae50-41dd64859b4a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandRawOutputEventArg::Output property'
---

# ICommandRawOutputEventArg::Output property

Retrieves the output from the command as a byte blob.

This property is read-only.

## Syntax


```C++
HRESULT get_Output(
  [out] SAFEARRAY **pOutput
);
```



## Property value

The output from the command. The [**ICommandRawOutputEventArg::Type**](icommandrawoutputeventarg-type.md) property determines if the output is from the command or is message text from an HPC or system error.

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

[**ICommandRawOutputEventArg**](icommandrawoutputeventarg.md)
</dt> </dl>

 

 




