---
title: DWRITE\_RENDERING\_MODE enumerations
description: Starting in Windows 8, the DWRITE\_RENDERING\_MODE enumeration added new enumeration values and deprecated others.
ms.assetid: 3EA568B4-310D-4F70-9530-5916419282E5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DWRITE\_RENDERING\_MODE enumerations

Starting in Windows 8, the **DWRITE\_RENDERING\_MODE** enumeration added new enumeration values and deprecated others.

Starting in Windows 8, the [**DWRITE\_TEXT\_ANTIALIAS\_MODE**](/windows/win32/Dwrite_1/ne-dwrite_1-dwrite_text_antialias_mode?branch=master) enumeration determines whether text is rendered using ClearType. As a result, all the ClearType rendering modes in the **DWRITE\_RENDERING\_MODE** enumeration are deprecated. These enumeration values now map to new rendering modes.

The table here shows the old enumeration values and the new values they are mapped to. For descriptions of the new values, see [**DWRITE\_RENDERING\_MODE**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master).



| Old mode                                                                                | New mode                                                                                |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_GDI\_CLASSIC**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)       | [**DWRITE\_RENDERING\_MODE\_GDI\_CLASSIC**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)                  |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_GDI\_NATURAL**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)       | [**DWRITE\_RENDERING\_MODE\_GDI\_NATURAL**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)                  |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)            | [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)            |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL\_SYMMETRIC**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master) | [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL\_SYMMETRIC**](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master) |



 

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>DWRITE_RENDERING_MODE (Windows 8 and later)</strong>](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master)<br/></td>
<td>Represents a method of rendering glyphs. <br/>
<blockquote>
[!Note]<br />
This topic is about [<strong>DWRITE_RENDERING_MODE</strong>](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master) in Windows 8 and later. For info on the previous version see [<strong>this topic</strong>](/windows/win32/dwrite/?branch=master).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>DWRITE_RENDERING_MODE</strong>](/windows/win32/dwrite/?branch=master)<br/></td>
<td>Represents a method of rendering glyphs. <br/>
<blockquote>
[!Note]<br />
This topic is about [<strong>DWRITE_RENDERING_MODE</strong>](/windows/win32/dwrite/ne-dwrite-dwrite_rendering_mode?branch=master) previous to Windows 8 and later. For info on the newer version see <strong>this topic</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 





