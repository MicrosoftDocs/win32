---
title: Color Space Conversion
description: Color Space Conversion
ms.assetid: f5f1ec99-b3b9-4420-bf64-3872d9bbe650
keywords:
- Windows Media Format SDK,color space conversion
- Advanced Systems Format (ASF),color space conversion
- ASF (Advanced Systems Format),color space conversion
- color space conversion
ms.topic: article
ms.date: 05/31/2018
---

# Color Space Conversion

There is often a difference between the color depth of the compressed video format in the profile and the input format. When this happens, the source video must be converted to conform to the color space of the destination. The writer handles this process, communicating with an internal color-space converter.

The reader also communicates with the color-space converter to reconcile any difference between the compressed format and the output format.

As with all transforms performed on data, converting between color depths can reduce the quality of the output. When possible, you should use input and output formats with the same color depth as the compressed format.

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> <dt>

[**Working with Outputs**](working-with-outputs.md)
</dt> </dl>

 

 




