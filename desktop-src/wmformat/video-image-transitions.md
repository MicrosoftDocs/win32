---
title: Video Image Transitions
description: Video Image Transitions
ms.assetid: 201ddbfb-567b-4893-b754-569f1e7d8466
keywords:
- Windows Media Format SDK,video image transitions
- Advanced Systems Format (ASF),video image transitions
- ASF (Advanced Systems Format),video image transitions
- video image transitions
- Windows Media Video 9 Image v2 codec
- codecs,Windows Media Video 9 Image v2 codec
- video streams,Windows Media Video 9 Image v2 codec
- video streams,image transitions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Image Transitions

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Video 9 Image v2 codec animates a series of images, resulting in a video stream. The codec can manipulate two images at once, blending them together and creating a transition from one to the other according to the configuration you supply. This section describes the supported transitions and the parameters they require.

The transitions are listed in the following table by their global identifiers.



| Transition identifier                                                                           | Description                                                                                                                                  |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WMT\_VIDEOIMAGE\_TRANSITION\_BOW\_TIE**](wmt-videoimage-transition-bow-tie.md)              | New image is revealed in a set of triangles on opposite sides of the frame.                                                                  |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_CIRCLE**](wmt-videoimage-transition-circle.md)                 | New image is revealed in a circle.                                                                                                           |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_CROSS\_FADE**](wmt-videoimage-transition-cross-fade.md)        | No special transition, the blend coefficients of the two images determine the cross-fade (dissolve).                                         |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_DIAGONAL**](wmt-videoimage-transition-diagonal.md)             | New image is revealed along a diagonal line originating in one corner of the frame.                                                          |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_DIAMOND**](wmt-videoimage-transition-diamond.md)               | New image is revealed in a diamond.                                                                                                          |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_FADE\_TO\_COLOR**](wmt-videoimage-transition-fade-to-color.md) | Dissolves from the image to a frame of solid color.                                                                                          |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_FILLED\_V**](wmt-videoimage-transition-filled-v.md)            | New image is revealed in a triangle originating from one side of the frame.                                                                  |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_FLIP**](wmt-videoimage-transition-flip.md)                     | Old image is rotated on a y-axis through the center of the frame. The new image is revealed as the back of the old image.                    |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_INSET**](wmt-videoimage-transition-inset.md)                   | New image is revealed by a rectangle originating from one corner of the frame.                                                               |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_IRIS**](wmt-videoimage-transition-iris.md)                     | New image is revealed along an x-axis and a y-axis.                                                                                          |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_PAGE\_ROLL**](wmt-videoimage-transition-page-roll.md)          | Old image is transformed in a page-flipping effect, revealing the new image underneath.                                                      |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_RECTANGLE**](wmt-videoimage-transition-rectangle.md)           | New image is revealed by a rectangle within the frame.                                                                                       |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_REVEAL**](wmt-videoimage-transition-reveal.md)                 | New image is revealed along a straight line originating from one side of the frame.                                                          |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_SLIDE**](wmt-videoimage-transition-slide.md)                   | Old image slides out of the frame, revealing the new image underneath.                                                                       |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_SPLIT**](wmt-videoimage-transition-split.md)                   | New image is revealed by a horizontal or vertical split in the old image. The split appears along a straight line starting inside the frame. |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_STAR**](wmt-videoimage-transition-star.md)                     | New image is revealed by a five-pointed star inside the frame.                                                                               |
| [**WMT\_VIDEOIMAGE\_TRANSITION\_WHEEL**](wmt-videoimage-transition-wheel.md)                   | New image is revealed by four rotating spokes with a common pivot point.                                                                     |



 

Each transition is fully described in its own topic.

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> <dt>

[**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2)
</dt> </dl>

 

 




