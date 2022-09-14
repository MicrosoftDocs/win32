---
description: Resolving a Topology with TopoEdit
ms.assetid: da3e2bbc-7c9f-4a15-8842-c1bb00662cd2
title: Resolving a Topology with TopoEdit
ms.topic: article
ms.date: 05/31/2018
---

# Resolving a Topology with TopoEdit

There are two types of topologies:

-   Partial Topology. The source node is connected directly to the output node. In some cases, a partial topology can have some intermediate transform nodes, such as effects, but not all. The transform nodes that are omitted are typically decoders or format conversion MFTs, such as color converters and audio resamplers.

-   Full Topology. The source node is connected to the output node through a transform node. This type of topology must have every node to process data.

TopoEdit can only play full topologies. TopoEdit uses the topology loader object, provided by Media Foundation, to convert a partial topology into a full topology by inserting the required transforms. The process of creating a full topology is called resolving a topology.

For information about topology types, see the Partial Topologies section in [About Topologies](about-topologies.md).

Before you resolve a topology ensure that:

-   The topology contains a source node and an output node.

-   The source and the output nodes are connected by a valid node connection. During topology resolution, the topology loader checks the media type of the nodes for compatibility. If an invalid node connection exists, then the process fails and an error message is displayed.

To resolve a topology, from the **Topology** menu, click **Resolve Topology**.

The toolbar indicates the topology status: **\[Resolved\]** or **\[Not Resolved\]**.

If TopoEdit resolves a topology successfully, **Topology Status** is set to **\[Resolved\]** and the playback controls are enabled.

Each time you make changes to the topology, **Topology Status** is set to **\[Not Resolved\]** which indicates that it must be resolved again.

## Related topics

<dl> <dt>

[Building Topologies by Using TopoEdit](building-topologies-by-using-topoedit.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 



