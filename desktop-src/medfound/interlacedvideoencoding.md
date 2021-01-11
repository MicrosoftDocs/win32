---
description: Interlaced Video Encoding
ms.assetid: 7695d4e3-4a75-4972-ab02-bc532d6a4dce
title: Interlaced Video Encoding (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Interlaced Video Encoding (Microsoft Media Foundation)

Video data intended for use with computers is typically *progressive*, meaning that each frame is encoded as a single image. Some devices, like televisions, do not display a frame all at once, but as two images. One of the images, or fields, contains all of the even numbered rows. The other field contains the data for all of the odd numbered rows. Video encoded with more than one field per frame is called interlaced, because it is rendered by switching between the even field and the odd field.

In the past, interlaced video content was always de-interlaced before encoding with the Windows Media Video codec. Beginning with Windows Media 9 Series, however, the video encoder supports compression of interlaced content without first converting it to progressive. Maintaining interlacing in an encoded file is important if the content is ever rendered on an interlaced display, such as a television. This feature is of increasing importance, as support for Windows Media-based content spreads to DVD players, set-top boxes, and other home electronics.

The easiest way to encode and deliver interlaced video is to develop your application using the Windows Media Format SDK and storing the content in ASF files. The interlaced information about frames is passed to the codec using data unit extensions, which work well for ASF content, but are a little trickier to support in other containers. For more information about data unit extensions, see [Using Data Unit Extensions](usingdataunitextensions.md).

To support interlaced encoding involves two major steps: getting the frame information to the encoder, and delivering the information to the rendering application. These steps are described in the following paragraphs.

## Interlaced Video and the Encoder

The first step in encoding video with maintained interlacing is to configure the encoder to encode interlaced fields. To do this, set the [MFPKEY\_INTERLACEDCODINGENABLED](mfpkey-interlacedcodingenabledproperty.md) property to **TRUE**. This prepares the encoder to receive interlaced samples. Each input sample must contain both fields.

Each sample that you process with the encoder after activating interlaced encoding should have a data unit extension attached. Samples without the expected data unit extension are assumed to be progressive. The GUID identifying the extension is D590DC20-07BC-436C-9CF7-F3BBFBF1A4DC. The values passed by the objects of the Windows Media Format SDK are defined in the following table.



| Value      | Description                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000020 | Specifies that the sample is encoded with the bottom field first. This value is only meaningful when combined with the interlaced value. |
| 0x00000040 | Specifies that the sample is encoded with the top field first. This value is only meaningful when combined with the interlaced value.    |
| 0x00000080 | Specifies that the sample is interlaced. This is the only value that is meaningful to the codec DMOs.                                    |



 

One of the first two values is always combined with 0x80 using a bitwise **OR** before being set on the sample. However, the encoder only checks for 0x80 and disregards the rest of the extension. If the extension identifies the sample as interlaced, the encoder maintains the sample interlacing in the compressed stream, and embeds an indication flag in the stream so that the decoder can identify interlaced frames. Each interlaced sample is marked, so that source content that is a mix of progressive and interlaced can be encoded into a stream together.

The Windows Media Format SDK writer object includes the content type data unit extensions in the samples that it writes to the data section of the ASF container for use at the time of rendering.

## Reading and Rendering Interlaced Video

The decoder identifies interlaced samples based on the flag set in the stream by the encoder. As a default, the decoder deinterlaces the samples and delivers progressive outputs. The player application can configure the decoder to process outputs with interlacing maintained by setting the [MFPKEY\_DECODER\_DEINTERLACING](mfpkey-decoder-deinterlacingproperty.md) property.

The difficulty in interlaced video playback arises after the decoder delivers the samples. The renderer (video card or chip in a device) cannot properly display the video content without knowing which field is which. In applications using the Windows Media Format SDK, the content type data unit extension is retrieved from the uncompressed samples, and can be passed to the device.

When using the codec objects directly, none of this data transfer is automatic. You must implement data-unit-extension support, both in your buffer objects and in the container that you use for your encoded content. Most common types of media containers (like AVI) do not support sample-level metadata. You can implement your own system to store the data in the file and associate it with individual samples, but only a customized reader would be able to retrieve it.

> [!Note]  
> Setting the [MFPKEY\_INTERLACEDCODINGENABLED](mfpkey-interlacedcodingenabledproperty.md) property to **TRUE**, and then not sending any samples with the content-type data-unit extension attached can cause the encoder to crash. Set the encoder for interlaced encoding only if you have interlaced samples to deliver.

 

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



