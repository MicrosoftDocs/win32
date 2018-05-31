---
title: To speed up the HTML Help Java Applet download time
description: To speed up the HTML Help Java Applet download time
ms.assetid: C3FEEB4E-6386-479b-8F3E-F23FDFF41C95
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To speed up the HTML Help Java Applet download time

1.  Place all the required class and image files into a cabinet (.cab) file if Microsoft Internet Explorer is the target browser, or a .zip file if Netscape Navigator is the target browser.
2.  Use the following syntax:

    ```
    <APPLET archive="HHCtrl.zip" code="HHCtrl.class" width=200 height=200 codebase="code base">
    <PARAM name="Command" value="command type">
    <PARAM name="Item1" value="text data">
    <PARAM name="Cabbase" value="HHCtrl.cab">
    </APPLET> 
    ```

    

## Notes

-   Microsoft Internet Explorer lets you specify a CABBASE parameter with the name of a .cab file. A .cab file is a compressed archive containing your class files.
-   Netscape Navigator uses an ARCHIVE parameter with the &lt;APPLET&gt; tag, and an uncompressed .zip file as an archive.

## Related topics

<dl> <dt>

[About the HTML Help Java Applet](about-the-html-help-java-applet.md)
</dt> </dl>

 

 




