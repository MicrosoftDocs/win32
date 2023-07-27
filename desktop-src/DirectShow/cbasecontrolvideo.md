---
description: The CBaseControlVideo class implements the IBasicVideo interface and controls the video properties of a generic video window. Generally, a CBaseControlVideo object is a video renderer that draws video into a window on the display.
ms.assetid: 16fc1b0a-e5b5-4f33-ac2b-5acff61bab81
title: CBaseControlVideo class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CBaseControlVideo class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cbasecontrolvideo class hierarchy](images/wctrl02.png)

The **CBaseControlVideo** class implements the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface and controls the video properties of a generic video window. Generally, a **CBaseControlVideo** object is a video renderer that draws video into a window on the display.

Many **CBaseControlVideo** member functions require only that the video renderer be connected to a filter graph. If it is not connected, member functions will return **VFW\_E\_NOT\_CONNECTED**. Properties set on a video renderer persist between successive connections and disconnections. All applications should ensure that they reset the renderer properties before starting a presentation.

When working with video, the application can select a portion of the video to use. This portion is the source rectangle that the **CBaseControlVideo** object controls. **CBaseControlVideo** enables your application to set and retrieve the source rectangle. All the rectangles that **CBaseControlVideo** uses employ width and height values rather than right and bottom values. When no source rectangle has been set, the properties of the source rectangle return the full, native video size.



| Protected Data Members                                                                   | Description                                                                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| m\_pFilter                                                                               | Pointer to an owning media filter.                                                              |
| m\_pInterfaceLock                                                                        | Externally defined critical section.                                                            |
| m\_pPin                                                                                  | Control of the media types for connection.                                                      |
| Member Functions                                                                         | Description                                                                                     |
| [**CBaseControlVideo**](cbasecontrolvideo-cbasecontrolvideo.md)                         | Constructs a **CBaseControlVideo** object.                                                      |
| [**CopyImage**](cbasecontrolvideo-copyimage.md)                                         | Creates a memory copy of a video image.                                                         |
| [**GetImageSize**](cbasecontrolvideo-getimagesize.md)                                   | Retrieves video image size information.                                                         |
| [**SetControlVideoPin**](cbasecontrolvideo-setcontrolvideopin.md)                       | Sets the pin with which this object should synchronize.                                         |
| Overridable Member Functions                                                             | Description                                                                                     |
| [**CheckSourceRect**](cbasecontrolvideo-checksourcerect.md)                             | Determines if a source rectangle is valid.                                                      |
| [**CheckTargetRect**](cbasecontrolvideo-checktargetrect.md)                             | Determines if a target rectangle is valid.                                                      |
| [**GetSourceRect**](cbasecontrolvideo-getsourcerect.md)                                 | Retrieves the current source video rectangle (pure virtual).                                    |
| [**GetStaticImage**](cbasecontrolvideo-getstaticimage.md)                               | Returns the current image in a memory buffer (pure virtual).                                    |
| [**GetTargetRect**](cbasecontrolvideo-gettargetrect.md)                                 | Retrieves the current target video rectangle (pure virtual).                                    |
| [**GetVideoFormat**](cbasecontrolvideo-getvideoformat.md)                               | Retrieves the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure containing the video format. |
| [**IsDefaultSourceRect**](cbasecontrolvideo-isdefaultsourcerect.md)                     | Determines if the renderer is using the default source rectangle (pure virtual).                |
| [**IsDefaultTargetRect**](cbasecontrolvideo-isdefaulttargetrect.md)                     | Determines if the renderer is using the default target rectangle (pure virtual).                |
| [**OnUpdateRectangles**](cbasecontrolvideo-onupdaterectangles.md)                       | Called when the source or target rectangle changes.                                             |
| [**OnVideoSizeChange**](cbasecontrolvideo-onvideosizechange.md)                         | Passes EC\_VIDEO\_SIZE\_CHANGED to the application.                                             |
| [**SetDefaultSourceRect**](cbasecontrolvideo-setdefaultsourcerect.md)                   | Sets the default source video rectangle (pure virtual).                                         |
| [**SetDefaultTargetRect**](cbasecontrolvideo-setdefaulttargetrect.md)                   | Sets the default target video rectangle (pure virtual).                                         |
| [**SetSourceRect**](cbasecontrolvideo-setsourcerect.md)                                 | Sets the current source video rectangle (pure virtual).                                         |
| [**SetTargetRect**](cbasecontrolvideo-settargetrect.md)                                 | Sets the current target rectangle (pure virtual).                                               |
| IBasicVideo Methods                                                                      | Description                                                                                     |
| [**get\_AvgTimePerFrame**](cbasecontrolvideo-get-avgtimeperframe.md)                    | Retrieves an approximate average time per frame.                                                |
| [**get\_BitErrorRate**](cbasecontrolvideo-get-biterrorrate.md)                          | Retrieves an approximate bit error rate.                                                        |
| [**get\_BitRate**](cbasecontrolvideo-get-bitrate.md)                                    | Retrieves an approximate bit rate for the video.                                                |
| [**GetCurrentImage**](cbasecontrolvideo-getcurrentimage.md)                             | Retrieves a memory rendering of the current image.                                              |
| [**get\_DestinationHeight**](cbasecontrolvideo-get-destinationheight.md)                | Retrieves the current destination rectangle's height.                                           |
| [**get\_DestinationLeft**](cbasecontrolvideo-get-destinationleft.md)                    | Retrieves the current destination rectangle's left coordinate.                                  |
| [**GetDestinationPosition**](cbasecontrolvideo-getdestinationposition.md)               | Retrieves the current destination position.                                                     |
| [**get\_DestinationTop**](cbasecontrolvideo-get-destinationtop.md)                      | Retrieves the current destination rectangle's top coordinate.                                   |
| [**get\_DestinationWidth**](cbasecontrolvideo-get-destinationwidth.md)                  | Retrieves the current destination rectangle's width.                                            |
| [**get\_SourceHeight**](cbasecontrolvideo-get-sourceheight.md)                          | Retrieves the current source rectangle's height.                                                |
| [**get\_SourceLeft**](cbasecontrolvideo-get-sourceleft.md)                              | Retrieves the current source rectangle's left coordinate.                                       |
| [**GetSourcePosition**](cbasecontrolvideo-getsourceposition.md)                         | Retrieves the current source position.                                                          |
| [**get\_SourceTop**](cbasecontrolvideo-get-sourcetop.md)                                | Retrieves the current source rectangle's top coordinate.                                        |
| [**get\_SourceWidth**](cbasecontrolvideo-get-sourcewidth.md)                            | Retrieves the current source rectangle's width.                                                 |
| [**get\_VideoHeight**](cbasecontrolvideo-get-videoheight.md)                            | Retrieves the native video height.                                                              |
| [**GetVideoPaletteEntries**](cbasecontrolvideo-getvideopaletteentries.md)               | Retrieves a range of palette entries for the video.                                             |
| [**GetVideoSize**](cbasecontrolvideo-getvideosize.md)                                   | Retrieves the width and height of the native video.                                             |
| [**get\_VideoWidth**](cbasecontrolvideo-get-videowidth.md)                              | Retrieves the native video width.                                                               |
| [**IsUsingDefaultDestination**](cbasecontrolvideo-isusingdefaultdestination.md)         | Determines if the renderer is using the default destination window.                             |
| [**IsUsingDefaultSource**](cbasecontrolvideo-isusingdefaultsource.md)                   | Determines if the renderer is using the default source window.                                  |
| [**put\_DestinationHeight**](cbasecontrolvideo-put-destinationheight.md)                | Sets the destination rectangle's height.                                                        |
| [**put\_DestinationLeft**](cbasecontrolvideo-put-destinationleft.md)                    | Sets the destination rectangle's left coordinate.                                               |
| [**put\_DestinationTop**](cbasecontrolvideo-put-destinationtop.md)                      | Sets the destination rectangle's top coordinate.                                                |
| [**put\_DestinationWidth**](cbasecontrolvideo-put-destinationwidth.md)                  | Sets the destination rectangle's width.                                                         |
| [**put\_SourceHeight**](cbasecontrolvideo-put-sourceheight.md)                          | Sets the source rectangle's height.                                                             |
| [**put\_SourceLeft**](cbasecontrolvideo-put-sourceleft.md)                              | Sets the source rectangle's left coordinate.                                                    |
| [**put\_SourceTop**](cbasecontrolvideo-put-sourcetop.md)                                | Sets the source rectangle's top coordinate.                                                     |
| [**put\_SourceWidth**](cbasecontrolvideo-put-sourcewidth.md)                            | Sets the source rectangle's width.                                                              |
| [**SetDefaultDestinationPosition**](cbasecontrolvideo-setdefaultdestinationposition.md) | Sets the default destination position again.                                                    |
| [**SetDefaultSourcePosition**](cbasecontrolvideo-setdefaultsourceposition.md)           | Sets the default source position again.                                                         |
| [**SetDestinationPosition**](cbasecontrolvideo-setdestinationposition.md)               | Sets the destination rectangle position.                                                        |
| [**SetSourcePosition**](cbasecontrolvideo-setsourceposition.md)                         | Sets the source rectangle position.                                                             |



 

## See also

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> </dl>

 

 



