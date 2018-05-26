---
Description: The Null Renderer filter is a renderer that discards every sample it receives, without displaying or rendering the sample data.
ms.assetid: 2954762d-2ae6-4e38-ac88-5390a081897e
title: Null Renderer Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Null Renderer Filter

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Null Renderer filter is a renderer that discards every sample it receives, without displaying or rendering the sample data.



|                                          |                                                                                                                      |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) |
| Input pin media types                    | Any media type                                                                                                       |
| Input pin interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)               |
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



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Editing Services Objects](directshow-editing-services-objects.md)
</dt> </dl>

 

 




