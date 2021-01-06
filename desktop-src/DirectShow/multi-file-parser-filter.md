---
description: Multi-File Parser Filter
ms.assetid: 8ef06f49-fda4-49e2-9b07-70453a2e897c
title: Multi-File Parser Filter
ms.topic: article
ms.date: 05/31/2018
---

# Multi-File Parser Filter

The Multi-File Parser filter parses a simple file format that enables multiple file names to be specified as though they were one file. These files have the format shown in the following example:


```C++
;MULTI
https://server/share/video.mpg
https://server/share/captions.smi
```



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
<li>Major type: MEDIATYPE_Stream</li>
<li>Subtype: CLSID_MultFile</li>
<li>Format type: GUID_NULL</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input pin interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Output pin media types</td>
<td><ul>
<li>Major type: MEDIATYPE_File</li>
<li>Subtype: GUID_NULL</li>
<li>Format type: MEDIATYPE_File</li>
</ul></td>
</tr>
<tr class="odd">
<td>Output pin interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_MultFile</td>
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

The filter creates one output pin for each file listed in the source file. The output type is MEDIATYPE\_File, and the format block for the output type is a wide-character string that contains the file name. Each pin connects to an instance of the [File Stream Renderer](file-stream-renderer-filter.md) filter. The File Stream Renderer filter creates one output pin, which exposes the [**IStreamBuilder**](/windows/desktop/api/Strmif/nn-strmif-istreambuilder) interface. The output pin renders the specified file. No media data travels between the Multi-File Parser and the File Stream Renderer.

The filter's CLSID is not defined in Uuids.h. Use this macro in your own header file:


```C++
// {D51BD5A3-7548-11cf-A520-0080C77EF58A}
DEFINE_GUID(CLSID_MultFile,
0xd51bd5a3, 0x7548, 0x11cf, 0xa5, 0x20, 0x0, 0x80, 0xc7, 0x7e, 0xf5, 0x8a);
```



## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



