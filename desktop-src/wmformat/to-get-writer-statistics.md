---
title: To Get Writer Statistics
description: To Get Writer Statistics
ms.assetid: 81d7f567-0d99-4199-9248-1a497dc2eaab
keywords:
- Advanced Systems Format (ASF),writer statistics
- ASF (Advanced Systems Format),writer statistics
- writer statistics,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To Get Writer Statistics

The writer can provide statistical information about writing operations. There are two methods for gathering writer statistics: [**IWMWriterAdvanced::GetStatistics**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-getstatistics?branch=master) and [**IWMWriterAdvanced3::GetStatisticsEx**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced3-getstatisticsex?branch=master). The information retrieved by **GetStatisticsEx** is more specific than the information retrieved by **GetStatistics**.

Both methods populate structures with statistical information. **GetStatistics** uses the [**WM\_WRITER\_STATISTICS**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmwriterstatistics?branch=master) structure, and **GetStatisticsEx** uses the [**WM\_WRITER\_STATISTICS\_EX**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmwriterstatisticsex?branch=master) structure. **GetStatisticsEx** does not duplicate the data obtained by **GetStatistics**. For the most complete information, you should call both methods.

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced?branch=master)
</dt> <dt>

[**IWMWriterAdvanced3 Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced3?branch=master)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




