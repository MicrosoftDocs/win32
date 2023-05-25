---
description: Line 21 Decoder Filter
ms.assetid: 48fa5484-1f8c-4133-b2e1-888cb1834402
title: Line 21 Decoder Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Line 21 Decoder Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

This Line 21 Decoder filter decodes line 21 data and draws the caption text onto bitmaps.

The input pin connects to any line 21 data provider, typically either a DVD video decoder or the [CC Decoder](cc-decoder-filter.md) filter. The CC Decoder provides line 21 data from the VBI of an analog television signal. The output pin connects to a secondary pin on the [Overlay Mixer](overlay-mixer-filter.md) or to another video renderer, such as the VMR.

This filter accepts line 21 data in the standard byte-pair format or, for DVD, as a packet for the whole group of pictures (GOP). For every GOP in the DVD video stream, there can be a user data packet that has that particular GOP's header information and line 21 data. The format of the byte pairs is defined in the EIA/CEA-608-B standard; please refer to that standard for more information.

Two versions of this filter are available:



| Filter            | CLSID                 |
|-------------------|-----------------------|
| Line 21 Decoder   | CLSID\_Line21Decoder  |
| Line 21 Decoder 2 | CLSID\_Line21Decoder2 |



 

The version 1 filter is used on Microsoft® Windows® 95/98/Me and Windows 2000 platforms. The version 2 filter is available in Microsoft Windows XP and later, and is used whenever the Video Mixing Renderer is in the graph.

The information in the following table applies to both versions of the filter:




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/previous-versions/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder"><strong>IAMLine21Decoder</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a> | 
| Input Pin Media Types | Major Type: MEDIATYPE_AUXLine21DataSubtype:<br /><ul><li>MEDIASUBTYPE_Line21_BytePair (standard line 21)</li><li>MEDIASUBTYPE_Line21_GOPPacket (DVD line 21)</li></ul>Format Type: FORMAT_VideoInfo or GUID_NULL<br /> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | Major type: MEDIATYPE_VideoSubtype:<br /><ul><li>MEDIASUBTYPE_RGB8</li><li>MEDIASUBTYPE_RGB555</li><li>MEDIASUBTYPE_RGB565</li><li>MEDIASUBTYPE_RGB24</li><li>MEDIASUBTYPE_RGB32</li></ul>Format Type: FORMAT_VideoInfo<br /> | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | See previous table | 
| Property Page CLSID | None | 
| Executable | qdvd.dll | 
| <a href="merit.md">Merit</a> | Line 21 Decoder: MERIT_NORMALLine 21 Decoder 2: MERIT_NORMAL + 2<br /> | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Closed Captions and Teletext](closed-captions-and-teletext.md)
</dt> <dt>

[DVD Filter Graph Configuration](dvd-filter-graph-configuration.md)
</dt> </dl>

 

 




