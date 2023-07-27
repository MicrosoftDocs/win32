---
description: The IAMTimelineTrack interface provides methods for manipulating track objects in DirectShow Editing Services (DES).A track contains a list of sources that are rendered in the final output.
ms.assetid: 42ac88f2-1361-413a-a9b0-95f5c32a7c3c
title: IAMTimelineTrack interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrack interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineTrack` interface provides methods for manipulating *track* objects in [DirectShow Editing Services](directshow-editing-services.md) (DES).

A track contains a list of sources that are rendered in the final output. Sources within the same track may not overlap. Video tracks can have both effects and transitions. The render engine applies effects before it applies transitions. Audio tracks can have effects, but not transitions. For more information, see [The Timeline Model](the-timeline-model.md).

To create a track object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_TRACK. You can query the returned **IAMTimelineObj** pointer for the `IAMTimelineTrack` interface.

## Members

The **IAMTimelineTrack** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineTrack** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineTrack** interface has these methods.



| Method                                                          | Description                                                                                                                                          |
|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AreYouBlank**](iamtimelinetrack-areyoublank.md)             | Determines whether the track is blank (contains no source objects).<br/>                                                                       |
| [**GetNextSrc**](iamtimelinetrack-getnextsrc.md)               | Searches the track for the next source that appears at the specified time or later.<br/>                                                       |
| [**GetNextSrc2**](iamtimelinetrack-getnextsrc2.md)             | Searches the track for the next source that appears at the specified time or later, with the given as a [**REFTIME**](reftime.md) value.<br/> |
| [**GetNextSrcEx**](iamtimelinetrack-getnextsrcex.md)           | Retrieves the next source after the specified source.<br/>                                                                                     |
| [**GetSourcesCount**](iamtimelinetrack-getsourcescount.md)     | Retrieves the number of sources in the track.<br/>                                                                                             |
| [**GetSrcAtTime**](iamtimelinetrack-getsrcattime.md)           | Retrieves the source object nearest to the specified time, according to the specified boundary conditions.<br/>                                |
| [**GetSrcAtTime2**](iamtimelinetrack-getsrcattime2.md)         | Retrieves the source object nearest to the specified time, given as a [**REFTIME**](reftime.md) value.<br/>                                   |
| [**InsertSpace**](iamtimelinetrack-insertspace.md)             | Splits any objects that exist at the specified time and inserts space between them.<br/>                                                       |
| [**InsertSpace2**](iamtimelinetrack-insertspace2.md)           | Splits any objects that exist at the specified time and inserts space between them, using [**REFTIME**](reftime.md) values.<br/>              |
| [**MoveEverythingBy**](iamtimelinetrack-moveeverythingby.md)   | Not supported.<br/>                                                                                                                            |
| [**MoveEverythingBy2**](iamtimelinetrack-moveeverythingby2.md) | Not supported.<br/>                                                                                                                            |
| [**SrcAdd**](iamtimelinetrack-srcadd.md)                       | Adds a source to the track.<br/>                                                                                                               |
| [**ZeroBetween**](iamtimelinetrack-zerobetween.md)             | Removes everything from the track between the specified times.<br/>                                                                            |
| [**ZeroBetween2**](iamtimelinetrack-zerobetween2.md)           | Removes everything from the track between the specified times, given as [**REFTIME**](reftime.md) values.<br/>                                |



 

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



 

 
