---
Description: 'Lists the nodes in an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c5a9fa64-3339-42be-a8f7-c289cbec402d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeView
---

# NodeView

Lists the nodes in an HPC cluster.



| Column name               | Data type                | Can be null    | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NodeID<br/>         | int<br/>           | No<br/>  | A unique numeric identifier for the node.<br/>                                                                                                                                                                                                                                                                                        |
| NodeName<br/>       | nvarchar(64)<br/>  | No<br/>  | The name of the node. <br/>                                                                                                                                                                                                                                                                                                           |
| Processor<br/>      | nvarchar(400)<br/> | Yes<br/> | The type of the processor for the node. This value is a string in the form of {Name="*processor\_name*", MaxClockSpeed="*speed*", L2Cache="*cache\_size*"}, where the value of MaxClockSpeed is the maximum speed of the processor in megahertz, and the value of L2Cache is the size of secondary processor cache in kilobytes.<br/> |
| NumberofCore<br/>   | int<br/>           | Yes<br/> | The number of cores for the node.<br/>                                                                                                                                                                                                                                                                                                |
| NumberofSocket<br/> | int<br/>           | Yes<br/> | The number of processors for the node.<br/>                                                                                                                                                                                                                                                                                           |
| MemorySize<br/>     | int<br/>           | Yes<br/> | The total amount of physical memory for the node, in megabytes. <br/>                                                                                                                                                                                                                                                                 |



 

## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[NodeGroupMembershipView](nodegroupmembershipview.md)
</dt> <dt>

[**NodeEventHistoryView**](nodeeventhistoryview.md)
</dt> <dt>

[**DailyNodeStatView**](dailynodestatview.md)
</dt> </dl>

 

 




