---
Description: 'Retrieves the collection of node names on which the command will run or has run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd4bb4a57-e149-48f4-bdbb-da5194e3c2d8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::SortedNodeNames property'
---

# IRemoteCommand::SortedNodeNames property

Retrieves the collection of node names on which the command will run or has run.

This property is read-only.

## Syntax


```C++
HRESULT get_SortedNodeNames(
  [out] IStringCollection **pNodeNames
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains the collection of node names. The list is sorted.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The list of nodes is specified when you call the [**IScheduler::CreateCommand**](ischeduler-createcommand.md) method to create the command.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




