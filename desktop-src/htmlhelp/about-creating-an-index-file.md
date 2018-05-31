---
title: About Creating an Index File
description: About Creating an Index File
ms.assetid: A010B31E-D397-4051-9645-DEDFC9D2F1E0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Creating an Index File

The index file you create in HTML Help Workshop is an HTML file that uses a site map and can be added to a Web site. If you choose to include it as part of a compiled help (.chm) file, the compiler will compress the site map and create a binary index, which takes up less space.

There are some important [differences between binary and site map index files](the-difference-between-binary-and-site-map-indexes.md) that can help you decide which type you want to use.

### Notes

-   If you are designing a help system using the [Help Viewer](using-the-help-viewer-for-topics.md), adding an index file to your help project will also create the [Index](index.md) tab in the left pane of the Help Viewer after the project is compiled.
-   If you are designing for a Web site or your own frameset, make sure you [add the HTML Help ActiveX control](inserting-the-html-help-activex-control.md) to the appropriate files and [specify a default frame](to-specify-the-default-frame-in-a-contents-or-index-file.md) to display your index file.

## Related topics

<dl> <dt>

[Create an Index](create-an-index-file.md)
</dt> </dl>

 

 




