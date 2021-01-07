---
description: Connecting and Disconnecting Topology Nodes
ms.assetid: b2f70989-f0a8-4a11-baeb-18f026afaeab
title: Connecting and Disconnecting Topology Nodes
ms.topic: article
ms.date: 05/31/2018
---

# Connecting and Disconnecting Topology Nodes

For a topology to be functional, the source node and the output node must be connected. To connect two topology nodes, drag the node output of one node to the node input of the other node. TopoEdit displays the node connection as a black line. This is equivalent to connecting topology nodes by calling the [**IMFTopologyNode::ConnectOutput**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-connectoutput) method.

The topology can be resolved only if the node connection is valid; that is, if the media types of the two nodes are compatible. For information about resolving topologies, see [Resolving a Topology with TopoEdit](resolving-a-topology-with-topoedit.md).

If you attempt to make a connection from a node that is already connected, the new node connection replaces the old node connection.

To delete a connection, select the node connection and press the DELETE key or select **Delete** from the **Topology** menu.

## Related topics

<dl> <dt>

[Building Topologies by Using TopoEdit](building-topologies-by-using-topoedit.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 



