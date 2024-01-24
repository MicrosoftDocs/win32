---
title: Watermark Category Types
description: Watermark Category Types
ms.assetid: 5e03963d-6635-48c9-a6fd-cc890c3e7dac
keywords:
- Windows Media Format SDK,watermark categories
- Advanced Systems Format (ASF),watermark categories
- ASF (Advanced Systems Format),watermark categories
- Windows Media Format SDK,DMO
- Advanced Systems Format (ASF),DMO
- ASF (Advanced Systems Format),DMO
- watermarking,category types
- DirectX Media Object (DMO),watermark category types
- DMO (DirectX Media Object),watermark category types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Watermark Category Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use the DMO enumeration function, **DMOEnum**, to get information about the watermarking DMOs that are installed on a computer. The Windows Media Format SDK defines GUIDs that identify the watermarking DMO categories. For more information about **DMOEnum**, see the DirectShow documentation on MSDN.

The following table lists the identifiers for watermarking categories.



| Watermarking DMO category constant | GUID                                 |
|------------------------------------|--------------------------------------|
| WMT\_DMOCATEGORY\_AUDIO\_WATERMARK | 65221c5a-fa75-4b39-b50c-06c336b6a3ef |
| WMT\_DMOCATEGORY\_VIDEO\_WATERMARK | 187cc922-8efc-4404-9daf-63f4830df1bc |



 

## Related topics

<dl> <dt>

[**GUID Values**](guid-values.md)
</dt> </dl>

 

 




