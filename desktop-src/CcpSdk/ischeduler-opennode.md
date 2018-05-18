---
Description: 'Retrieves a node object using the specified node identifier.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9ac76560-0873-48d6-a838-66024a4a1f93'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::OpenNode method'
---

# IScheduler::OpenNode method

Retrieves a node object using the specified node identifier.

## Syntax


```C++
HRESULT OpenNode(
  [in]  long           id,
  [out] ISchedulerNode **node
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

The identifier of the node to retrieve.

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

[**IScheduler::OpenNodeByName**](ischeduler-opennode-2.md)
</dt> </dl>

 

 




