---
title: BDA Network Provider Filter
description: BDA Network Provider Filter
ms.assetid: 'f5de924f-defe-4300-a347-c9d63271dc90'
---

# BDA Network Provider Filter

The BDA Network Provider is the source filter for any digital television filter graph based on Microsoft Broadcast Driver Architecture (BDA). The following Network Provider filter is available. The Microsoft Network Provider Filter supports all legacy network providers.

| Network Provider           | CLSID                  |
|----------------------------|------------------------|
| Microsoft Network Provider | CLSID\_NetworkProvider |



 

**Windows Server 2008, Windows Vista and earlier:** The following Network Provider filters are also available.

| Network Provider                              | CLSID                      |
|-----------------------------------------------|----------------------------|
| Microsoft ATSC Network Provider (Deprecated)  | CLSID\_ATSCNetworkProvider |
| Microsoft DVB-C Network Provider (Deprecated) | CLSID\_DVBCNetworkProvider |
| Microsoft DVB-S Network Provider (Deprecated  | CLSID\_DVBSNetworkProvider |
| Microsoft DVB-T Network Provider (Deprecated) | CLSID\_DVBTNetworkProvider |



 

The information in the following table applies to all of these filters:



|                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                          | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526), [**IBDA\_EthernetFilter**](ibda-ethernetfilter.md), [**IBDA\_NetworkProvider**](ibda-networkprovider.md), [**IBDA\_TIF\_REGISTRATION**](ibda-tif-registration.md), [**IBDA\_IPV4Filter**](ibda-ipv4filter.md), [**IBDA\_IPV6Filter**](ibda-ipv6filter.md), [**IFrequencyMap**](ifrequencymap.md), [**IMPEG2\_TIF\_CONTROL**](impeg2-tif-control.md), [**IScanningTuner**](iscanningtuner.md), [**ITuner**](ituner.md) |
| Input Pin Media Types                      | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Input Pin Interfaces                       | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output Pin Media Types                     | Major type: KSDATAFORMAT\_TYPE\_BDA\_ANTENNA                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output Pin Interfaces                      | [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)                                                                                                                                                                                                                                                                                                                                                                                                 |
| Filter CLSID                               | See previous table.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Filter Category](https://msdn.microsoft.com/library/windows/desktop/dd375655) | KSCATEGORY\_BDA\_NETWORK\_PROVIDER                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

## Remarks

The Network Provider acts as the default tuner in a BDA filter graph, by exposing the [**ITuner**](ituner.md) interface. No signals or data actually pass through this filter. It works closely with the Transport Information Filter (TIF) and the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) to acquire transport streams and route the elementary stream to the appropriate downstream filters.

If you are creating a digital TV graph manually (rather than using the Video Control), use **CoCreateInstance** and [**IFilterGraph::AddFilter**](https://msdn.microsoft.com/library/windows/desktop/dd390016) to add this filter to the graph. The [**ICaptureGraphBuilder2**](https://msdn.microsoft.com/library/windows/desktop/dd376359) interface does not automatically add this filter to the graph.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 




