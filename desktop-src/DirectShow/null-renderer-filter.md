---
description: The Null Renderer filter is a renderer that discards every sample it receives, without displaying or rendering the sample data.
ms.assetid: 2954762d-2ae6-4e38-ac88-5390a081897e
title: Null Renderer Filter (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Null Renderer Filter
api_type: 
- HeaderDef
api_location: 
- Qedit.h
ms.custom: UpdateFrequency5
---

# Null Renderer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Null Renderer filter is a renderer that discards every sample it receives, without displaying or rendering the sample data.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) |
| Input pin media types                    | Any media type                                                                                                       |
| Input pin interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)               |
| Output pin media types                   | Not applicable.                                                                                                      |
| Output pin interfaces                    | Not applicable.                                                                                                      |
| Filter CLSID                             | CLSID\_NullRenderer                                                                                                  |
| Property Page CLSID                      | No property page.                                                                                                    |
| Executable                               | Qedit.dll                                                                                                            |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                  |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                        |



 

## Remarks

Use this filter when an output pin in the graph requires a downstream connection, but you do not wish to render the data from that pin. By connecting the output pin to the Null Renderer, you complete the connection without rendering the data.

Even though this filter does not render any samples, it does wait for each sample's presentation time before discarding the sample. Therefore, the graph will run at the normal rate. If you want the graph the run as quickly as possible, set the reference clock to **NULL**. For more information, see [Setting the Graph Clock](setting-the-graph-clock.md).

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Editing Services Objects](directshow-editing-services-objects.md)
</dt> </dl>

 

 




