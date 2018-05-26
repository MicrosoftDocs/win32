---
title: To create a link to a command without using a button
description: To create a link to a command without using a button
ms.assetid: 76FA0718-4A64-4ca4-B6FD-E8F35F833A11
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create a link to a command without using a button

1.  Open the HTML file in which you want to have the Related Topics link, Associative link (ALink), Keyword link (KLink), Shortcut, Close window, HTML Help ActiveX control version dialog box, or WinHelp topic appear.
2.  Click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

3.  In the **Specify the command** box, click a command. You must enter the ID name to use for this instance of the HTML Help ActiveX control because you will use scripting to access the command.
4.  Click **Next**, and then click **Hidden** to specify that you will be scripting this use of the control.
5.  Select the appropriate display type and button options, and then add the ALink names you want to jump to.
6.  Add the appropriate JavaScript to the HTML file to create a text, graphic, or other link to the control.

## Note

-   This procedure can be used with any of the HTML Help ActiveX control commands that provide a button by default. It is useful, for example, when you want to create a Related Topics link, KLink, or ALink in an HTML file [using a text link](create-a-text-link-for-html-help-activex-control-commands.md). Instead of clicking a button, the user clicks the text link.
-   For more information about commands, see the [HTML Help ActiveX control reference](about-commands.md).

## Related topics

<dl> <dt>

[About Working with Links](work-with-links.md)
</dt> </dl>

 

 





