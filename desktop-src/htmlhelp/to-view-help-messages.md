---
title: To view help messages
description: To view help messages
ms.assetid: 27121FF2-A7C2-4c39-8055-EF6B4430AD4E
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To view help messages

1.  In HTML Help Workshop on the **View** menu, click **HTML Help Messages**.
2.  Open the application you are testing, and use context-sensitive help.
3.  A message will appear for each API call that is sent in response to context-sensitive help.
4.  To save the messages in a text file, click **Save File** on the **File** menu in HTML Help Workshop.

## Example help message text

``` syntax
HH_TP_HELP_WM_HELP/HH_TP_HELP_CONTEXTMENU: Control id = 1035, Help id = 1000, File = htmlhelp.chm::/cxthelp/wintype.txt.
HH_TP_HELP_WM_HELP/HH_TP_HELP_CONTEXTMENU: Control id = 1041, Help id = 1001, File = htmlhelp.chm::/cxthelp/wintype.txt.
```

## Notes

-   To see an example of context-sensitive help in HTML Help Workshop, do step one (above), and then: open a project (.hhp) file, click **Add/Modify Window Definitions**. If you have not defined any already, add a new window type. Click the question mark in the upper-right corner of the dialog box, and then click a control. Note the text that appears in the View Messages window. 

    |                        |                                                                                                  |
    |------------------------|--------------------------------------------------------------------------------------------------|
    | ![](images/sb-adm.gif) | Adds or edits window definitions and the general appearance of the HTML Help Viewer. <br/> |

    

     

-   When viewing help messages, you can [clear the message log at any time](to-clear-help-messages.md).
-   This feature only displays help messages associated with the HTML Help API. Messages for interface elements such as the **OK** and **Cancel** buttons will not appear, since they are part of the Windows API.

## Related topics

<dl> <dt>

[About Testing a Help System](test-a-help-system.md)
</dt> </dl>

 

 





