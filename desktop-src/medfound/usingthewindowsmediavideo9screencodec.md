---
description: Using the Windows Media Video 9 Screen Codec
ms.assetid: d88d5f5e-0935-4bbe-8abf-72cc536f9b40
title: Using the Windows Media Video 9 Screen Codec (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Video 9 Screen Codec (Microsoft Media Foundation)

The Windows Media Video 9 Screen codec is optimized for compressing *application video*, which consists of consecutive screen shots for a computer display. The codec takes advantage of the typical image simplicity (relatively few colors, lots of straight lines, and so on) and relative lack of motion to achieve a very high compression ratio. The disadvantage of this optimization is that video that doesn't conform to the expected characteristics of application video can be difficult to compress with an acceptable level of quality.

The Windows Media Video 9 Screen encoder is identified by the class identifier CLSID\_CMSSEncMediaObject2, and the decoder is identified the class identifier CLSID\_CMSSDecMediaObject. The FOURCC value for media types using this codec is "MSS2".

## Configuring the Encoder

The encoder of the Windows Media Video 9 Screen codec is configured in the same way as the standard video decoder.

> [!Note]  
> The screen encoder supports only one-pass encoding. You can set the [MFPKEY\_PASSESUSED](mfpkey-passesusedproperty.md) property to 2 and process the inputs twice without error, but there is no benefit to doing so. This is a known issue and may be corrected in future releases.

 

## Getting the Best Results

If you discover that the quality you want in your screen capture content requires a higher bit rate than you can use for your delivery scenario, you can try the following techniques to get more efficiency from the codec:

-   Use a smaller resolution for the screen capture. Capturing a larger screen resolution than needed can confuse the viewer by presenting unnecessary information.
-   Use a slower frame rate. Screen captures can often be effective at very low frame rates (sometimes as low as 4 or 5 frames per second).
-   Use fewer graphics in the screen capture. The Windows Media Video 9 Screen codec is optimized to encode Windows primitives and text with high quality. Usually problems occur because of bitmapped graphics, which often contain thousands of individual colors. The fewer bitmaps that are on the screen when you capture, the better your results will be. If you cannot eliminate graphics from your screen capture, there are several ways to minimize the impact that a bitmap has on image quality:
    -   Reduce the size of the graphic.
    -   Reduce the number of individual graphics that appear on the screen at the same time.
    -   Reduce the amount of movement of the graphic. For example, if the graphic is in a window, keep the window as stationary as possible.
    -   Avoid moving the mouse pointer over the graphic, or dragging windows or other elements over the graphic.

## Decoding

There are no special requirements for decoding screen capture video. However, as with all Windows Media Video 9 codecs, the screen capture decoder cannot properly decompress the encoded content without the codec private data.

## Related topics

<dl> <dt>

[Configuring Video Encoding](configuringvideoencoding.md)
</dt> <dt>

[Using Video Codec Private Data](usingvideocodecprivatedata.md)
</dt> <dt>

[Windows Media Video 9 Screen Encoder](windowsmediavideo9screenencoder.md)
</dt> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



