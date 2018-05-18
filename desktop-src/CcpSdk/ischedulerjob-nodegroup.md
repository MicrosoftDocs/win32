---
Description: 'Retrieves or sets the names of the node groups that specify the nodes on which the job can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4e5608e1-35d8-4f96-aa94-75e4b08293a3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::NodeGroups property'
---

# ISchedulerJob::NodeGroups property

Retrieves or sets the names of the node groups that specify the nodes on which the job can run.

This property is read/write.

## Syntax


```C++
HRESULT get_NodeGroups(
  [out] IStringCollection **pNodeGroups
);
```



## Property value

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) job property.

## Remarks

A node group is typically created to identify a group of nodes with a similar characteristic. For example, nodes that contain a specific software license. You can then use this property to identify the nodes instead of having to specify each node using the [**ISchedulerJob::RequestedNodes**](ischedulerjob-requestednodes.md) property.

If you specify multiple node groups, the resulting node list is the intersection of the groups. For example if group A contains nodes 1, 2, 3, and 4 and group B contains nodes 3, 4, 5, and 6, the resulting list is 3 and 4.

If you also specify nodes in the [**RequestedNodes**](ischedulerjob-requestednodes.md) property, the list of nodes on which the job may run is the intersection of the requested node list and the resulting node group list.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**IScheduler::GetNodeGroupList**](ischeduler-getnodegrouplist.md)
</dt> <dt>

[**IScheduler::GetNodesInNodeGroup**](ischeduler-getnodesinnodegroup.md)
</dt> </dl>

 

 




