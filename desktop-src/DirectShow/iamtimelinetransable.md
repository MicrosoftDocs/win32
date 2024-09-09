---
description: The IAMTimelineTransable interface adds transitions to an object in DirectShow Editing Services (DES).
ms.assetid: 1be9adaa-4145-447c-b307-dabb4419c86c
title: IAMTimelineTransable interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTransable interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineTransable` interface adds transitions to an object in [DirectShow Editing Services](directshow-editing-services.md) (DES). This interface is exposed by any object that can have transitions applied to it, including tracks, compositions, and groups. An object that implements this interface can have any number of transitions, but the transitions must not overlap in time.

> [!Note]  
> Audio does not support transitions. Objects within audio groups can expose the `IAMTimelineTransable` interface, but the application should not add transitions to them.

 

## Members

The **IAMTimelineTransable** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineTransable** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineTransable** interface has these methods.



| Method                                                          | Description                                                                                                                        |
|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**GetNextTrans**](iamtimelinetransable-getnexttrans.md)       | Retrieves the first transition that appears at the specified time or later.<br/>                                             |
| [**GetNextTrans2**](iamtimelinetransable-getnexttrans2.md)     | Retrieves the first transition that appears at the specified time or later, with the time given as a **REFTIME** value.<br/> |
| [**GetTransAtTime**](iamtimelinetransable-gettransattime.md)   | Retrieves the transition nearest to the specified time.<br/>                                                                 |
| [**GetTransAtTime2**](iamtimelinetransable-gettransattime2.md) | Retrieves the transition nearest to the specified time, given as a **REFTIME** value.<br/>                                   |
| [**TransAdd**](iamtimelinetransable-transadd.md)               | Adds a transition to the object.<br/>                                                                                        |
| [**TransGetCount**](iamtimelinetransable-transgetcount.md)     | Retrieves the number of transitions on this object.<br/>                                                                     |



 

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



 

 
