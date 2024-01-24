---
title: Converting Data from One Format to Another
description: Converting Data from One Format to Another
ms.assetid: df995b7d-ac45-4964-a1b0-efd079c0c010
keywords:
- audio compression manager (ACM),converting data
- ACM (audio compression manager),converting data
- ACM examples,converting data
- converting data
- acmStreamOpen function
- acmStreamSize function
- acmStreamPrepareHeader function
- acmStreamConvert function
- acmStreamUnprepareHeader function
- acmStreamClose function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Converting Data from One Format to Another

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The ACM uses stream functions to support data format conversion. Converters in the ACM change the format, but not the data type. For example, a converter module can change 44-kHz, 16-bit data to 44-kHz, 8-bit data.

The following ACM functions support data format conversion. They are listed in the order in which you would typically use them.

-   The [**acmStreamOpen**](/windows/desktop/api/Msacm/nf-msacm-acmstreamopen) function opens a conversion stream.
-   The [**acmStreamSize**](/windows/desktop/api/Msacm/nf-msacm-acmstreamsize) function calculates the appropriate size of the source or destination buffer.
-   The [**acmStreamPrepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamprepareheader) function prepares source and destination buffers to be used in a conversion.
-   The [**acmStreamConvert**](/windows/desktop/api/Msacm/nf-msacm-acmstreamconvert) function converts data in a source buffer into the destination format, writing the converted data into the destination buffer.
-   The [**acmStreamUnprepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamunprepareheader) function cleans up the source and destination buffers prepared by **acmStreamPrepareHeader**. You must call this function before freeing the source and destination buffers.
-   The [**acmStreamClose**](/windows/desktop/api/Msacm/nf-msacm-acmstreamclose) function closes a conversion stream.

When converting data, first identify the source format, then choose the destination format. The easiest way to do this is by using the [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) function, which displays a format-selection dialog box and returns the user's format choice.

When you know the source and destination formats, you can use [**acmStreamOpen**](/windows/desktop/api/Msacm/nf-msacm-acmstreamopen) to open a conversion stream. Then you can use the [**acmStreamSize**](/windows/desktop/api/Msacm/nf-msacm-acmstreamsize) function to determine the appropriate buffer sizes.

The next step is to prepare the buffers to be used in the conversion by using [**acmStreamPrepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamprepareheader).

To perform the conversion, use [**acmStreamConvert**](/windows/desktop/api/Msacm/nf-msacm-acmstreamconvert) until all the buffers have been processed. When the conversion is complete, use [**acmStreamUnprepareHeader**](/windows/desktop/api/Msacm/nf-msacm-acmstreamunprepareheader) to clean up the buffers and then use [**acmStreamClose**](/windows/desktop/api/Msacm/nf-msacm-acmstreamclose) to close the conversion stream.

 

 




