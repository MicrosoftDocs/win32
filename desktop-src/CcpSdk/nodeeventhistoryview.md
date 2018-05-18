---
Description: 'Lists the events that occurred on the nodes of an HPC cluster. Events include the addition or removal of nodes and changes to the node state.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e3ebcd2d-adfb-48e9-8f7e-95b55dec629c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeEventHistoryView
---

# NodeEventHistoryView

Lists the events that occurred on the nodes of an HPC cluster. Events include the addition or removal of nodes and changes to the node state.



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
<td>NodeEventHistoryId<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>A unique numeric identifier for the node event.<br/></td>
</tr>
<tr class="even">
<td>NodeName<br/></td>
<td>nvarchar(64)<br/></td>
<td>No<br/></td>
<td>The name of the node for which the event occurred. <br/></td>
</tr>
<tr class="odd">
<td>EventTime<br/></td>
<td>datetime<br/></td>
<td>No<br/></td>
<td>The date and time in Coordinated Universal Time (UTC) at which the event occurred.<br/></td>
</tr>
<tr class="even">
<td>Event<br/></td>
<td>varchar(11)<br/></td>
<td>No<br/></td>
<td>The type of event the occurred. The following values are the possible types:<br/>
<ul>
<li>Added<br/></li>
<li>Removed<br/></li>
<li>Online<br/></li>
<li>Offline<br/></li>
<li>Reachable<br/></li>
<li>UnReachable<br/></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Remarks

The reporting database stores information about node events only for the number of days that the DataExtensibilityTtl configuration parameter specifies. This value is 365 by default.

To view the current value of the DataExtensibilityTtl configuration parameter, use the Get-HpcClusterProperty cmdlet with the Parameter and Name parameters, for example:


```PowerShell
Get-HpcClusterProperty -Parameter -Name DataExtensibilityTtl
```



To set or change the value of the DataExtensibilityTtl configuration parameter, use the Set-HpcClusterParameter cmdlet with the DataExtensibilityTtl parameter, for example:


```PowerShell
Set-HpcClusterProperty -DataExtensibilityTtl 730
```



## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[**NodeView**](nodeview.md)
</dt> </dl>

 

 




