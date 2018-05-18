---
title: To Get Writer Statistics
description: To Get Writer Statistics
ms.assetid: '81d7f567-0d99-4199-9248-1a497dc2eaab'
keywords: ["Advanced Systems Format (ASF),writer statistics", "ASF (Advanced Systems Format),writer statistics", "writer statistics,about"]
---

# To Get Writer Statistics

The writer can provide statistical information about writing operations. There are two methods for gathering writer statistics: [**IWMWriterAdvanced::GetStatistics**](iwmwriteradvanced-getstatistics.md) and [**IWMWriterAdvanced3::GetStatisticsEx**](iwmwriteradvanced3-getstatisticsex.md). The information retrieved by **GetStatisticsEx** is more specific than the information retrieved by **GetStatistics**.

Both methods populate structures with statistical information. **GetStatistics** uses the [**WM\_WRITER\_STATISTICS**](wm-writer-statistics.md) structure, and **GetStatisticsEx** uses the [**WM\_WRITER\_STATISTICS\_EX**](wm-writer-statistics-ex.md) structure. **GetStatisticsEx** does not duplicate the data obtained by **GetStatistics**. For the most complete information, you should call both methods.

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](iwmwriteradvanced.md)
</dt> <dt>

[**IWMWriterAdvanced3 Interface**](iwmwriteradvanced3.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




