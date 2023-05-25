---
description: WST Decoder Filter
ms.assetid: 2d33ae3f-565d-4e69-8fb0-117ff582a4d0
title: WST Decoder Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WST Decoder Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This component has been removed from Windows Vista and later operating systems. It is available for use in the Windows XP and Windows Server 2003 operating systems.

> [!Note]  
> Starting in Windows Vista, DirectShow does not provide a filter to decode World Standard Teletext (WST).

 

The WST Decoder is a kernel-mode filter that accepts decoded World Standard Teletext data from the [WST Codec](wst-codec-filter.md) and delivers the bitmaps to Pin 2 on the [Overlay Mixer](overlay-mixer-filter.md) using fonts supplied by Microsoft. Only Western European languages are supported at this time; no Unicode fonts are currently provided.

This filter can be added to the graph automatically by calling [**ICaptureGraphBuilder2::RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream), using the output pin of the WST Codec.



| Label | Value |
|------------------------------------------|---------------------------------------------------------------|
| Filter Interfaces                        | ISpecifyPropertyPages, [**IAMWstDecoder**](/previous-versions/windows/desktop/api/Iwstdec/nn-iwstdec-iamwstdecoder) |
| Input Pin Media Types                    | MEDIATYPE\_VBI, MEDIASUBTYPE\_TELETEXT                        |
| Input Pin Interfaces                     | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)                                          |
| Output Pin Media Types                   | MEDIATYPE\_Video                                              |
| Output Pin Interfaces                    | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)                                          |
| Filter CLSID                             | CLSID\_WSTDecoder                                             |
| Property Page CLSID                      | CLSID\_WstDecoderPropertyPage                                 |
| Executable                               | Wstdecod.DLL                                                  |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                 |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                 |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Viewing World Standard Teletext](viewing-world-standard-teletext.md)
</dt> </dl>

 

 



