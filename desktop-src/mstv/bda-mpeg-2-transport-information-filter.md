---
title: BDA MPEG-2 Transport Information Filter
description: BDA MPEG-2 Transport Information Filter
ms.assetid: 22044a4c-480f-4c98-a78e-52c66a5eac99
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BDA MPEG-2 Transport Information Filter

Digital TV transmissions multiplex many programs and their related elementary streams (such as audio, video, IP data) in a single transport stream. So that a receiver can properly acquire all the elementary streams related to a specific program and so that a receiver can tell what programs are contained in the stream, the transport stream will also contain many sets of tables that act as a catalog of information contained in the transport stream. Under direction of the [BDA Network Provider](bda-network-provider-filter.md), the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) delivers these tables to the Transport Information Filter. The Transport Information Filter then parses these tables and provides the information to the Network Provider so that it can control the other receiver filters in the graph.

This filter also provides COM interfaces that enable a Guide Store loader application to retrieve in-band EPG information.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>[<strong>IBaseFilter</strong>](https://msdn.microsoft.com/library/windows/desktop/dd389526), <strong>IConnectionPointContainer</strong>, [<strong>IGuideData</strong>](iguidedata.md), [<strong>IPSITables</strong>](/windows/desktop/api/mpeg2psiparser/nn-mpeg2psiparser-ipsitables), [<strong>ITuneRequestInfo</strong>](itunerequestinfo.md)</td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major type: MEDIATYPE_MPEG2_SECTIONS<br/> Subtypes:<br/>
<ul>
<li>MEDIASUBTYPE_ATSC_SI</li>
<li>MEDIASUBTYPE_DVB_SI</li>
<li>MEDIASUBTYPE_ISDB_SI</li>
</ul>
Format type: None<br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IPin</strong>](https://msdn.microsoft.com/library/windows/desktop/dd390397)</td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>Not applicable</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>Not applicable</td>
</tr>
<tr class="odd">
<td>[Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)</td>
<td>MERIT_NORMAL</td>
</tr>
<tr class="even">
<td>[Filter Category](https://msdn.microsoft.com/library/windows/desktop/dd375655)</td>
<td>KSCATEGORY_BDA_TRANSPORT_INFORMATION</td>
</tr>
</tbody>
</table>



 

## Remarks

Currently, the [**IGuideData**](iguidedata.md) interface is available only for DVB broadcasts. For other types, the filter returns E\_NOINTERFACE when queried for the interface.

This filter supports event notifications through the [**IGuideDataEvent**](iguidedataevent.md) connection point interface. To set up the event sink, use the **IConnectionPointContainer** interface on the filter.

## Related topics

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 





