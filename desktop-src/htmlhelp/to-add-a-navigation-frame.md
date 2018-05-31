---
title: To add a navigation frame
description: To add a navigation frame
ms.assetid: AF2386E5-A44B-4f06-A2C0-6CF24F9E0CBA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To add a navigation frame

1.  On the **File** menu, click **New**, and then click **HTML File**.
2.  Enter a title for your file.
3.  Within the &lt;BODY&gt; start and end tags, type:
    ```
    <object type="text/site properties"> <param name="FrameName" value="right"> </object> 
    ```

    

4.  Click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

5.  In the **Specify the command** box, click **Table of Contents**, and then click **Next**.
6.  In the **Location of .hhc file** box, specify where the contents file is located. Do not specify an **Image Bitmap** or change the **Height** or **Width** values.
7.  Click **Next** twice, and then click **Finish**. Do not specify any **Window styles**.
8.  Save the file as **left.htm**, so that it matches the name you gave when you created frames.htm.

## Related topics

<dl> <dt>

[Step 3: Add a Default Frame Location to the Table of Contents File](to-add-a-default-frame-location-to-the-table-of-contents-file.md)
</dt> </dl>

 

 





