---
description: VMR with Multiple Streams (Mixing Mode)
ms.assetid: 053edb70-8631-4fe4-a137-2fe54e02ab9e
title: VMR with Multiple Streams (Mixing Mode)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VMR with Multiple Streams (Mixing Mode)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The VMR can render multiple input streams. In this configuration, called mixing mode, the VMR loads its mixer and compositor to perform the mixing and blending prior to rendering. Mixing mode can be used either while the VMR is in windowed mode or windowless mode.

Mixing mode requires that the graphics driver supports the DDCAPS\_BLTFOURCC and DDCAPS\_BLTSTRETCH capability flags (color space conversion and stretch blitting, respectively). Almost all new graphics drivers have those capabilities. In addition, the driver must support the creation of Direct3D render targets for the current display pixel depth. Some devices do not support Direct3D operations when the display is set to 24 bits per pixel. For more information, see the DirectX Graphics SDK documentation.

> [!Note]  
> When the VMR mixes multiple video streams, the filter graph does not seek correctly. If you need to seek multiple video streams, you must create separate filter graphs that share the same custom allocator-presenter object.

 

**Configuring the VMR-7 for Multiple Streams**

To render multiple input streams with the VMR-7, do the following:

1.  Before connecting any of the VMR's input pins, call the [**IVMRFilterConfig::SetNumberOfStreams**](/windows/desktop/api/Strmif/nf-strmif-ivmrfilterconfig-setnumberofstreams) method with the number of streams. This causes the VMR to load the mixer and compositor and to create the specified number of input pins.
2.  Call [**IVMRFilterConfig::SetRenderingPrefs**](/windows/desktop/api/Strmif/nf-strmif-ivmrfilterconfig-setrenderingprefs) to specify various rendering preferences.
3.  Connect the pins to the upstream filters. The easiest way to do this is to call [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) for each input stream. If the output pin on the upstream filter (usually a decoder) and the input pin on the VMR cannot agree on a connection, then a new instance of the VMR with default settings will be created. This will result in a new window with "ActiveMovie" in the title bar. To prevent this from happening, the application should always verify that the correct instance of the VMR is being used by calling a method such as [**IPin::ConnectedTo**](/windows/desktop/api/Strmif/nf-strmif-ipin-connectedto). Another option is to add the source filter and then connect the pins using **IGraphBuilder::Connect**.
4.  Use the [**IVMRMixerControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrmixercontrol) interface on the VMR to control parameters for each stream, such as the alpha value, the Z-ordering, and the output rectangle.
5.  Run the filter graph.

**Configuring the VMR-9 for Multiple Streams**

By default, the VMR-9 creates four input pins. If you want to mix more than four video streams, call [**IVMRFilterConfig9::SetNumberOfStreams**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setnumberofstreams) before connecting any input pins. Use the [**IVMRMixerControl9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixercontrol9) interface to set the stream parameters, such as alpha, Z-order, and position.

## Related topics

<dl> <dt>

[Using VMR Mixing Mode](using-vmr-mixing-mode.md)
</dt> </dl>

 

 



