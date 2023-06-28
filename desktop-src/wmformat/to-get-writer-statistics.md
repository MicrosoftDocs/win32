---
title: To Get Writer Statistics
description: To Get Writer Statistics
ms.assetid: 81d7f567-0d99-4199-9248-1a497dc2eaab
keywords:
- Advanced Systems Format (ASF),writer statistics
- ASF (Advanced Systems Format),writer statistics
- writer statistics,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Get Writer Statistics

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer can provide statistical information about writing operations. There are two methods for gathering writer statistics: [**IWMWriterAdvanced::GetStatistics**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-getstatistics) and [**IWMWriterAdvanced3::GetStatisticsEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced3-getstatisticsex). The information retrieved by **GetStatisticsEx** is more specific than the information retrieved by **GetStatistics**.

Both methods populate structures with statistical information. **GetStatistics** uses the [**WM\_WRITER\_STATISTICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_writer_statistics) structure, and **GetStatisticsEx** uses the [**WM\_WRITER\_STATISTICS\_EX**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_writer_statistics_ex) structure. **GetStatisticsEx** does not duplicate the data obtained by **GetStatistics**. For the most complete information, you should call both methods.

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced)
</dt> <dt>

[**IWMWriterAdvanced3 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced3)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




