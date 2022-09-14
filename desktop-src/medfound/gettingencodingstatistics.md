---
description: Describes statistics that you can retrieve from a Windows Media codec.
ms.assetid: 86c029af-e0fb-436a-b758-3f7d10c8bdeb
title: Getting Encoding Statistics (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Getting Encoding Statistics (Microsoft Media Foundation)

Information about what is happening in an encoding session is generally immediately available in the form of error codes returned when processing samples. However, there are some statistics that you can retrieve from the codec about various encoding aspects.

## Video Frame Information

Some video statistics that you can retrieve deal with the number of frames processed by the encoder. There are three frame number properties that you can read from the video encoder:

-   [MFPKEY\_TOTALFRAMES](mfpkey-totalframesproperty.md) is the number of frames processed through the input stream of the DMO.
-   [MFPKEY\_CODEDFRAMES](mfpkey-codedframesproperty.md) is the number of frames encoded. By subtracting this value from the total number of frames passed, you can determine how many frames were dropped.
-   [MFPKEY\_ZEROBYTEFRAMES](mfpkey-zerobyteframesproperty.md) is the number of frames not encoded because they duplicated content already included. This value is not subtracted from the number of coded frames reported by the DMO.

You can read video frame properties at any time during encoding. This can be useful in determining if the encoding settings are appropriate for your content; if there is a large difference between total frames and coded frames, the compressed content might not meet your quality requirements. You can read the final values after you finish encoding.

## VBR Buffer Statistics

Depending upon the encoding mode used, some or all of the buffer settings may be determined during encoding (for example, the bit rate of quality based VBR is not known until the content is encoded). There are four VBR buffer properties that you can get using the **IPropertyBag::Read** method:

-   [MFPKEY\_RAVG](mfpkey-ravgproperty.md) is the average bit rate of the VBR content.
-   [MFPKEY\_BAVG](mfpkey-bavgproperty.md) is the buffer window for the average bit rate.
-   [MFPKEY\_RMAX](mfpkey-rmaxproperty.md) is the peak bit rate of the VBR content.
-   [MFPKEY\_BMAX](mfpkey-bmaxproperty.md) is the peak buffer window.

After you begin processing samples, you should not read any of the VBR properties until you are finished encoding the stream. If you do, the encoder interprets your request as a signal that the encoding is complete. The next sample that you process is treated as a new encoding session.

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



