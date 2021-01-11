---
description: Why does the video encoder reject an output format that I try to set, when I retrieved the format from the same object?
ms.assetid: f0747450-d224-423a-a9f1-04580df8a17e
title: Why does the video encoder reject an output format that I try to set, when I retrieved the format from the same object?
ms.topic: article
ms.date: 05/31/2018
---

# Why does the video encoder reject an output format that I try to set, when I retrieved the format from the same object?

Unlike audio encoder output types, the supported outputs enumerated by the video encoders are not complete as delivered. You must set the bit rate of the stream in the **dwBitrate** member of the **VIDEOINFOHEADER** structure to match the value set for the [MFPKEY\_RAVG](mfpkey-ravgproperty.md) property.

After all of the options are set the way that you want them, you must retrieve the codec private data and append it to the **VIDEOINFOHEADER** structure. For more information, see [Using Video Codec Private Data](usingvideocodecprivatedata.md).

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 



