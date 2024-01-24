---
title: Video Image
description: Video Image
ms.assetid: 71183b90-dd10-49e3-9f03-9aad0cfe3d2a
keywords:
- Windows Media Format SDK,video images
- codecs,video images
- video images,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Image

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Video 9 Image v2 codec enables you to create Windows Media Video files whose content consists of a series of still images such as digital photographs. The images in the Video Image stream can be manipulated to produce pans and zooms as well as a number of transitions. End users can use this capability to create and share simple slide shows which can also contain a music soundtrack or voice-over narration. Because of the superior compression of the Windows Media Video Image codec, a file containing several photographs is still small enough to conveniently e-mail over the Internet.

A Video Image stream has its own media type and a specialized structure that defines the various transitions that are possible when moving from one image to the next. You can pan and zoom the view of the images while blending them together. The resulting file can then be played like any other Windows Media video file.

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Using the Windows Media Video 9 Image Codec**](using-the-windows-media-video-9-image-codec--deprecated.md)
</dt> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> <dt>

[**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2)
</dt> <dt>

[**Writing Video Image Samples**](writing-video-image-samples.md)
</dt> </dl>

 

 




