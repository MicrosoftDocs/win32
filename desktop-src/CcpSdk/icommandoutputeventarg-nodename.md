---
Description: 'Retrieves the name of the node that generated the output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5d09029f-0530-4bc3-931f-fe195d87db4c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandOutputEventArg::NodeName property'
---

# ICommandOutputEventArg::NodeName property

Retrieves the name of the node that generated the output.

This property is read-only.

## Syntax


```C++
HRESULT get_NodeName(
  [out] BSTR *pNodeName
);
```



## Property value

The name of the node that is running the command that generated the output.

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

 

 




