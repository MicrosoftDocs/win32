---
Description: 'Retrieves the date and time that the node last went offline.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5ee0951f-cb66-465d-8baf-528fe78d1d83'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::OfflineTime property'
---

# ISchedulerNode::OfflineTime property

Retrieves the date and time that the node last went offline.

This property is read-only.

## Syntax


```C++
HRESULT get_OfflineTime(
  [out] DATE *pOfflineTime
);
```



## Property value

The last time that the node went offline. The value is in Coordinated Universal Time.

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

[**ISchedulerNode.OnlineTime**](ischedulernode-onlinetime.md)
</dt> <dt>

[**ISchedulerNode.MoveToOffline**](ischedulernode-movetooffline.md)
</dt> </dl>

 

 




