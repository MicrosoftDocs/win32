---
Description: Creating Topologies
ms.assetid: afd1e646-9bb6-4265-a225-6aaaf1a7bb2a
title: Creating Topologies
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Topologies

This section describes some of the general procedures for creating a topology.

The general steps for creating a topology are as follows:

1.  Create a new topology object by calling [**MFCreateTopology**](/windows/win32/mfidl/nf-mfidl-mfcreatetopology?branch=master). This function returns a pointer to the topology's [**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master) interface.

2.  Initially, the topology does not contain any nodes. To create nodes for the topology, call [**MFCreateTopologyNode**](/windows/win32/mfidl/nf-mfidl-mfcreatetopologynode?branch=master). This function returns a pointer to the node's [**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master) interface. You must specify the node type when you create the node:

    -   Source node.

    -   Transform node.

    -   Output node.

    -   Tee node.

3.  Initialize each node. The initialization process depends on the node type, as described in the topics that follow.

4.  Add each node to the topology by calling [**IMFTopology::AddNode**](/windows/win32/mfidl/nf-mfidl-imftopology-addnode?branch=master).

5.  Connect the nodes. To connect a node, call [**IMFTopologyNode::ConnectOutput**](/windows/win32/mfidl/nf-mfidl-imftopologynode-connectoutput?branch=master) on the upstream node, and pass in a pointer to the downstream node.

The following topics give the specific steps for each node type.



| Topic                                                    | Description                     |
|----------------------------------------------------------|---------------------------------|
| [Creating Source Nodes](creating-source-nodes.md)       | How to create a source node.    |
| [Creating Transform Nodes](creating-transform-nodes.md) | How to create a transform node. |
| [Creating Output Nodes](creating-output-nodes.md)       | How to create an output node.   |



 

## Related topics

<dl> <dt>

[Topologies](topologies.md)
</dt> </dl>

 

 



