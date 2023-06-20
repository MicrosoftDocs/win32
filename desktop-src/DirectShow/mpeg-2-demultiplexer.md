---
description: This filter demultiplexes MPEG-2 transport and program streams that are delivered in push-mode.
ms.assetid: 99bfc55d-6519-4e85-98ce-cad27bd71ffb
title: MPEG-2 Demultiplexer
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MPEG-2 Demultiplexer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This filter demultiplexes MPEG-2 transport and program streams that are delivered in push-mode. Starting in Windows XP, this filter also supports program streams in pull mode (file playback). On earlier platforms, use the [MPEG-2 Splitter](mpeg-2-splitter.md) filter for program streams in pull mode. This filter can be used in any type of filter graph, including a BDA digital TV filter graph.

> [!Note]  
> The MPEG-2 Demultiplexer does not support frame-accurate seeking.

 




| Label | Value |
|--------|-------|
| Filter Interfaces | All modes:<br /><ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></li><li><strong>ISpecifyPropertyPages</strong></li></ul>Push mode only:<br /><ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags"><strong>IAMFilterMiscFlags</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-impeg2demultiplexer"><strong>IMpeg2Demultiplexer</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ireferenceclock"><strong>IReferenceClock</strong></a></li></ul> | 
| Input Pin Media Types | Major type: MEDIATYPE_STREAM<br /> Subtype:<br /><ul><li>KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT</li><li>MEDIASUBTYPE_MPEG2_PROGRAM</li><li>MEDIASUBTYPE_MPEG2_TRANSPORT</li><li>MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE</li></ul>For more information, see <a href="mpeg-2-demultiplexer-media-types.md"><strong>MPEG-2 Demultiplexer Media Types</strong></a>.<br /> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | Audio and video elementary streams must have a major type of MEDIATYPE_Audio or MEDIATYPE_Video.<br /> For more information, see <a href="mpeg-2-demultiplexer-media-types.md"><strong>MPEG-2 Demultiplexer Media Types</strong></a>.<br /> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a>Push mode only: <a href="/windows/desktop/api/Strmif/nn-strmif-iampushsource"><strong>IAMPushSource</strong></a>, <a href="/previous-versions/windows/desktop/api/Bdaiface/nn-bdaiface-impeg2pidmap"><strong>IMPEG2PIDMap</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-impeg2streamidmap"><strong>IMPEG2StreamIdMap</strong></a><br /> Pull mode only: <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a><br /> | 
| Filter CLSID | CLSID_MPEG2Demultiplexer | 
| Property Page CLSID | Available for testing only. Use the <strong>ISpecifyPropertyPages</strong> interface to access the property pages | 
| Executable | mpg2splt.ax | 
| <a href="merit.md">Merit</a> | MERIT_NORMAL | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Remarks

To output audio and video elementary streams, the demux must receive the PCR and SCR streams. On the input side, this means a transport stream must contain the PAT and PMT tables that define the PID for the PCR stream; and program streams must contain at least one pack header.

## Requirements



| Requirement | Value |
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

 

 




