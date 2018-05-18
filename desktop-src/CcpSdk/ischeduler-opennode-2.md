---
Description: 'Retrieves a node object using the specified node name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '87f82ae2-dde5-4dfc-b138-2af4efba29bc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::OpenNodeByName method'
---

# IScheduler::OpenNodeByName method

Retrieves a node object using the specified node name.

## Syntax


```C++
HRESULT OpenNodeByName(
  [in]  BSTR           nodeName,
  [out] ISchedulerNode **node
);
```



## Parameters

<dl> <dt>

*nodeName* \[in\]
</dt> <dd>

The name of the node to open.

</dd> <dt>

*node* \[out\]
</dt> <dd>

An [**ISchedulerNode**](ischedulernode.md) interface that you can use to retrieve information about the node.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetNodeIdList**](ischeduler-getnodeidlist.md)
</dt> <dt>

[**IScheduler::GetNodeList**](ischeduler-getnodelist.md)
</dt> <dt>

[**IScheduler::OpenNode**](ischeduler-opennode.md)
</dt> </dl>

 

 




