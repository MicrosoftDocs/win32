---
Description: 'Retrieves the date and time that the node last came online.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dd8faeb0-4514-440e-bf86-6a3cce4f1efd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::OnlineTime property'
---

# ISchedulerNode::OnlineTime property

Retrieves the date and time that the node last came online.

This property is read-only.

## Syntax


```C++
HRESULT get_OnlineTime(
  [out] DATE *pOnlineTime
);
```



## Property value

The last time that the node came online. The value is in Coordinated Universal Time.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**ISchedulerNode.OfflineTime**](ischedulernode-offlinetime.md)
</dt> <dt>

[**ISchedulerNode.MoveToOffline**](ischedulernode-movetooffline.md)
</dt> </dl>

 

 




