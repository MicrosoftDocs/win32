---
title: Stream Buffer Source Filter
description: Stream Buffer Source Filter
ms.assetid: 435081e9-8a3f-42ab-9091-30c7c3dd59c6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Source Filter

*This topic applies only to Windows XP Service Pack 1 or later.*

The Stream Buffer Source filter is the source filter for the Stream Buffer Engine. It reads content that the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter or [Stream Buffer Sink2](stream-buffer-sink2-filter.md) filter has stored.



<table>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><dl>[<strong>IAMFilterMiscFlags</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389374)<br />
[<strong>IBaseFilter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389526)<br />
[<strong>IFileSourceFilter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389981)<br />
<strong>ISpecifyPropertyPages</strong><br />
[<strong>IStreamBufferMediaSeeking</strong>](/previous-versions/windows/desktop/api/Sbe/)<br />
[<strong>IStreamBufferMediaSeeking2</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffermediaseeking2)<br />
[<strong>IStreamBufferInitialize</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferinitialize)<br />
[<strong>IStreamBufferSource</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersource)<br />
[<strong>ISBE2GlobalEvent</strong>](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2globalevent)<br />
[<strong>ISBE2SpanningEvent</strong>](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2spanningevent)<br />
[<strong>ISBE2Crossbar</strong>](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar)<br />
</dl></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>All audio, video, and data types accepted<br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><dl>[<strong>IMediaSeeking</strong>](https://msdn.microsoft.com/library/windows/desktop/dd407023) (see Remarks)<br />
[<strong>IPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd390397)<br />
[<strong>IQualityControl</strong>](https://msdn.microsoft.com/library/windows/desktop/dd376912)<br />
[<strong>IStreamBufferDataCounters</strong>](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferdatacounters)<br />
[<strong>ISBE2StreamMap</strong>](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2streammap)<br />
</dl></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_StreamBufferSource</td>
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

The Stream Buffer Source filter supports the [**IMediaSeeking**](https://msdn.microsoft.com/library/windows/desktop/dd407023) interface for completed recordings only. For live content, use the [**IStreamBufferMediaSeeking**](/previous-versions/windows/desktop/api/Sbe/) interface, which has the same methods but slightly different behavior for each method. This reflects the fact that live content continuously grows on one end, as the show is being recorded, and shrinks on the other end, as backing files are deleted. See the description of the **IStreamBufferMediaSeeking** interface for details.

You can use the [**IStreamBufferMediaSeeking**](/previous-versions/windows/desktop/api/Sbe/) interface with completed recordings, but do not mix **IStreamBufferMediaSeeking** calls and [**IMediaSeeking**](https://msdn.microsoft.com/library/windows/desktop/dd407023) calls. After the first call to an **IStreamBufferMediaSeeking** method, the filter will fail any subsequent calls to **IMediaSeeking** methods and will also fail any subsequent **QueryInterface** calls for the **IMediaSeeking** interface.

To use the [**IStreamBufferMediaSeeking**](/previous-versions/windows/desktop/api/Sbe/) methods, an application should query the filter directly. To use the [**IMediaSeeking**](https://msdn.microsoft.com/library/windows/desktop/dd407023) methods, the application should query the Filter Graph Manager. The Filter Graph Manager routes the seek commands to the filter, as described in [Seeking](https://msdn.microsoft.com/library/windows/desktop/dd377559).

Beginning with Windows Media Center TV Pack 2008 and Windows 7, the Stream Buffer Source filter supports the .WTV file format. H.264 is added as the default supported media type. Several new interfaces are also added to the filter:

-   The [**ISBE2GlobalEvent**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2globalevent) and [**ISBE2SpanningEvent**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2spanningevent) interfaces offer the ability to obtain event data from global spanning events and in-band spanning events, respectively. A *global spanning event* sends state information that applies to all streams in the pipeline. An *in-band spanning event* is an in-band event that can be recorded as part of the state information in a stream. For more information how to obtain data from global spanning events, see [Receiving Spanning Events in the Stream Buffer Engine](receiving-spanning-events-in-the-stream-buffer-engine.md).
-   The [**ISBE2Crossbar**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar) interface provides the ability to define profiles of all media types (corresponding to output pins) for a Stream Buffer Source filter.
-   The [**ISBE2StreamMap**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2streammap) interface provides the ability to enumerate streams that are available for mapping to a Stream Buffer Source filter's output pins, and specify custom mappings between streams and output pins.

For more information on crossbars, profiles, and stream mappings, see [Stream Buffer Source Filter Enhancements in Windows 7](stream-buffer-source-filter-enhancements-in-windows-7.md).

## Related topics

<dl> <dt>

[Receiving Spanning Events in the Stream Buffer Engine](receiving-spanning-events-in-the-stream-buffer-engine.md)
</dt> <dt>

[Stream Buffer Engine Filters](stream-buffer-engine-filters.md)
</dt> <dt>

[Using the Stream Buffer Engine](using-the-stream-buffer-engine.md)
</dt> </dl>

 

 





