---
description: Finding Audio Encoder Output Types
ms.assetid: cd47d45b-ea47-4dec-867e-d51145d7f084
title: Finding Audio Encoder Output Types (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Finding Audio Encoder Output Types (Microsoft Media Foundation)

Because you must use an audio encoder output format that is enumerated by the audio encoder, you need to have a way of finding the format that is most suited to your needs. The number of channels, bits per sample, and sample rate of the output that you choose must match the values for the content that you compress. However, the encoder may support several types within these constraints.

The deciding factor for choosing a type is the bit rate of the encoded stream; you want to find a media type that matches your input and has a bit rate that is as close as possible to a target value. If you are enumerating one-pass VBR output types, it is the quality value that will decide the type you use. For more information about quality values in enumerated output types, see [Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md).

> [!Note]  
>    The audio encoder enumerates some types that are duplicates of other types in almost all ways. These duplicates exist for formats where the number of packets per second does not meet the requirements for storage in ASF files when synchronized with video. Audio synchronized with video in an ASF file must have 3 or more packets per second for bit rates less than 32000, and 5 or more packets per second for bit rates greater than or equal to 32000.

 

## Related topics

<dl> <dt>

[Configuring Audio Encoding](configuringaudioencoding.md)
</dt> <dt>

[Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md)
</dt> </dl>

 

 



