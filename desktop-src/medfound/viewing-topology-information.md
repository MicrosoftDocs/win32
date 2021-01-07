---
description: Viewing Topology Information
ms.assetid: d687ecd3-9ad6-46d5-b927-d9b99af2002f
title: Viewing Topology Information
ms.topic: article
ms.date: 05/31/2018
---

# Viewing Topology Information

In TopoEdit, each topology item, such as nodes, node inputs, and node outputs, has an associated attribute store that manages the behavior of the node. To see the attributes, select the item, and the **Attributes Pane** displays the information. For topologies that are loaded from an XML file, some of the nodes may not display the entire attribute store. To see the entire attribute store, resolve the topology. For more information, see [Resolving a Topology with TopoEdit](resolving-a-topology-with-topoedit.md).

The following table shows the topology item and the attributes that the pane displays.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topology item</th>
<th>Attributes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Topology nodes</td>
<td><ul>
<li><a href="topology-node-attributes.md">Topology Node Attributes</a> for all nodes.<br/></li>
<li><a href="presentation-descriptor-attributes.md">Presentation Descriptor Attributes</a> for source nodes only.<br/></li>
<li>Input and output trust authority information for transform and output nodes.<br/></li>
</ul></td>
</tr>
<tr class="even">
<td>Node input</td>
<td><ul>
<li><a href="media-type-attributes.md">Media Type Attributes</a> for all nodes.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Node output</td>
<td><ul>
<li><a href="stream-descriptor-attributes.md">Stream Descriptor Attributes</a> for source nodes only.<br/></li>
<li><a href="media-type-attributes.md">Media Type Attributes</a> for all nodes.<br/></li>
</ul></td>
</tr>
</tbody>
</table>



 

The attribute values, except for pointer references and array values, can be changed. To change an attribute value, type in the new value next to the attribute and click **Save** on the **Attributes Pane**. The new value is updated in the attribute store and applied to the topology only after it is resolved.

## To add a new attribute for a node

1.  Select the node by clicking it on the **Topology Pane**.

    The attributes that are set on the node are shown on the **Attributes Pane**.

2.  On the **Attributes Pane**, click **Add**.

    This opens the **Add Attribute** dialog box.

3.  From the first drop-down list, choose the Attribute category.

    The categories depend on the topology node. For example, for the source node, the drop-down list shows **Presentation Descriptor Attributes** and **Node Attributes** as the available categories.

4.  From the second drop-down list, choose the attribute that you want to set on the node.

5.  In the edit box, add the value for the attribute.

6.  Click **Add** to add the attribute and return to the main window, or click **Cancel** to cancel the operation.

7.  From the **Topology** menu, click **Resolve Topology** to set the new attribute to the topology.

## Related topics

<dl> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 




