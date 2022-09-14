---
description: About Topologies
ms.assetid: 4f69b099-0ca7-4ea6-8412-0f1ea02e1600
title: About Topologies
ms.topic: article
ms.date: 05/31/2018
---

# About Topologies

A topology is an object that represents how data flows in the pipeline. An application creates a topology to describe the path that each stream takes from the media source to a media sink. The application passes the topology to the Media Session, and the Media Session uses the topology to control the data flow.

The data-processing components in the pipeline (media sources, transforms, and media sinks) are represented in the topology as *nodes*. The flow of data from one component to another is represented by a connection between the nodes. The following node types are defined:

-   Source node: Represents a media stream on a media source.
-   Transform node: Represents a Media Foundation transform (MFT).
-   Output node: Represents a stream sink on a media sink.
-   Tee node: Represents a fork in the stream. Tee nodes are an exception to the rule that a node represents a pipeline object. Unlike other node types, the tee node simply directs the flow of data.

A functioning topology must contain at least one source node connected to an output node, possibly through one or more transform nodes. For example, the following diagram shows a simple topology with one stream.

![a diagram that shows a topology with one stream.](images/topology01.png)

For file playback, the transform node might represent a decoder and the output node would represent the audio or video renderer. For file encoding, the transform node would represent an encoder and the output node would represent an archive sink, such as the ASF file sink.

If two nodes are connected, the node that produces data is called the *upstream* node, and the node that receives data is called the *downstream* node. For example, in the previous diagram, the source node is upstream from the transform node.

In a pair of connected nodes, the connection point on the upstream node is called an *output*. The connection point on the downstream node is called an *input*. The following diagram shows a pair of nodes with their connection points, and the flow of data between them. The connection points are not represented as separate objects in the topology. They are specified by index value on the node object.

![a diagram that shows two connected nodes.](images/topology04.png)

A source node cannot have any inputs. Therefore, there cannot be any nodes upstream from a source node. Similarly, an output node cannot have outputs, and there cannot be any nodes downstream from an output node. A chain of nodes from a source node to an output node is called a *branch* of the topology. The first diagram in this topic shows a topology with a single branch. Generally there is one branch per stream. To play a file with one audio stream and one video stream, for example, requires a topology with two branches.

## Partial Topologies

A complete or *full* topology contains a node for every pipeline object that is needed. However, the application does not always need to create a full topology. Instead, it creates a *partial* topology that omits one or more transform nodes.

The Media Session completes the topology by using an object called the *topology loader*. The topology loader converts partial topologies into full topologies by inserting the needed transforms. The process of conversion is called *resolving* the topology.

For example, to play an encoded audio stream, the topology must have a decoder between the source and output nodes. The application creates a partial topology that connects the source node directly to the output node, without the decoder. The topology loader examines the stream formats, finds the right decoder, and inserts a transform node into the topology.

The following diagram shows the partial topology created by the application.

![a diagram that shows a partial with a source node and output node.](images/topology02.png)

The next diagram shows the full topology after the topology loader resolves it. In this example, the topology loader has inserted a transform node for the decoder.

![a diagram that shows a full topology.](images/topology03.png)

In the current version of Media Foundation, the topology loader supports topologies for playback. For file encoding and other scenarios, the application must construct a full topology.

Applications can also create the topology loader and use it directly. For example, you can use the topology loader to resolve a partial topology and then modify the full topology before giving it to the Media Session. To create the topology loader, call [**MFCreateTopoLoader**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopoloader).

## Related topics

<dl> <dt>

[Topologies](topologies.md)
</dt> </dl>

 

 



