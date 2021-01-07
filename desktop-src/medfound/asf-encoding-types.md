---
description: ASF Encoding Types
ms.assetid: ffa99c6b-3b62-4068-96d5-ad57c340d088
title: ASF Encoding Types
ms.topic: article
ms.date: 05/31/2018
---

# ASF Encoding Types

The encoding methods all focus on the buffer used by the encoder to manage uncompressed input data. This buffer is defined by the bit rate of the stream, in bits per second, and the buffer window, in milliseconds. When encoding to ASF files, the Windows Media encoders abide by the constraints of the buffer. For more information about the buffer window, see [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md). Knowing how and when to use each method can help you create high-quality compressed content. The following table contains links to topics about each of the available encoding methods that an application can use to encode media data to ASF.



| Encoding method                                                                                      | Description                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Constant Bit Rate Encoding](constant-bit-rate-encoding.md)                                         | The encoder compresses data to a specified bit rate.                                                                                                                                                     |
| [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md)       | The encoder compresses data to a particular quality value so that the quality of the encoded media is consistent throughout its duration, regardless of the buffer requirements of the resulting stream. |
| [Unconstrained Variable Bit Rate Encoding](unconstrained-variable-bit-rate--vbr--encoding.md)       | The encoder compresses data to the highest possible quality while maintaining a specified bit rate. This mode is also called 2-pass variable bit rate (VBR) encoding.                                    |
| [Peak-Constrained Variable Bit Rate Encoding](peak-constrained-variable-bit-rate--vbr--encoding.md) | The encoder compresses data to a specified bit rate while keeping the buffer values under the specified maximum buffer window and bit rate. This mode is also called 2-pass peak VBR.                    |



 

## Related topics

<dl> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 



