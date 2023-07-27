---
description: Filter Mapper
ms.assetid: cb8f25b3-a0f0-48fa-843f-88a5a5d17019
title: Filter Mapper
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Filter Mapper

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Filter Mapper searches the registry for registered filters. The Filter Graph Manager uses this component to build filter graphs. Applications can use it to find filters that match specified search criteria. Create this object by calling **CoCreateInstance**.




| Label | Value |
|--------|-------|
| Class Identifier | CLSID_FilterMapper2 | 
| Interfaces | <ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2"><strong>IFilterMapper2</strong></a></li><li><a href="iamfilterdata.md"><strong>IAMFilterData</strong></a> (deprecated)</li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ifiltermapper3"><strong>IFilterMapper3</strong></a> (deprecated)</li></ul> | 




 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Using the Filter Mapper](using-the-filter-mapper.md)
</dt> </dl>

 

 



