---
title: To split topics in an HTML file
description: To split topics in an HTML file
ms.assetid: 6C2CD495-3868-4eb9-BE34-5AB402BECDF6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To split topics in an HTML file

1.  Open an HTML file.
2.  Position your cursor anywhere between the &lt;BODY&gt; start and end tags of the file, at the location where you want to create the new topic.
3.  On the **Edit** menu, click **Split File**.
4.  In the **New HTML file name** box, type a name for the new file.
5.  In the **New title** box, type a title for the new file.

## Notes

-   HTML Help Workshop splits the file during the compilation process. The basic &lt;BODY&gt;, &lt;HTML&gt;, and &lt;DOCTYPE&gt; tags will be added after each split. The &lt;TITLE&gt; tag will also be duplicated if you do not specify a new title for each file.
-   You can have multiple instances of the HTML Help ActiveX control in a single HTML file to split the file in multiple locations.
-   This feature can be used only with a compiled help (.chm) file.
-   The split HTML files do not appear in the \[FILES\] section of the project (.hhp) file. To create links to these files in any HTML file or in your table of contents, refer to the file names specified in **Split File**. These HTML files are accessible only from the master HTML file until after compilation.

## Related topics

<dl> <dt>

[About Creating HTML Topic Files](create-html-topic-files.md)
</dt> </dl>

 

 




