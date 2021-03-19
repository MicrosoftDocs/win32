---
description: The Windows Media Audio Voice decoder decodes streams that were encoded by the Windows Media Audio Voice Encoder.
ms.assetid: 8bb5c8bd-949f-4faa-b679-8854f78076a4
title: Windows Media Audio Voice Decoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Media Audio Voice Decoder

The Windows Media Audio Voice decoder decodes streams that were encoded by the [**Windows Media Audio Voice Encoder**](windowsmediaaudiovoiceencoder.md).

## Class Identifier

The class identifier (CLSID) for the Windows Media Audio Voice decoder is represented by the constant **CLSID\_CWMSPDecMediaObject**. You can create an instance of the voice decoder by calling **CoCreateInstance**.

## Input Formats

Windows Media Audio Voice encoded content is identified by the format tag 0x00A.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Wmspdmod.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Using the Windows Media Audio Voice Codec](usingthewindowsmediaaudio9voicecodec.md)
</dt> <dt>

[Windows Media Audio Voice Encoder](windowsmediaaudiovoiceencoder.md)
</dt> </dl>

 

 




