---
description: Subobjects
ms.assetid: 03cbd590-b573-4a98-9ab7-fe548800cfcb
title: Subobjects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Subobjects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

Sources, effects, and transitions have internal pointers to other COM objects, called *subobjects*. The subobject performs the actual work of the object. The subobject of a source is the component that creates the video or audio data. The subobject of an effect or transition is the component that transforms the data; for example, in a video effect, it creates the visual effect in the video stream.

The type of subobject depends on the type of object:

-   Source: Any DirectShow source filter or parser filter that supports seeking and produces a format that DES supports. It can be a compressed format if DirectShow filters exist to decode it.
-   Effect: For video, any 2-D one-input Microsoft® DirectX® Transform object. For audio, any DirectShow audio effect filter.
-   Transition: For video, any 2-D two-input DirectX Transform object. Audio does not support transitions.

Groups, compositions, and tracks do not have subobjects.

The application does not directly set the subobject pointer. For effects and transitions, the application calls the [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) method to specify the GUID of the subobject. For source objects, an application typically calls the [**IAMTimelineSrc::SetMediaName**](iamtimelinesrc-setmedianame.md) to specify the name of a source file. However, the **SetSubObjectGUID** method can also be used for source objects, to specify the class identifier (CLSID) of a filter.

For more information, see [Working with Sources](working-with-sources.md) and [Working with Effects and Transitions](working-with-effects-and-transitions.md).

## Related topics

<dl> <dt>

[Overview of the Timeline Components](overview-of-the-timeline-components.md)
</dt> </dl>

 

 



