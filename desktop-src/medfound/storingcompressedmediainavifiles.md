---
description: Describes how to store Windows Media data in an AVI file.
ms.assetid: f2a9d9ff-4876-4f24-b96a-5d89e42fa3d5
title: Storing Compressed Media in AVI Files (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Storing Compressed Media in AVI Files (Microsoft Media Foundation)

Any of the content that you compress using the Windows Media Audio and Video codecs must be put in some container format. One of the most popular formats is Audio Video Interleave, or AVI. You can use Microsoft Video for Windows (VfW) or Microsoft DirectShow to create AVI files. For more information about using Video for Windows or DirectShow, refer to the product documentation on MSDN.

The Windows Media Audio and Video codecs have been developed to use the properties of the Advanced Systems Format (ASF), which is the container used by Windows Media. Because AVI and ASF store content differently, some difficulties arise when storing content compressed with the Windows Media Audio and Video codecs in an AVI file.

The Windows Media Audio codecs compress audio content in such a way that it cannot be properly decompressed without time stamps for the individual samples. This enables some optimization in the compressed media. Because the ASF container keeps time stamps with all samples, this characteristic of the audio algorithms has always worked well.

AVI files, however, do not keep time stamps with samples. This means that Windows Media Audio content cannot be decompressed properly when stored in an AVI file. Windows Media Video content does not have this limitation, and can be included in AVI files. To encode Windows Media Video content to an AVI file with synchronized sound, you must use another audio codec.

The other issue with using an AVI file as a container for Windows Media concerns low-bit-rate video. One of the ways in which the Windows Media Video codecs produce video content for low bit rates is by dropping duplicate frames. If you want to put Windows Media Video content in an ASF file, you need to set the encoder to deliver dummy frames for duplicate frames (set [MFPKEY\_PRODUCEDUMMYFRAMES](mfpkey-producedummyframesproperty.md) to VARIANT\_TRUE) so that every frame is represented in the file. The dummy frames produced by the codec are 8 bytes in size. However, the frame written to file by the AVI multiplexer can be hundreds of bytes larger, and filled with random data. An AVI file made in this way will still be playable, but it will be much larger than expected. You can avoid this problem by using higher bit rates when encoding video for storage in AVI files.

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



