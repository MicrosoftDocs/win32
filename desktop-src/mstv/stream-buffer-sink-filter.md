---
title: Stream Buffer Sink Filter
description: Stream Buffer Sink Filter
ms.assetid: e49fe3c2-e77f-419a-910c-78f72ebdfdbc
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Sink Filter

This topic applies only to Windows XP Service Pack 1 or later.

The Stream Buffer Sink filter is the sink filter for the Stream Buffer Engine. It stores streamed content for the [Stream Buffer Source](stream-buffer-source-filter.md) filter to read.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389526), <strong>ISpecifyPropertyPages</strong>, [<strong>IStreamBufferInitialize</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferinitialize), [<strong>IStreamBufferSink</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink), [<strong>IStreamBufferSink2</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink2), [<strong>IStreamBufferSink3</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink3)</td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Video:
<ul>
<li>MEDIATYPE_Video</li>
<li>MEDIASUBTYPE_MPEG2_VIDEO</li>
<li>MEDIASUBTYPE_dvsd</li>
</ul>
<strong>Audio and Data</strong>: All types accepted.<br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd407073), [<strong>IPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd390397), [<strong>IQualityControl</strong>](https://msdn.microsoft.com/library/windows/desktop/dd376912), [<strong>IStreamBufferDataCounters</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferdatacounters)</td>
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
<td>CLSID_StreamBufferSink</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Sbeio.dll</td>
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

The Stream Buffer Sink can receive data only at 1x speed. If the source is a file, the playback speed must be restricted to 1x.

If the Stream Buffer Sink is stopped and restarted, the render graph will lose context and be unable to access the capture graph. However, the tuner can change channels while the graph is running without problems.

## Related topics

<dl> <dt>

[Stream Buffer Engine Filters](stream-buffer-engine-filters.md)
</dt> <dt>

[Using the Stream Buffer Engine](using-the-stream-buffer-engine.md)
</dt> </dl>

 

 





