---
Description: 'Determines if the output is coming from a proxy task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '359202e7-fc03-44ff-a64f-f40ee653e242'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandTaskStateEventArg::IsProxy property'
---

# ICommandTaskStateEventArg::IsProxy property

Determines if the output is coming from a proxy task.

This property is read-only.

## Syntax


```C++
HRESULT get_IsProxy(
  [out] VARIANT_BOOL *pIsProxy
);
```



## Property value

Is VARIANT\_TRUE if the output is from a proxy; otherwise, VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

When you run a command, the server creates a separate command for each node on which the command will run. The server also creates a single proxy command that it uses to capture the output and return the output to the client. You can use this property to ignore state changes for the proxy.

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

 

 




