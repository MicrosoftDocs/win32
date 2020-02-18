---
title: Getting Good Results with the Windows Media Video 9 Screen Codec
description: Getting Good Results with the Windows Media Video 9 Screen Codec
ms.assetid: c5b080d3-2934-4af7-8f01-9ab0829db05d
keywords:
- Windows Media Format SDK,Windows Media Video 9 Screen codec
- Advanced Systems Format (ASF),Windows Media Video 9 Screen codec
- ASF (Advanced Systems Format),Windows Media Video 9 Screen codec
- codecs,Windows Media Video 9 Screen
- Windows Media Video 9 Screen codec,results
ms.topic: article
ms.date: 05/31/2018
---

# Getting Good Results with the Windows Media Video 9 Screen Codec

The Windows Media Video 9 Screen codec is designed to produce highly compressed video for screen capture. Because most of the need for screen capture involves fairly simple and static images, the high levels of compression attained do not usually mean a great sacrifice in image quality. However, each screen capture is different, and the resulting image quality can vary considerably depending upon the circumstances.

The best way to determine the profile settings for a screen codec session is to encode a test file using a quality-based variable bit rate stream. Set the quality to the value you desire, and encode a screen capture as if you were recording the final file. When the file is written, play it using the asynchronous reader object, making regular calls to [**IWMReaderAdvanced::GetStatistics**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getstatistics). By monitoring the value of the **dwBandwidth** member of the [**WM\_READER\_STATISTICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_reader_statistics) structure for each call, you can determine the approximate bit rate required to achieve the quality you want. You can then use that bit rate for constant bit rate encoding.

If you discover that the quality you want requires a higher bit rate than you can use for your delivery scenario, you can try the following techniques to get more efficiency from the codec.

-   Use a smaller resolution for the screen capture. Capturing a larger screen resolution than you need can also create confusion for the viewer by presenting more information than is needed.
-   Use fewer graphics in the screen capture. The Windows Media Video 9 Screen codec is optimized to encode Windows primitives and text with high quality. Usually problems occur because of bitmapped graphics, which often contain thousands of individual colors. The fewer bitmaps that are on the screen when you capture, the better your results will be. If you cannot eliminate graphics from your screen capture, there are several ways to minimize the impact a bitmap has on image quality:
    -   Reduce the size of the graphic.
    -   Reduce the number of individual graphics that appear on the screen concurrently.
    -   Reduce the amount of movement of the graphic. For example, if the graphic is in a window, keep the window as stationary as possible.
    -   Avoid moving the mouse pointer over the graphic, or dragging windows or other elements over the graphic.
-   Use a slower [*frame rate*](wmformat-glossary.md). Screen captures can often be effective at very low frame rates (sometimes as low as 4 or 5 frames per second).
-   Reduce the bit rate of the accompanying audio.

Also, the codec does not support resizing of the video rectangle. In other words, if you try to use the codec to encode a 800 x 600 screen down into to a 640 x 480 video rectangle, the resulting video will have significant artifacts that may make much of the text on the screen illegible.

## Related topics

<dl> <dt>

[**Configuring Screen Capture Streams**](configuring-screen-capture-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




