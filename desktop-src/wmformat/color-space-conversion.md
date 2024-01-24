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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Color Space Conversion

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




