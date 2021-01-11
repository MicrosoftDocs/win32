---
description: How can a video stream encoded using quality-based VBR have fewer frames than the original stream?
ms.assetid: acce9c88-2ee1-4628-9fd5-ccb441f8b43e
title: How can a video stream encoded using quality-based VBR have fewer frames than the original stream?
ms.topic: article
ms.date: 05/31/2018
---

# How can a video stream encoded using quality-based VBR have fewer frames than the original stream?

The frame count of an encoded stream can be lower than the frame count of the original for one of two reasons: duplicate frames and dropped frames.

The encoder does not normally produce frames that are exact duplicates of the previous frame. If you need to have a sample for every frame (this is required by some containers, for example), you can configure the encoder to produce "dummy" frames by setting the [MFPKEY\_PRODUCEDUMMYFRAMES](mfpkey-producedummyframesproperty.md) property to VARIANT\_TRUE.

The encoder drops frames when it cannot encode all of the frames without overflowing the buffer. Dropped frames affect the quality of the stream, duplicate frames do not.

You can get frame statistics from the encoder to determine whether frames have been dropped. For more information, see [Getting Encoding Statistics](gettingencodingstatistics.md).

Typically, quality-based VBR streams will only have fewer frames than the original if there are duplicate frames (because the bit rate is not constrained).

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 



