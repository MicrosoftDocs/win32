---
description: Internal Script Command Renderer Filter
ms.assetid: 264cc7c3-987c-4832-85a2-087278a4d024
title: Internal Script Command Renderer Filter
ms.topic: article
ms.date: 05/31/2018
---

# Internal Script Command Renderer Filter

Receives script commands and dispatches them to the application.

This filter accepts script commands in one of two formats:

-   MEDIATYPE\_Text: Each media sample contains an ANSI text string.
-   MEDIATYPE\_ScriptCommand: Each media sample contains two NULL-terminated Unicode strings, concatenated together. The first string describes the command type and the second string is the script command.

    When the filter receives a sample, it sends an [**EC\_OLE\_EVENT**](ec-ole-event.md) event notification. The first event parameter is a **BSTR** with the command type, or `Text` if the format is MEDIATYPE\_Text. The second event parameter is a **BSTR** with the script command. The application can retrieve the event and respond to the script command.

For an example of how to use this filter, see [SAMI (CC) Parser](sami--cc--parser-filter.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td><ul>
<li>MEDIATYPE_ScriptCommand, MEDIASUBTYPE_NULL</li>
<li>MEDIATYPE_Text, MEDIASUBTYPE_NULL</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
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
<td>{48025243-2D39-11CE-875D-00608CB78066}</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>No property page</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Quartz.dll</td>
</tr>
<tr class="odd">
<td><a href="merit.md">Merit</a></td>
<td>MERIT_PREFERRED + 1</td>
</tr>
<tr class="even">
<td><a href="filter-categories.md">Filter Category</a></td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



