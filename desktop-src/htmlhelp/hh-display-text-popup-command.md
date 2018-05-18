---
title: HH\_DISPLAY\_TEXT\_POPUP command
description: HH\_DISPLAY\_TEXT\_POPUP command
ms.assetid: '58FDF707-F628-4e41-9994-8B00FD1B00DB'
---

# HH\_DISPLAY\_TEXT\_POPUP command

Opens a pop-up window that displays the contents of one of the following:

-   An explicit text string.
-   A text string based on a resource ID.
-   A text string ID based on a text file contained in a compiled help (.chm) file.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><em>pszFile</em></th>
<th><em>dwData</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>To use an explicit text string:
<ul>
<li>Specify a NULL value.</li>
</ul>
To use a text string from a resource: <br/>
<ul>
<li>Specify a NULL value.</li>
</ul>
To use text string from a text file contained in a compiled help file: <br/>
<ul>
<li>Specify the .chm file and the text file within the .chm file.</li>
</ul></td>
<td>Specifies a pointer to an [<strong>HH_POPUP</strong>](hh-popup-structure.md) structure.</td>
</tr>
</tbody>
</table>



 

## Example


```
HtmlHelp(
         hwndCTRL,
         NULL,
         HH_DISPLAY_TEXT_POPUP,
         (DWORD_PTR)&amp;popup) ;
```



## Return Value

The handle (hwnd) of the pop-up window.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_TP\_HELP\_CONTEXTMENU](hh-tp-help-contextmenu-command.md)
</dt> <dt>

[HH\_TP\_HELP\_WM\_HELP](hh-tp-help-wm-help-command.md)
</dt> </dl>

 

 





