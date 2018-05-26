---
Description: Filter Mapper
ms.assetid: cb8f25b3-a0f0-48fa-843f-88a5a5d17019
title: Filter Mapper
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filter Mapper

The Filter Mapper searches the registry for registered filters. The Filter Graph Manager uses this component to build filter graphs. Applications can use it to find filters that match specified search criteria. Create this object by calling **CoCreateInstance**.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Class Identifier</td>
<td>CLSID_FilterMapper2</td>
</tr>
<tr class="even">
<td>Interfaces</td>
<td><ul>
<li>[<strong>IFilterMapper2</strong>](/windows/win32/Strmif/nn-strmif-ifiltermapper2?branch=master)</li>
<li>[<strong>IAMFilterData</strong>](iamfilterdata.md) (deprecated)</li>
<li>[<strong>IFilterMapper3</strong>](/windows/win32/Strmif/nn-strmif-ifiltermapper3?branch=master) (deprecated)</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Using the Filter Mapper](using-the-filter-mapper.md)
</dt> </dl>

 

 



