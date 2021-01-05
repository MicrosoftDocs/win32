---
description: File Stream Renderer Filter
ms.assetid: e26462bb-e67f-4522-bec2-88378c4ff442
title: File Stream Renderer Filter
ms.topic: article
ms.date: 05/31/2018
---

# File Stream Renderer Filter

The File Stream Renderer filter renders file names that are parsed by the [Multi-File Parser](multi-file-parser-filter.md) filter. For more information, see the documentation for that filter.

The use of this filter is deprecated. To render multiple files within the same filter graph, the application should simply call **RenderFile** or **AddSourceFilter** multiple times.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></td>
</tr>
<tr class="even">
<td>Input pin media types</td>
<td><ul>
<li>Major type: MEDIATYPE_File</li>
<li>Subtype: GUID_NULL</li>
<li>Format type: MEDIATYPE_File</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input pin interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output pin media types</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Output pin interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-istreambuilder"><strong>IStreamBuilder</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_FileRend</td>
</tr>
<tr class="odd">
<td>Executable</td>
<td>Quartz.dll</td>
</tr>
<tr class="even">
<td><a href="merit.md">Merit</a></td>
<td>MERIT_UNLIKELY</td>
</tr>
<tr class="odd">
<td><a href="filter-categories.md">Filter Category</a></td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

The filter's CLSID is not defined in Uuids.h. Use this macro in your own header file:


```C++
// {D51BD5A5-7548-11cf-A520-0080C77EF58A}
DEFINE_GUID(CLSID_FileRend,
0xd51bd5A5, 0x7548, 0x11cf, 0xa5, 0x20, 0x0, 0x80, 0xc7, 0x7e, 0xf5, 0x8a);
```



## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



