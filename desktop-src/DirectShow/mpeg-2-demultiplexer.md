---
Description: 'This filter demultiplexes MPEG-2 transport and program streams that are delivered in push-mode.'
ms.assetid: '99bfc55d-6519-4e85-98ce-cad27bd71ffb'
title: 'MPEG-2 Demultiplexer'
---

# MPEG-2 Demultiplexer

This filter demultiplexes MPEG-2 transport and program streams that are delivered in push-mode. Starting in Windows XP, this filter also supports program streams in pull mode (file playback). On earlier platforms, use the [MPEG-2 Splitter](mpeg-2-splitter.md) filter for program streams in pull mode. This filter can be used in any type of filter graph, including a BDA digital TV filter graph.

> [!Note]  
> The MPEG-2 Demultiplexer does not support frame-accurate seeking.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>All modes:<br/>
<ul>
<li>[<strong>IBaseFilter</strong>](ibasefilter.md)</li>
<li><strong>ISpecifyPropertyPages</strong></li>
</ul>
Push mode only:<br/>
<ul>
<li>[<strong>IAMFilterMiscFlags</strong>](iamfiltermiscflags.md)</li>
<li>[<strong>IMpeg2Demultiplexer</strong>](impeg2demultiplexer.md)</li>
<li>[<strong>IReferenceClock</strong>](ireferenceclock.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major type: MEDIATYPE_STREAM<br/> Subtype:<br/>
<ul>
<li>KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT</li>
<li>MEDIASUBTYPE_MPEG2_PROGRAM</li>
<li>MEDIASUBTYPE_MPEG2_TRANSPORT</li>
<li>MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE</li>
</ul>
For more information, see [<strong>MPEG-2 Demultiplexer Media Types</strong>](mpeg-2-demultiplexer-media-types.md).<br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IMemInputPin</strong>](imeminputpin.md), [<strong>IPin</strong>](ipin.md), [<strong>IQualityControl</strong>](iqualitycontrol.md)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Audio and video elementary streams must have a major type of MEDIATYPE_Audio or MEDIATYPE_Video.<br/> For more information, see [<strong>MPEG-2 Demultiplexer Media Types</strong>](mpeg-2-demultiplexer-media-types.md).<br/></td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>[<strong>IPin</strong>](ipin.md), [<strong>IQualityControl</strong>](iqualitycontrol.md)Push mode only: [<strong>IAMPushSource</strong>](iampushsource.md), [<strong>IMPEG2PIDMap</strong>](impeg2pidmap.md), [<strong>IMPEG2StreamIdMap</strong>](impeg2streamidmap.md)<br/> Pull mode only: [<strong>IMediaSeeking</strong>](imediaseeking.md)<br/></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_MPEG2Demultiplexer</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>Available for testing only. Use the <strong>ISpecifyPropertyPages</strong> interface to access the property pages</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>mpg2splt.ax</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_NORMAL</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

To output audio and video elementary streams, the demux must receive the PCR and SCR streams. On the input side, this means a transport stream must contain the PAT and PMT tables that define the PID for the PCR stream; and program streams must contain at least one pack header.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of server support<br/>    | Windows Server 2003 R2<br/>                          |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
</dt> </dl>

 

 




