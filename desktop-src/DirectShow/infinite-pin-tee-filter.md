---
Description: Infinite Pin Tee Filter
ms.assetid: '5f3e06ec-adee-4bc7-8ea8-cce3030d3baa'
title: Infinite Pin Tee Filter
---

# Infinite Pin Tee Filter

This filter delivers samples delivered to its input pin to a variable number of output pins. When an instance of the filter is created, it has one output pin. Each time an output pin is connected, the filter creates another output pin. All output pins share the same media type as the input pin.

A version of this filter is also provided as an SDK sample. See [InfTee Filter Sample](inftee-filter-sample.md).



|                                          |                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](ibasefilter.md)                                                                                                                 |
| Input Pin Media Types                    | Any media type                                                                                                                                     |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                             |
| Output Pin Media Types                   | Any media type. The output type always matches the input type, for all output pins                                                                 |
| Output Pin Interfaces                    | [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
| Filter CLSID                             | CLSID\_InfTee                                                                                                                                      |
| Property Page CLSID                      | No property page                                                                                                                                   |
| Executable                               | qcap.dll                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



