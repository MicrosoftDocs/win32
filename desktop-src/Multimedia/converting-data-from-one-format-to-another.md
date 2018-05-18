---
title: Converting Data from One Format to Another
description: Converting Data from One Format to Another
ms.assetid: 'df995b7d-ac45-4964-a1b0-efd079c0c010'
keywords: ["audio compression manager (ACM),converting data", "ACM (audio compression manager),converting data", "ACM examples,converting data", "converting data", "acmStreamOpen function", "acmStreamSize function", "acmStreamPrepareHeader function", "acmStreamConvert function", "acmStreamUnprepareHeader function", "acmStreamClose function"]
---

# Converting Data from One Format to Another

The ACM uses stream functions to support data format conversion. Converters in the ACM change the format, but not the data type. For example, a converter module can change 44-kHz, 16-bit data to 44-kHz, 8-bit data.

The following ACM functions support data format conversion. They are listed in the order in which you would typically use them.

-   The [**acmStreamOpen**](acmstreamopen.md) function opens a conversion stream.
-   The [**acmStreamSize**](acmstreamsize.md) function calculates the appropriate size of the source or destination buffer.
-   The [**acmStreamPrepareHeader**](acmstreamprepareheader.md) function prepares source and destination buffers to be used in a conversion.
-   The [**acmStreamConvert**](acmstreamconvert.md) function converts data in a source buffer into the destination format, writing the converted data into the destination buffer.
-   The [**acmStreamUnprepareHeader**](acmstreamunprepareheader.md) function cleans up the source and destination buffers prepared by **acmStreamPrepareHeader**. You must call this function before freeing the source and destination buffers.
-   The [**acmStreamClose**](acmstreamclose.md) function closes a conversion stream.

When converting data, first identify the source format, then choose the destination format. The easiest way to do this is by using the [**acmFormatChoose**](acmformatchoose.md) function, which displays a format-selection dialog box and returns the user's format choice.

When you know the source and destination formats, you can use [**acmStreamOpen**](acmstreamopen.md) to open a conversion stream. Then you can use the [**acmStreamSize**](acmstreamsize.md) function to determine the appropriate buffer sizes.

The next step is to prepare the buffers to be used in the conversion by using [**acmStreamPrepareHeader**](acmstreamprepareheader.md).

To perform the conversion, use [**acmStreamConvert**](acmstreamconvert.md) until all the buffers have been processed. When the conversion is complete, use [**acmStreamUnprepareHeader**](acmstreamunprepareheader.md) to clean up the buffers and then use [**acmStreamClose**](acmstreamclose.md) to close the conversion stream.

 

 




