---
Description: 'Retrieves the name of the node that is running the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '140b8020-4c3e-4d24-9590-2dc6171a8cd3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandTaskStateEventArg::NodeName property'
---

# ICommandTaskStateEventArg::NodeName property

Retrieves the name of the node that is running the command.

This property is read-only.

## Syntax


```C++
HRESULT get_NodeName(
  [out] BSTR *pNodeName
);
```



## Property value

The name of the node that is running the command.

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

 

 




