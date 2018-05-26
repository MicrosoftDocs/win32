---
title: Creating an Index for a Web Site
description: Creating an index for use as a navigational aid on a Web site is similar to creating an index for use in a compiled help file. This procedure describes the extra steps you must take to make the index usable over the Web.
ms.assetid: 92D669A0-0BB2-4a37-BC19-6F466C23A0B0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating an Index for a Web Site

Creating an index for use as a navigational aid on a Web site is similar to creating an index for use in a compiled help file. This procedure describes the extra steps you must take to make the index usable over the Web.

## To create an index for a Web site

1.  [Create an index file](creating-an-index-file.md).
2.  [Create the HTML file](to-create-a-new-html-file.md) that will contain your index.
3.  Place your cursor at the location where you want the index file to appear, and then click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                          |
    |------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file. <br/> |

    

     

4.  In the **Specify the command** box, click **Index**, and then follow the instructions on your screen.

## Notes

-   Because an index created for a Web site is not compiled, it should be created using a [site map](to-create-an-index-that-uses-a-site-map.md).
-   If your users do not have a browser that supports ActiveX controls, try using the [HTML Help Java applet](about-the-html-help-java-applet.md).
-   For more information about the [Index](index.md) command, see the HTML Help ActiveX control reference.

## Related topics

<dl> <dt>

[About Creating Index Files](create-an-index-file.md)
</dt> </dl>

 

 





