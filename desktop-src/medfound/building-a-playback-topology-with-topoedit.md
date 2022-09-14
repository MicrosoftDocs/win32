---
description: Building a Playback Topology with TopoEdit
ms.assetid: 4d4c4ff9-dad1-4c79-a44a-2ad20f1bbca0
title: Building a Playback Topology with TopoEdit
ms.topic: article
ms.date: 05/31/2018
---

# Building a Playback Topology with TopoEdit

TopoEdit can build a playback topology for a local media file by automatically adding and connecting the source, transform, and output nodes. TopoEdit does not automatically resolve the topology. To play the topology, resolve it and then use the transport controls.

## To build and play a topology for a media file

1.  On the **File** menu, click **Render File**.

    This opens the **Select Media Source** dialog box.

2.  Navigate to the folder where the media file is located.
3.  In the **File name:** field, enter the name of the file.
4.  Click **Open**.

    The **Topology Pane** shows the connected topology. Internally, TopoEdit performs the following tasks:

    -   Enumerates the streams in the media file and creates the source nodes.
    -   Depending on the media type of the source nodes, adds transform nodes, such as decoders.
    -   Adds the Streaming Audio Renderer (SAR) sink for audio stream and the enhanced video renderer (EVR) sink for the video stream.
    -   Connects the node inputs and the node outputs.

5.  On the **Topology** menu, click **Resolve Topology**.
6.  Click the **Play** button on the toolbar to play the topology. The following image shows the **Play** button :::image type="icon" source="images/536e8908-ef44-4d25-98f1-c06b5ef37591.jpg":::.

## Related topics

<dl> <dt>

[Playback Controls in TopoEdit](playback-controls-in-topoedit.md)
</dt> <dt>

[Resolving a Topology with TopoEdit](resolving-a-topology-with-topoedit.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 



