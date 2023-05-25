---
description: The IAMTimelineComp interface inserts or retrieves virtual tracks on a composition in DirectShow Editing Services (DES).A composition is a collection of layers that acts as a single, composited track.
ms.assetid: b0a47303-9e3c-4b78-ac90-c5d8fce2b727
title: IAMTimelineComp interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineComp interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **IAMTimelineComp** interface inserts or retrieves virtual tracks on a composition in [DirectShow Editing Services](directshow-editing-services.md) (DES).

A composition is a collection of layers that acts as a single, composited *track*. For example, a composition that contains two tracks with a transition between them acts as a single track with the transition precomposited. A composition should contain media of only one type (such as audio or video), but this limitation is not enforced. A *virtual track* is any object that can reside in a composition, including tracks and other compositions.

The topmost nodes in the timeline are *groups*. Groups implement both the `IAMTimelineComp` interface and the [**IAMTimelineGroup**](iamtimelinegroup.md) interface.

To create a composition object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_COMPOSITE. You can query the returned [**IAMTimelineObj**](iamtimelineobj.md) pointer for the `IAMTimelineComp` interface. For more information, see [The Timeline Model](the-timeline-model.md) and [Constructing a Timeline](constructing-a-timeline.md).

## Members

The **IAMTimelineComp** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineComp** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineComp** interface has these methods.



| Method                                                                       | Description                                                                                                                                               |
|:-----------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetCountOfType**](iamtimelinecomp-getcountoftype.md)                     | Retrieves the number of objects of a given type contained in this composition and all of its virtual tracks, recursively.<br/>                      |
| [**GetNextVTrack**](iamtimelinecomp-getnextvtrack.md)                       | Retrieves the next virtual track after a specified virtual track.<br/>                                                                              |
| [**GetRecursiveLayerOfType**](iamtimelinecomp-getrecursivelayeroftype.md)   | Performs a depth-first ordering of the virtual tracks contained in this composition, and retrieves the *n*th virtual track from that ordering.<br/> |
| [**GetRecursiveLayerOfTypeI**](iamtimelinecomp-getrecursivelayeroftypei.md) | Not supported.<br/>                                                                                                                                 |
| [**GetVTrack**](iamtimelinecomp-getvtrack.md)                               | Retrieves the virtual track at the specified priority.<br/>                                                                                         |
| [**VTrackGetCount**](iamtimelinecomp-vtrackgetcount.md)                     | Retrieves the number of virtual tracks contained in the composition.<br/>                                                                           |
| [**VTrackInsBefore**](iamtimelinecomp-vtrackinsbefore.md)                   | Inserts a virtual track into the composition at the specified priority.<br/>                                                                        |
| [**VTrackSwapPriorities**](iamtimelinecomp-vtrackswappriorities.md)         | Switches the priority levels of two tracks.<br/>                                                                                                    |



 

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



 

 
