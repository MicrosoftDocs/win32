---
title: Example Create an ALink Using a Text Link
description: Example Create an ALink Using a Text Link
ms.assetid: 814B5C5A-BB8F-4e21-818A-CE3CA7E3D9D9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example: Create an ALink Using a Text Link

1.  Open the HTML file in which you want to create an Associative link (ALink) as a text link.
2.  Click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

3.  In the **Specify the command** box, click **ALink Search** and, if you have already used the HTML Help ActiveX control in this file, enter an ID name for this instance of the control.
4.  Click **Next** and then click **Hidden** to specify that you will be scripting this use of the HTML Help ActiveX control.
5.  Select the appropriate display type options, and then add the ALink names you want to jump to.
6.  Position the cursor at the location where you want to create the link, and then copy the following tag into your file:
    ```
    <A HREF="JavaScript:hhctrl2.Click()">add link text here</A> 
    ```

    

7.  In this example, `hhctrl2` specifies 2 as the ID number for this instance of the HTML Help ActiveX control, which the **ALink Search** command should look for.

Replace "add link text here" with the words you want to use.

## Notes

-   For this example, the ALink name `example` was added to the beginning of the HTML file. When you click the text link, it jumps to all target files that contain `example` as an ALink name.
-   You can [test ALinks](to-test-klinks-or-alinks.md) in compiled help files.
-   For more information about ALinks, see the [HTML Help ActiveX control reference](alink.md).

## Related topics

<dl> <dt>

[About Working with Links](work-with-links.md)
</dt> </dl>

 

 





