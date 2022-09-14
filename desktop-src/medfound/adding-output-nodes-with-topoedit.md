---
description: Adding Output Nodes with TopoEdit
ms.assetid: 23d60fc7-547b-4ef5-b334-5f1b38e58e92
title: Adding Output Nodes with TopoEdit
ms.topic: article
ms.date: 05/31/2018
---

# Adding Output Nodes with TopoEdit

In a topology, an output node represents a media sink that receives media data from a transform node and presents it for playback. The type of output node depends on the media type of the source node.

The following table shows the menu/toolbar command for adding an output node to the topology.




| Source media type | Menu/Toolbar Command | Description | 
|-------------------|----------------------|-------------|
| Audio stream | On the <strong>Topology</strong> menu, click <strong>Add SAR</strong>. | Creates an output node for the Streaming Audio Renderer (SAR) that plays an audio stream through an audio device such as a sound card. | 
| Video stream | On the <strong>Topology</strong> menu, click <strong>Add EVR</strong>. | Creates an output node for the enhanced video renderer (EVR) that displays frames for a video stream. | 
| Custom media sink | <ol><li>On the <strong>Topology</strong> menu, click <strong>Add Custom Sink</strong>.<br /> The <strong>Input Custom GUID</strong> dialog box opens.<br /></li><li><p>In the <strong>GUID:</strong> field, enter the GUID of your custom sink that you want to add to the topology.<br /></p><blockquote>[!Note]<br />TopoEdit expects the GUID in the format "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}". Otherwise, it fails to add the node and displays an "Invalid GUID" error message.</blockquote><p><br /></p></li><li>Click <strong>OK</strong>.<br /></li></ol> | Creates an output node for the stream sink for a custom media source.<br /> The custom sink must support <strong>CoCreateInstance</strong> so that the sink can be specified with a CLSID.<br /> | 




 

TopoEdit creates the specified output node. The **Topology Pane** shows the output node as a green box that shows the name of the stream sink.

For information about adding output nodes programmatically by using Media Foundation APIs, see [Creating Output Nodes](creating-output-nodes.md).

## Related topics

<dl> <dt>

[Building Topologies by Using TopoEdit](building-topologies-by-using-topoedit.md)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 




