---
Description: 'Indicates the node groups to which the nodes in an HPC cluster belong. Contains one row for each combination of node and node group where the node is a member of the node group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '522b601c-1ce3-4f30-a3bd-1e08566bf135'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeGroupMembershipView
---

# NodeGroupMembershipView

Indicates the node groups to which the nodes in an HPC cluster belong. Contains one row for each combination of node and node group where the node is a member of the node group.



| Column name          | Data type                | Can be null   | Description                                                     |
|----------------------|--------------------------|---------------|-----------------------------------------------------------------|
| NodeName<br/>  | nvarchar(64)<br/>  | No<br/> | The name of a node in the HPC cluster.<br/>               |
| GroupName<br/> | nvarchar(256)<br/> | No<br/> | The name of a node group to which the node belongs. <br/> |



 

## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[**NodeView**](nodeview.md)
</dt> <dt>

[**NodeGroupView**](nodegroupview.md)
</dt> </dl>

 

 




