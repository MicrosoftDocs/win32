---
title: To create an ALink in a topic that links to a target file
description: To create an ALink in a topic that links to a target file
ms.assetid: 5304EE18-0426-4f35-9A5A-3EA64E06E3AE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create an ALink in a topic that links to a target file

1.  Open the HTML file you want to link from, and then position your cursor at the location where you want to create an Associative link (ALink).
2.  Click **HTML Help ActiveX Control**.

    

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

3.  In the **Specify the command** box, click **ALink Search**, and then choose the appropriate display type and button options.
4.  In the **Related Topics** dialog box, specify the ALink names you want to jump to.
5.  For more information about ALinks, see the [HTML Help ActiveX control reference](alink.md).

## Notes

-   You must [add ALink names](to-add-an-alink-name-to-a-target-html-file.md) to the appropriate target topics before the ALink will work.
-   Adding an ALink to an HTML file adds an &lt;OBJECT&gt; tag to your file. This allows you to link to any other files that contain the ALink names you specify. When a user clicks the ALink, any topics that contain the ALink names you have specified will appear.
-   You can [test ALinks](to-test-klinks-or-alinks.md) in compiled help files.

## Related topics

<dl> <dt>

[About Working with Links](work-with-links.md)
</dt> </dl>

 

 





