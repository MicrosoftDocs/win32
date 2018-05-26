---
Description: Infinite Pin Tee Filter
ms.assetid: 5f3e06ec-adee-4bc7-8ea8-cce3030d3baa
title: Infinite Pin Tee Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Infinite Pin Tee Filter

This filter delivers samples delivered to its input pin to a variable number of output pins. When an instance of the filter is created, it has one output pin. Each time an output pin is connected, the filter creates another output pin. All output pins share the same media type as the input pin.

A version of this filter is also provided as an SDK sample. See [InfTee Filter Sample](inftee-filter-sample.md).



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)                                                                                                                 |
| Input Pin Media Types                    | Any media type                                                                                                                                     |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                             |
| Output Pin Media Types                   | Any media type. The output type always matches the input type, for all output pins                                                                 |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) |
| Filter CLSID                             | CLSID\_InfTee                                                                                                                                      |
| Property Page CLSID                      | No property page                                                                                                                                   |
| Executable                               | qcap.dll                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



