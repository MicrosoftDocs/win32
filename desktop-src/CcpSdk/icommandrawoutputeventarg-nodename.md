---
Description: 'Retrieves the name of the node that generated the output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8a426ad-aec5-424a-aa22-9ba0308cb0a7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandRawOutputEventArg::NodeName property'
---

# ICommandRawOutputEventArg::NodeName property

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

[**ICommandRawOutputEventArg**](icommandrawoutputeventarg.md)
</dt> </dl>

 

 




