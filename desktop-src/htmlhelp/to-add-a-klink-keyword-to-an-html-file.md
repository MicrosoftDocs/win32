---
title: To add a KLink keyword to an HTML file
description: To add a KLink keyword to an HTML file
ms.assetid: 2B6CA051-5A12-4c44-A046-14C231A8B194
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To add a KLink keyword to an HTML file

1.  Open an HTML file.
2.  Position your cursor anywhere between the &lt;BODY&gt; start and end tags of the file, at the location where you want to add the keywords.
3.  On the **Edit** menu, click **Compiler Information**, and then click **Keywords**.
4.  Click **Add**, and then specify any keywords you want to insert into the file. You can add multiple keywords by separating each name with a semicolon.

## Notes

-   To use KLinks, your help project must be set up to [include keywords from HTML files](to-generate-keywords-from-html-files.md).
-   Inserting a KLink adds an &lt;OBJECT&gt; tag to your HTML file. The file can now be a target file, and you can [create a KLink](to-create-a-klink-in-an-html-file-to-a-keyword-in-a-target-file.md) from another HTML file to it.
-   Index files created using the site map method do not support KLinks.
-   You can [test KLinks](to-test-klinks-or-alinks.md) in compiled help files.
-   For more information about KLinks, see the [HTML Help ActiveX control reference](klink.md).

## Related topics

<dl> <dt>

[About Working with Links](work-with-links.md)
</dt> </dl>

 

 




