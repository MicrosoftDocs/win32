---
description: Using an Editing Decision List for Encoding Voice
ms.assetid: a3d88483-acc9-47cf-8735-f17bd3b4ad57
title: Using an Editing Decision List for Encoding Voice
ms.topic: article
ms.date: 05/31/2018
---

# Using an Editing Decision List for Encoding Voice

An editing decision list (EDL), is data given to a codec that provides information about how specific portions of content should be encoded. The Windows Media Audio 9 Voice codec supports a simple EDL in which you can specify the portions of content that contain music. By default, the codec detects passages of music itself when configured to encode mixed content. You should use an EDL only if the codec is not detecting the content types correctly.

To use an EDL, the voice encoder must be set to encode mixed content. Configure the mode of the voice codec to "mixed" by setting the [MFPKEY\_WMAVOICE\_ENC\_MusicSpeechClassMode](mfpkey-wmavoice-enc-musicspeechclassmodeproperty.md) property to 2. Set the EDL using the [MFPKEY\_WMAVOICE\_ENC\_EDL](mfpkey-wmavoice-enc-edlproperty.md) property. The value of this property is a string containing a comma-delimited list of the time ranges in the content that should be encoded as music. The first item in the list is the version of the EDL, which is always 1. The second item is the number of music sections described in the list. Following the second item are a number of pairs of values equal to the second item; each pair of values describes the starting and ending point of a music passage in the content, in milliseconds.

For example, the EDL string "1, 4, 1000, 2000, 5000, 6000, 9000, 10000, 13000, 14000" specifies four musical passages, each of which is one second long. If the information in the EDL string is invalid, it is ignored.

## Related topics

<dl> <dt>

[Using the Windows Media Audio 9 Voice Codec](usingthewindowsmediaaudio9voicecodec.md)
</dt> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



