---
description: The IMediaDet interface retrieves information about a media file, such as the number of streams, and the media type, duration, and frame rate of each stream.
ms.assetid: 596fc84e-a88a-4e1b-aa48-b6dc9031db31
title: IMediaDet interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IMediaDet interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IMediaDet` interface retrieves information about a media file, such as the number of streams, and the media type, duration, and frame rate of each stream. It also contains methods for retrieving individual frames from a video stream. The [Media Detector (MediaDet)](media-detector--mediadet.md) object exposes this interface.

To obtain information about a file using this interface, perform the following steps:

1.  Create an instance of the MediaDet object by calling **CoCreateInstance**. The class ID is CLSID\_MediaDet.
2.  Call [**IMediaDet::put\_Filename**](imediadet-put-filename.md) to specify the name of the source file.
3.  Call [**IMediaDet::get\_OutputStreams**](imediadet-get-outputstreams.md) to obtain the number of output streams in the source.
4.  Call [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md) to specify a particular stream.
5.  Call any of the following methods:
    -   [**IMediaDet::get\_FrameRate**](imediadet-get-framerate.md)
    -   [**IMediaDet::get\_StreamLength**](imediadet-get-streamlength.md)
    -   [**IMediaDet::get\_StreamMediaType**](imediadet-get-streammediatype.md)
    -   [**IMediaDet::get\_StreamType**](imediadet-get-streamtype.md)

To retrieve a video frame, call [**IMediaDet::GetBitmapBits**](imediadet-getbitmapbits.md) or [**IMediaDet::WriteBitmapBits**](imediadet-writebitmapbits.md). The returned frame is always in 24-bit RGB format.

> [!Note]  
> Do not use the same MediaDet object with multiple files. To get information or video frames from more than one file, use separate MediaDet instances.

 

The **IMediaDet** interface does not support [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) formats, so you cannot use this interface to get interlaced fields or information about interlacing. Also, if the upstream decoder supports only **VIDEOINFOHEADER2**, you cannot use `IMediaDet`. This might be the case with an MPEG-2 decoder, for example. Also, the `IMediaDet` interface ignores any streams in the file that are not video or audio. For example, if the file contains an audio stream, a data stream, and a video stream, the **get\_OutputStreams** method will report only two streams (the audio and video).

## Members

The **IMediaDet** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IMediaDet** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMediaDet** interface has these methods.



| Method                                                        | Description                                                                                                |
|:--------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md)  | Switches the media detector to bitmap grab mode and seeks the filter graph to a specified time.<br/> |
| [**get\_CurrentStream**](imediadet-get-currentstream.md)     | Retrieves the stream number currently used by the media detector.<br/>                               |
| [**get\_Filename**](imediadet-get-filename.md)               | Retrieves the name of the source file currently used by the media detector.<br/>                     |
| [**get\_Filter**](imediadet-get-filter.md)                   | Retrieves a pointer to the source filter currently used by the media detector.<br/>                  |
| [**get\_FrameRate**](imediadet-get-framerate.md)             | Retrieves the frame rate of the current stream.<br/>                                                 |
| [**get\_OutputStreams**](imediadet-get-outputstreams.md)     | Retrieves the number of audio and video streams contained in the media source.<br/>                  |
| [**get\_StreamLength**](imediadet-get-streamlength.md)       | Retrieves the duration of the current stream.<br/>                                                   |
| [**get\_StreamMediaType**](imediadet-get-streammediatype.md) | Retrieves the media type of the current stream.<br/>                                                 |
| [**get\_StreamType**](imediadet-get-streamtype.md)           | Retrieves the globally unique identifier (GUID) for the media type of the current stream.<br/>       |
| [**get\_StreamTypeB**](imediadet-get-streamtypeb.md)         | Retrieves a string representing the GUID of the media type for the current stream.<br/>              |
| [**GetBitmapBits**](imediadet-getbitmapbits.md)              | Retrieves a video frame at the specified media time.<br/>                                            |
| [**GetSampleGrabber**](imediadet-getsamplegrabber.md)        | Retrieves a pointer to the [**ISampleGrabber**](isamplegrabber.md) interface.<br/>                  |
| [**put\_CurrentStream**](imediadet-put-currentstream.md)     | Specifies the stream number for the media detector to use.<br/>                                      |
| [**put\_Filename**](imediadet-put-filename.md)               | Specifies the name of the source file for the media detector to use.<br/>                            |
| [**put\_Filter**](imediadet-put-filter.md)                   | Specifies a source filter for the media detector to use.<br/>                                        |
| [**WriteBitmapBits**](imediadet-writebitmapbits.md)          | Retrieves a video frame at the specified media time and writes it to a file.<br/>                    |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 
