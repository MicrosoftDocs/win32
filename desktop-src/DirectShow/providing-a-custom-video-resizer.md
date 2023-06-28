---
description: Providing a Custom Video Resizer
ms.assetid: 4009f93f-cd50-440f-b943-7e3700e0e2cb
title: Providing a Custom Video Resizer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Providing a Custom Video Resizer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

> [!Note]  
> This feature requires DirectX 9.0 or later.

 

When [DirectShow Editing Services](directshow-editing-services.md) (DES) resizes a video source clip, the default behavior is a *StretchBlt*, which is fast but not anti-aliased. You can change the resizing behavior by implementing a custom resizer as a DirectShow transform filter. The filter must expose the [**IResize**](iresize.md) interface, which enables DES to specify the input and output video size. For information about writing a transform filter, see [Writing Transform Filters](writing-transform-filters.md). The **CTransformFilter** base class is recommended as the starting point. When you implement the filter, note the following:

-   Support the **IResize** interface on the filter (not the pins).
-   The filter should accept only [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) formats (FORMAT\_VideoInfo). Reject other format types.
-   The video format from DES may be any uncompressed RGB type, including 32-bit RGB with alpha (MEDIASUBTYPE\_ARGB32). Your filter can safely reject formats with **biHeight** < 0.
-   Before the Render Engine connects the filter's output pin, it calls [**IResize::put\_MediaType**](iresize-put-mediatype.md) to set the output type. It may also call [**IResize::put\_Size**](iresize-put-size.md) to adjust the output size. It can call these two methods in any order, any number of times, before it connects the output pin.
-   After the Render Engine connects the output pin, it might call **put\_Size** again. The resizer filter should reconnect its output pin with the new size.
-   Inside the filter's [**CTransformFilter::Transform**](ctransformfilter-transform.md) method, stretch the input video to the output size.
-   Your filter should never set the discontinuity flag on the output sample, or attach a media type to the output sample.
-   To save the filter's state in a GraphEdit (.grf) file, implement the **IPersistStream** interface. (This is optional, but useful for testing.)

To use the resizer filter, the filter must be registered as a COM object on the user's system. Before the application renders the video project, query the Render Engine for the [**IRenderEngine2**](irenderengine2.md) interface and call [**IRenderEngine2::SetResizerGUID**](irenderengine2-setresizerguid.md) with the CLSID of the resizer filter.

## Related topics

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> </dl>

 

 



