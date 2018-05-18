---
Description: 'Lists the node groups for the HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2728dda2-7e6b-4344-882c-5e046bf54184'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeGroupView
---

# NodeGroupView

Lists the node groups for the HPC cluster.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Column name</th>
<th>Data type</th>
<th>Can be null</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GroupID<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>A unique numeric identifier for the node group.<br/></td>
</tr>
<tr class="even">
<td>GroupName<br/></td>
<td>nvarchar(256)<br/></td>
<td>No<br/></td>
<td>The name of the node group. The node group can be a custom node group that an administrator of the HPC cluster created or one of the following built-in node groups:<br/>
<ul>
<li>HeadNodes<br/></li>
<li>ComputeNodes<br/></li>
<li>WCFBrokerNodes<br/></li>
<li>HyperVHostNodes<br/></li>
<li>VirtualNodes<br/></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[NodeGroupMembershipView](nodegroupmembershipview.md)
</dt> <dt>

[**NodeView**](nodeview.md)
</dt> </dl>

 

 




