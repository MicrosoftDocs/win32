---
description: Using the Windows Media Audio Voice Codec
ms.assetid: 771acb04-33a4-4ea3-8f50-e5e3dbdf9495
title: Using the Windows Media Audio Voice Codec
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Audio Voice Codec

The Windows Media Audio Voice codec provides low bit-rate compression optimized for audio containing speech. The ability of the codec to produce such small samples is due to the limited frequency range of the sounds of the human voice. This optimization means that a dedicated voice encoder creates poor-quality output for content that contains more complicated sounds, like music. However, the Windows Media Audio Voice codec compensates for this potential quality issue by providing separate modes for voice, music, and mixed content. The codec analyzes mixed content to determine which mode to use for each portion of the file.

The Windows Media Audio Voice codec is implemented in the encoder object identified by the class identifier CLSID\_CWMSPEncMediaObject2, and in the decoder object identified by the class identifier CLSID\_CWMSPDecMediaObject. The format tag of media types using this codec is 0x00A.

## Configuring the Encoder

The voice encoder supports three modes: speech, music, and mixed. Each mode is optimized to get the best results for that type of content. You can configure the mode of the voice encoder by using the methods of **IPropertyStore** to set the [MFPKEY\_WMAVOICE\_ENC\_MusicSpeechClassMode](mfpkey-wmavoice-enc-musicspeechclassmodeproperty.md) property.

When configured for mixed content, the Windows Media Audio Voice codec will automatically detect passages of music in the content. If you are not satisfied with the results, you can specify the location of music in the content using an editing decision list (EDL). For more information, see [Using an Editing Decision List for Encoding Voice](usingavoiceeditingdecisionlist.md).

Unlike the other audio encoders, you can set the buffer window value for voice content by using the [MFPKEY\_WMAVOICE\_ENC\_BufferWindow](mfpkey-wmavoice-enc-bufferwindowproperty.md) property. However, the default values should work fine in most cases.

> [!Note]  
>    When configuring the voice encoder, it is very important that you set the output type before you set the input type. This is the recommended order of operations for all of the audio codecs, but the voice encoder can report erroneous output types if an input is set when you call **IMediaObject::GetOutputType** or **IMFTransform::GetOutputType**.

 

## Decoding

There are no special requirements for decoding voice audio. Form more information, see [Configuring Audio Decoding](configuringaudiodecoding.md).

## Related topics

<dl> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



