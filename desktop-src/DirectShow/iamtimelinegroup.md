---
description: The IAMTimelineGroup interface sets and retrieves properties on groups in DirectShow Editing Services (DES).A group contains one or more tracks, and possibly one or more compositions, which in turn contain source clips of a uniform type, such as video or audio. Groups are the topmost compositions in a timeline, and also expose the IAMTimelineComp interface. A timeline can contain multiple groups.Each group has the following attributes.An associated media type.The frame rate at which the group renders, in frames per second (FPS). All edits occur at a time rounded to the nearest frame boundary, as defined by the group's FPS setting.A priority level, for writing files with multiple streams of the same media type (for example, a two-video-stream AVI file).To create a group object, call IAMTimeline::CreateEmptyNode with the value TIMELINE\_MAJOR\_TYPE\_GROUP. You can query the returned IAMTimelineObj pointer for the IAMTimelineGroup interface.
ms.assetid: c24e5e0a-43a5-4ba7-ac28-6e2ebb341a38
title: IAMTimelineGroup interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineGroup interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineGroup` interface sets and retrieves properties on groups in [DirectShow Editing Services](directshow-editing-services.md) (DES).

A group contains one or more tracks, and possibly one or more compositions, which in turn contain source clips of a uniform type, such as video or audio. Groups are the topmost compositions in a timeline, and also expose the [**IAMTimelineComp**](iamtimelinecomp.md) interface. A timeline can contain multiple groups.

Each group has the following attributes.

-   An associated media type.
-   The frame rate at which the group renders, in frames per second (FPS). All edits occur at a time rounded to the nearest frame boundary, as defined by the group's FPS setting.
-   A priority level, for writing files with multiple streams of the same media type (for example, a two-video-stream AVI file).

To create a group object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_GROUP. You can query the returned [**IAMTimelineObj**](iamtimelineobj.md) pointer for the **IAMTimelineGroup** interface.

## Members

The **IAMTimelineGroup** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineGroup** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineGroup** interface has these methods.



| Method                                                                            | Description                                                                                     |
|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**ClearRecompressFormatDirty**](iamtimelinegroup-clearrecompressformatdirty.md) | Not supported.<br/>                                                                       |
| [**GetGroupName**](iamtimelinegroup-getgroupname.md)                             | Retrieves the application-defined name of the group.<br/>                                 |
| [**GetMediaType**](iamtimelinegroup-getmediatype.md)                             | Retrieves the uncompressed media type for the group.<br/>                                 |
| [**GetOutputBuffering**](iamtimelinegroup-getoutputbuffering.md)                 | Retrieves the number of frames rendered in advance during preview.<br/>                   |
| [**GetOutputFPS**](iamtimelinegroup-getoutputfps.md)                             | Retrieves the output frame rate of this group.<br/>                                       |
| [**GetPreviewMode**](iamtimelinegroup-getpreviewmode.md)                         | Retrieves the preview mode for the group.<br/>                                            |
| [**GetPriority**](iamtimelinegroup-getpriority.md)                               | Retrieves the group's priority.<br/>                                                      |
| [**GetSmartRecompressFormat**](iamtimelinegroup-getsmartrecompressformat.md)     | Retrieves the current compression format for smart recompression.<br/>                    |
| [**GetTimeline**](iamtimelinegroup-gettimeline.md)                               | Retrieves the timeline to which this group belongs.<br/>                                  |
| [**IsRecompressFormatDirty**](iamtimelinegroup-isrecompressformatdirty.md)       | Not supported.<br/>                                                                       |
| [**IsSmartRecompressFormatSet**](iamtimelinegroup-issmartrecompressformatset.md) | Determines whether a smart compression format was set for the group.<br/>                 |
| [**SetGroupName**](iamtimelinegroup-setgroupname.md)                             | Sets the application-defined name of the group.<br/>                                      |
| [**SetMediaType**](iamtimelinegroup-setmediatype.md)                             | Sets the uncompressed media type for the group.<br/>                                      |
| [**SetMediaTypeForVB**](iamtimelinegroup-setmediatypeforvb.md)                   | Specifies the group media type, for Automation clients.<br/>                              |
| [**SetOutputBuffering**](iamtimelinegroup-setoutputbuffering.md)                 | Specifies the number of frames rendered in advance during preview.<br/>                   |
| [**SetOutputFPS**](iamtimelinegroup-setoutputfps.md)                             | Sets the uncompressed output frame rate for this group.<br/>                              |
| [**SetPreviewMode**](iamtimelinegroup-setpreviewmode.md)                         | Sets the preview mode for the group.<br/>                                                 |
| [**SetRecompFormatFromSource**](iamtimelinegroup-setrecompformatfromsource.md)   | Sets the video recompression format using the compression format from a source file.<br/> |
| [**SetSmartRecompressFormat**](iamtimelinegroup-setsmartrecompressformat.md)     | Specifies a compression format to use for smart recompression.<br/>                       |
| [**SetTimeline**](iamtimelinegroup-settimeline.md)                               | Not supported.<br/>                                                                       |



 

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



 

 
