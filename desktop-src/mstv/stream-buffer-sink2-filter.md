---
title: Stream Buffer Sink2 Filter
description: Stream Buffer Sink2 Filter
ms.assetid: 1606eab6-84dc-49ba-8fb6-df3b8615bf85
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Stream Buffer Sink2 Filter

*This topic applies only to Windows 7 or Vista with Windows Media Center TV Pack 2008 installed.*

The Stream Buffer Sink2 filter is the new sink filter that handles the .WTV file format for the Stream Buffer Engine. It stores streamed content for the [Stream Buffer Source](stream-buffer-source-filter.md) filter to read.



<table>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><dl>[<strong>IBaseFilter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389526)<br />
<strong>ISpecifyPropertyPages</strong><br />
[<strong>IStreamBufferInitialize</strong>](/windows/previous-versions/Sbe/nn-sbe-istreambufferinitialize?branch=master)<br />
[<strong>IStreamBufferSink</strong>](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink?branch=master)<br />
[<strong>IStreamBufferSink2</strong>](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink2?branch=master)<br />
[<strong>IStreamBufferSink3</strong>](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink3?branch=master)<br />
</dl></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>All audio, video, and data types accepted<br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><dl>[<strong>IMemInputPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd407073)<br />
[<strong>IPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd390397)<br />
[<strong>IQualityControl</strong>](https://msdn.microsoft.com/library/windows/desktop/dd376912)<br />
[<strong>IStreamBufferDataCounters</strong>](/windows/previous-versions/Sbe/nn-sbe-istreambufferdatacounters?branch=master)<br />
</dl></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_SBE2Sink</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Sbe.dll</td>
</tr>
<tr class="odd">
<td>Merit</td>
<td>MERIT_DO_NOT_USE</td>
</tr>
<tr class="even">
<td>Category</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

This filter stores data in .WTV file format.

If this filter is stopped and restarted, the render graph loses context and cannot access the capture graph. However, the tuner can change channels while the graph is running without problems.

## Related topics

<dl> <dt>

[Stream Buffer Engine Filters](stream-buffer-engine-filters.md)
</dt> <dt>

[Using the Stream Buffer Engine](using-the-stream-buffer-engine.md)
</dt> </dl>

 

 





