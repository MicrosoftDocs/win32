---
title: About Structures
description: About Structures
ms.assetid: E75CA82E-9759-47d8-AF84-5842EDAB019D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Structures

The HTML Help API provides several objects that you work with using data structures.

When working with a structure, it is recommended that you use a Win32 function such as **ZeroMemory**, **memcpy**, or **memset** to clear out the address space of a structure that has been declared. This ensures that you start with a known quantity before making any modifications. For example, the following code fragment uses **memset** to make a copy of an [**HH\_WINTYPE**](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_wintype) structure:


```
HH_WINTYPE hhWinType;                   //Create new wintype.
            HH_WINTYPE *phhWinType;      //Create a pointer to this wintype.
            memset(phhWinType,           //Requires "memory.h" header be included in the calling application.
                  0,
                  sizeof(HH_WINTYPE));
            HtmlHelp(hwnd,
                    "c:\\help\\MyHelpFile.chm>main",
                    HH_GET_WIN_TYPE,
                    (DWORD)&amp;phhWinType);
            hhWinType = *phhWinType;    //Create a copy so we don't write directly.
```



> [!Note]  
> The Win32 functions such as **ZeroMemory**,**memcpy**, or **memset** do not make a deep copy of the structure. Developer-written copy constructors perform proper deep copies for OOP/C++ classes and objects.

 

### Structures quick reference



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>Structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Window types</td>
<td><ul>
<li>[<strong>HH_POPUP</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_popup)</li>
<li>[<strong>HH_WINTYPE</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_wintype)</li>
</ul></td>
</tr>
<tr class="even">
<td>ALink name/KLink keyword lookups</td>
<td><ul>
<li>[<strong>HH_AKLINK</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_aklink)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Notification messages</td>
<td><ul>
<li>[<strong>HHN_NOTIFY</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghhn_notify)</li>
<li>[<strong>HHNTRACK</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghhntrack)</li>
</ul></td>
</tr>
<tr class="even">
<td>Full-text search</td>
<td><ul>
<li>[<strong>HH_FTS_QUERY</strong>](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghh_fts_query)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Error tracking</td>
<td><ul>
<li>[<strong>HH_LAST_ERROR</strong>](hh-last-error-structure.md)</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[About the HTML Help API](html-help-api-overview.md)
</dt> </dl>

 

 




