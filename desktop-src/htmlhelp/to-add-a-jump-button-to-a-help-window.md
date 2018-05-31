---
title: To add a Jump button to a help window
description: To add a Jump button to a help window
ms.assetid: 7D19D981-58F9-459b-B08A-C7F8CE186781
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To add a Jump button to a help window

1.  Click **Add/Modify Window Definitions**, and then click the **Buttons** tab. 

    |                        |                                                                                                  |
    |------------------------|--------------------------------------------------------------------------------------------------|
    | ![](images/sb-adm.gif) | Adds or edits window definitions and the general appearance of the HTML Help Viewer. <br/> |

    

     

2.  In the **Window Type** box, click the window you want to add a Jump button to.
3.  Select the **Jump 1** check box, and then type a name for the button in the **Jump 1** text box.
4.  Click **OK**. The Resolve Window Definition Wizard will appear.
5.  Verify the window name, and then click **Next**.
6.  In the **Button name** box, type the name of the button again, and then, in the **Jump to File** box, enter a file name or HTTP address:
    -   If you want to link to a file in your help system, and the file is located in the same folder as your project (.hhp) file, you only need to type the file name.
    -   If you want to link to a Web site, you need to provide the full URL including the HTTP address for the site. For example, http://www.example.com.
7.  Click **Next**, and then click **Finish**.

## Notes

-   You can add two Jump buttons to a help window.
-   If you are linking to a file in your help system that is not in the same folder as your project file, you need to provide the relative path to the file. For example, If your topic file is located in a subfolder called Topics, you need to type Topics/Mytopic.htm.

## Related topics

<dl> <dt>

[About Adding Buttons to a Help Window](adding-buttons-to-a-help-window.md)
</dt> </dl>

 

 





