---
description: How Decoders Use IAMVideoAccelerator
ms.assetid: 0bc6b65b-4502-4c6f-a0f2-82a2bd444d1d
title: How Decoders Use IAMVideoAccelerator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How Decoders Use IAMVideoAccelerator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**IAMVideoAccelerator**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator) interface enables generic video acceleration operations, including DirectX Video Acceleration (VA). For non-DirectX VA acceleration, the decoder and video driver must both adhere to a common protocol.

This section describes the general order of operations that any decoder should follow when using this interface. Further information specific to DirectX VA-based decoders can be found in [Mapping DirectX Video Acceleration to IAMVideoAccelerator](mapping-directx-video-acceleration-to-iamvideoaccelerator.md).

> [!Note]  
> This interface is available in Windows 2000 and later.

 

The [**IAMVideoAccelerator**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator) interface is exposed on the input pin of the [Overlay Mixer](overlay-mixer-filter.md) or Video Mixing Renderer (VMR). The [**IAMVideoAcceleratorNotify**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoacceleratornotify) interface is exposed on the decoder's output pin. The sequence of events for connecting the filter pins is as follows:

1.  The Filter Graph Manager calls [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) on the decoder filter's output pin. An [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) is an optional parameter.
    -   [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) is a data structure that describes a type of media. It contains a majortype GUID (which in our case should be MEDIATYPE\_Video), a subtype GUID (which in our case should be a video accelerator GUID), and a variety of other things. One of those things is a format type GUID containing information about the media, including in our case the width and height of an uncompressed video picture, most likely in an [**MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-mpeg1videoinfo), [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader), [**MPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-mpeg2videoinfo), or [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure.
    -   The [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure, if present, tells the decoder to operate using the specified media type, which may be "fully specified" or "partially specified". If "fully specified," the decoder would normally simply attempt to operate with that media type. If "partially specified," it will attempt to find a "fully-specified" compatible mode of operation that it can use to connect in a manner consistent with the "partially-specified" media type.
    -   The ordinary manner for attempting to find a "fully-specified" media type to use for a connection is to simply run through a list of every "fully-specified" media type that the output pin supports which is compatible with the "partially-specified" media type and attempt to connect with each of them until successful. The process would normally be similar if no AM\_MEDIA\_TYPE is contained in the [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) call, but with the output pin needing to check all of its media types.
2.  If the decoder wants to check whether a specific [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) (including a video accelerator GUID) is supported by the downstream input pin, it can call that pin's [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) (with the video accelerator GUID as the subtype of the **AM\_MEDIA\_TYPE**) or it can simply attempt to connect to that pin as described in item 5 below.
3.  If the decoder does not know which video accelerator GUIDs the downstream input pin supports and does not wish to propose just some particular candidate video accelerator GUID by calling the downstream input pin's [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept), the decoder can call [**IAMVideoAccelerator::GetVideoAcceleratorGUIDs**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getvideoacceleratorguids) to get a list of the video accelerator GUIDs the pin supports.
4.  For some particular video accelerator GUIDs, the decoder can call the downstream input pin's [**IAMVideoAccelerator::GetUncompFormatsSupported**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getuncompformatssupported) to get a list of the **DDPIXELFORMAT** pixel formats that can be used to render a specific video accelerator GUID. The list returned should be considered to be in decreasing preference order (that is, with the most preferred format listed first).
5.  The decoder calls the downstream input pin's [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection), passing it an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) with the proper video accelerator GUID as the subtype of the media type. This sets up the connection for operation, including the creation of the uncompressed output surfaces (which are allocated using the width and height found in **AM\_MEDIA\_TYPE**, and the number of surfaces to allocate found by a call described below, and whatever other information the video accelerator has available and wishes to use for that purpose—such as the video accelerator GUID itself). If the downstream input pin rejects the video accelerator GUID or some other aspect of the connection, this can cause the **IPin::ReceiveConnection** to fail. If **IPin::ReceiveConnection** fails, this is indicated in a returned **HRESULT**, and the decoder can try to make the call again, for example, with a new video accelerator GUID in the **AM\_MEDIA\_TYPE** structure.
    -   [!Note]  
        > This is another way (and the most definitive way) for the decoder to determine what is supported by the downstream input pin—simply calling [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) and trying to connect, and then checking whether the connection attempt was successful.

         

    -   During the [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection), the renderer calls the decoder's [**IAMVideoAcceleratorNotify::GetUncompSurfacesInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getuncompsurfacesinfo), passing it the video accelerator GUID and an [**AMVAUncompBufferInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvauncompbufferinfo) structure, in order to figure out how many uncompressed surfaces to allocate. The decoder fills in and returns the structure, which contains the minimum and maximum number of surfaces to be allocated of the particular type, and a **DDPIXELFORMAT** structure describing the pixel format of the surfaces to be allocated.
    -   [!Note]  
        > Nothing is actually passed in to the decoder in the call to [**IAMVideoAcceleratorNotify::GetUncompSurfacesInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getuncompsurfacesinfo) other than the video accelerator GUID.

         

6.  The renderer calls the decoder's [**IAMVideoAcceleratorNotify::SetUncompSurfacesInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-setuncompsurfacesinfo), passing to the decoder the actual number of uncompressed surfaces that were allocated.
7.  The renderer calls the decoder's [**IAMVideoAcceleratorNotify::GetCreateVideoAcceleratorData**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getcreatevideoacceleratordata) to get any data needed to initialize the video accelerator.
8.  The decoder calls [**IAMVideoAccelerator::GetCompBufferInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getcompbufferinfo), passing it a video accelerator GUID, an [**AMVAUncompDataInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvauncompdatainfo) structure, and the number of compressed buffer types, to get in return a set of [**AMVACompBufferInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvacompbufferinfo) data structures, one corresponding to each type of compressed data buffer used by the video accelerator GUID.
    -   The [**AMVAUncompDataInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvauncompdatainfo) structure contains the width and height of the decoded uncompressed data (in pixels) and the DDPIXELFORMAT of the uncompressed picture.
    -   The [**AMVACompBufferInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvacompbufferinfo) data structures returned each contain:
        -   The number of compressed buffers needed of the specific type.
        -   The width and height of the surface to create (fields which may or may not have any actual meaning).
            > [!Note]  
            > The DirectDraw surface allocation operation for the compressed buffers does not currently provide for the width or height of these surfaces to be greater than or equal to 2^15, although the surface allocation call may not overtly fail if this limit is violated. Therefore, the driver could structure its requests for compressed buffer memory to avoid such extreme sizes. For example, rather than requesting a buffer with width="1" and height="65536", the driver should request a buffer of width="1024" and height="64".

             

        -   The total number of bytes to be used by the surface.
        -   A structure of type **DDSCAPS2** defining a DirectDrawSurface object, describing the capabilities to create surfaces to store compressed data.
        -   A DDPIXELFORMAT, describing the pixel format used to create surfaces to store compressed data (a field which may or may not have any actual meaning).

> [!Note]  
> The renderer's calls to some of the decoder's [**IAMVideoAcceleratorNotify**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoacceleratornotify) interface methods may (and normally would) occur inside of the decoder's call to the renderer's [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection). Specifically, this applies to the following:
>
> -   [**IAMVideoAcceleratorNotify::GetUncompSurfacesInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getuncompsurfacesinfo),
> -   [**IAMVideoAcceleratorNotify::SetUncompSurfacesInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-setuncompsurfacesinfo), and
> -   [**IAMVideoAcceleratorNotify::GetCreateVideoAcceleratorData**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getcreatevideoacceleratordata).

 

> [!Note]  
> To support dynamic format changes, the decoder may also call [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) and other methods per above while the filters are connected and running. This capability is provided in order to support dynamic format changes (although not in the H.263, Annex P, sense - as all data sets are started up again from scratch and any reference picture information is therefore lost).

 

The following is a description of [**IAMVideoAccelerator**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator) use during operation after initialization:

1.  For each uncompressed surface, the decoder calls [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) to begin the processing to create the output picture. When it does this, the decoder sends an [**AMVABeginFrameInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvabeginframeinfo) structure.
    -   The [**AMVABeginFrameInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvabeginframeinfo) structure contains an index for a destination buffer, a pointer to some data to send downstream, and a pointer to a place where the accelerator can put some data for the decoder to read.
    -   NOTE 1: The accelerator does not actually receive the destination buffer index, as it is translated by the renderer before going downstream.
    -   NOTE 2: [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) can be called more than once between calls to [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe).
    -   NOTE 3: There is no assumption within the interface operation that [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) and [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe) need to be called for the processing of every individual picture in the bitstream.

        What [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) does, as far as the interface is concerned, is create an association within the renderer between an index and an uncompressed surface. It also provides a means to call a specific function in a device driver (with support of a means of passing arbitrary data back and forth between the decoder and the device driver).

        (However, in DirectX VA operation there is a requirement described below that [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) and [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe) do need to be called for the processing of every individual picture in the bitstream.)

2.  For sending uncompressed data to the accelerator, the decoder calls:
    -   [**IAMVideoAccelerator::QueryRenderStatus**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-queryrenderstatus) to determine whether a buffer is safe for reading from or writing to.
    -   [**IAMVideoAccelerator::GetBuffer**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getbuffer) to lock and obtain access to a specified buffer (if it has not previously called this to get that access). **GetBuffer** can also be used to get a copy of the contents of the last uncompressed output picture for which [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) was called, providing [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe) has not been called for that destination buffer index. If the DDI returns a render status of DDERR\_WASSTILLDRAWING for the requested buffer, a sleep loop will be operated within **GetBuffer** until this condition is cleared. In order to call **GetBuffer**, the decoder will need some information from an [**AMVACompBufferInfo**](/previous-versions/windows/desktop/api/amva/ns-amva-amvacompbufferinfo) data structure which is obtained by calling [**IAMVideoAccelerator::GetCompBufferInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getcompbufferinfo).
    -   [**IAMVideoAccelerator::Execute**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-execute) to indicate that the data in a set of compressed buffers as indicated in an array of [**AMVABUFFERINFO**](/previous-versions/windows/desktop/api/amva/ns-amva-amvabufferinfo) data structures should be processed. A function code dwFunction is passed to the driver in this call. A lpPrivateInputData pointer is also passed to some data to send downstream, and a lpPrivateOutputData pointer is passed to a place where the downstream process can put some data for the decoder to read.
    -   [**IAMVideoAccelerator::ReleaseBuffer**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-releasebuffer) to indicate that the decoder has completed use of a specified buffer for the moment and no longer needs locked access to the buffer. (If the decoder wishes to continue to use the buffer, it can simply not call **IAMVideoAccelerator::ReleaseBuffer** for the moment, thus avoiding the need to call [**IAMVideoAccelerator::GetBuffer**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getbuffer) until it really intends to not use the buffer anymore.) The decoder should not write into the buffer after [**Execute**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-execute) is called until [**QueryRenderStatus**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-queryrenderstatus) indicates that the buffer is safe for writing.
3.  To complete output processing for a destination buffer, the decoder calls [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe). It can pass some arbitrary data downstream with this call, and that's essentially all that happens as a result of this call. It doesn't send a destination buffer index in this call, so it can't indicate to the accelerator precisely what destination buffer is completed unless this indication is contained in the arbitrary data that is passed.
4.  To display a frame, the decoder calls [**IAMVideoAccelerator::DisplayFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-displayframe) with the index of the frame to display and a [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) structure containing start and stop time stamps and relevant flags such as **dwTypeSpecificFlags** in the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure, and **dwInterlaceFlags** in the [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure. The decoder must verify that all decompression operations that affect the content of the frame have completed before calling **DisplayFrame**.
5.  Finally, the decoder should, upon completion of all processing, indicate completion of all remaining begun output frames by calling [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe) and release all of its locked buffers by calling [**IAMVideoAccelerator::ReleaseBuffer**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-releasebuffer) for each unreleased buffer.

## Related topics

<dl> <dt>

[Decoder Interfaces and Specifications](decoder-interfaces-and-specifications.md)
</dt> </dl>

 

 



