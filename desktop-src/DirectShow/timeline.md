---
description: Timeline
ms.assetid: '6cc36034-224c-4126-873b-0cfeceec9781'
title: Timeline
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Timeline

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The timeline object manages all of the objects in a video editing project. To create this object, call **CoCreateInstance**. The class identifier is CLSID\_AMTimeline.

To read Windows Media™ files, the application must provide a software certificate, also called a key. Register the application as a key provider through the timeline's **IObjectWithSite** interface. For more information, see [Unlocking the Windows Media Format SDK](unlocking-the-windows-media-format-sdk.md).

The timeline object exposes the following interfaces:

-   [**IAMSetErrorLog**](iamseterrorlog.md)
-   [**IAMTimeline**](iamtimeline.md)
-   **IObjectWithSite**
-   **IPersistStream**

## Related topics

<dl> <dt>

[The Timeline Model](the-timeline-model.md)
</dt> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 



