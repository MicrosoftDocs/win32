---
title: To assign a window type to a topic when linking
description: To assign a window type to a topic when linking
ms.assetid: C640549D-C058-467c-9B0D-FD1C8A43076A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To assign a window type to a topic when linking

1.  Define the appropriate [secondary window](to-add-a-secondary-window.md) type in the project file.
2.  Open the HTML file you are linking from and click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

3.  In the **Specify the command** box, click **Related Topics**, and then, if you have already used the HTML Help ActiveX control in this file, enter an ID name for this instance of the control.
4.  Click **Next**, and then, because you most likely do not want a button associated with the link text, click **Hidden** to specify that you will be scripting this use of the HTML Help ActiveX control.
5.  Click **Next**, click **Add**, and then enter the **Title** and **File/URL** information for the topic you are linking to.
6.  In the **Window** box, specify the name of the secondary window you want the topic to appear in. This name must match the name you gave the secondary window in the project file.
7.  Click **Next**, and then click **Finish**.
8.  Add the following JavaScript syntax to the file to create the text link:

    ```
    <A HREF=JavaScript:hhctrl.Click()>link</a> 
    ```

    

    where hhctrl is the ID for the instance of the control and link is the link text.

## Notes

-   For example, you could link to the file Apple.htm with the title "How to eat an apple" and have the topic appear in a wide window.
-   The link will not work until the file is compiled.
-   For more information about the control, see the [HTML Help ActiveX control reference](html-help-activex-control-reference.md).

## Related topics

<dl> <dt>

[About Creating Help Windows](create-help-windows.md)
</dt> </dl>

 

 





