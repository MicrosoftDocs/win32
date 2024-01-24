---
description: Advanced Topology Building
ms.assetid: 66aa07d8-6756-4d5b-9f0a-24b902da6fa2
title: Advanced Topology Building
ms.topic: article
ms.date: 05/31/2018
---

# Advanced Topology Building

This section describes some advanced techniques for building topologies. You can use these techniques if you want more control over the topologies that you send to the Media Session.

Because these techniques are intended for scenarios that go beyond the functionality provided by the standard topology loader, many of the details will depend on the particular requirements of your application. Therefore, this section is organized loosely around smaller subtasks, rather than complete, end-to-end scenarios.

The typical playback application follows these steps:

1.  The application builds a partial topology and queues it on the Media Session.
2.  The Media Session invokes the topology loader to resolve the topology.

If you want to go beyond the capabilities of the topology loader, there are three general approaches:

-   Build a complete topology. When you queue the topology on the Media Session, call [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) with the MFSESSION\_SETTOPOLOGY\_NORESOLUTION flag. This flag prevents the Media Session from attempting to resolve the topology.

-   Directly invoke the topology loader to resolve the topology. You can then modify the full topology before queuing it on the Media Session.

-   Implement a custom topology loader. With this approach, you queue a partial topology, but the Media Session invokes your custom loader instead of the standard Media Foundation implementation. One advantage of this approach is that you can perform custom topology building inside the protected environment. (In that case, however, the topology loader must be a trusted component. For more information, see [Protected Media Path](protected-media-path.md).)

This section contains the following topics.



| Topic                                                                          | Description                                                                                                      |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [Custom Topology Loaders](custom-topology-loaders.md)                         | How to provide a custom implementation of [**IMFTopoLoader**](/windows/desktop/api/mfidl/nn-mfidl-imftopoloader) for the Media Session.          |
| [Binding Output Nodes to Media Sinks](binding-output-nodes-to-media-sinks.md) | How to prepare the output nodes in a topology if you are using the topology loader outside of the Media Session. |
| [Adding a Decoder to a Topology](adding-a-decoder-to-a-topology.md)           | How to select a decoder manually and add it to a topology.                                                       |



 

## Related topics

<dl> <dt>

[Topologies](topologies.md)
</dt> </dl>

 

 



