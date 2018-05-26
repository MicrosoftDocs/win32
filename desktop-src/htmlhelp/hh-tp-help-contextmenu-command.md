---
title: HH\_TP\_HELP\_CONTEXTMENU command
description: Opens a pop-up context menu. Generally used in response to the Windows WM\_CONTEXTMENU message. For example, this message is sent when a user right-clicks a dialog box control.
ms.assetid: 4C222E07-C647-40e6-85DB-A8F8AAB940ED
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HH\_TP\_HELP\_CONTEXTMENU command

Opens a pop-up context menu. Generally used in response to the Windows **WM\_CONTEXTMENU** message. For example, this message is sent when a user right-clicks a dialog box control.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><em>hwndCaller</em></th>
<th><em>pszFile</em></th>
<th><em>dwData</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Specifies the window handle of the dialog box control for which you want pop-up help to appear. This is typically the control that has focus.</td>
<td>Specifies the compiled help (.chm) file, and the text file that contains the pop-up help topics. By default, the text file is named Cshelp.txt. If Cshelp.txt is located in the root of the compiled help file, then you only need to specify the help file name. If not, you must also specify the relative path.<br/></td>
<td>Specifies an array of DWORDs containing pairs of dialog box control IDs and help topic IDs. The array must be terminated by zero. If a control does not require pop-up help, specify -1 for the help topic ID.
<pre data-space="preserve"><code>DWORD ids[5] ;
     ids[0] = ControlID1 ;
     ids[1] = HelpID1 ;
     ids[2] = ControlID2 ;
     ids[3] = -1 ;
     ids[4] = 0 ; </code></pre></td>
</tr>
</tbody>
</table>



 

## Example


```
HtmlHelp(
         hwndCTRL,
         "c:\\myHelp.chm::/popups\cshelp.txt",
         HH_TP_HELP_CONTEXTMENU,
         (DWORD) ids) ;
```



## Remarks

-   The text (.txt) file that contains the pop-up help topics must be included in the \[TEXT POPUPS\] section of your project (.hhp) file.
-   **HH\_TP\_HELP\_CONTEXTMENU** does not display the What's This? menu. It does the exact same thing as **HH\_TP\_HELP\_WM\_HELP**.
-   **HH\_TP\_HELP\_CONTEXTMENU** is very similar to the WinHelp **HELP\_CONTEXTMENU***uCommand* parameter.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_DISPLAY\_TEXT\_POPUP](hh-display-text-popup-command.md)
</dt> <dt>

[HH\_TP\_HELP\_WM\_HELP](hh-tp-help-wm-help-command.md)
</dt> </dl>

 

 





