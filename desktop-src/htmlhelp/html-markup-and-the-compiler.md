---
title: HTML Markup and the Compiler
description: HTML Markup and the Compiler
ms.assetid: E047A78C-2310-421a-B8B6-3426C02B2A1E
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTML Markup and the Compiler

HTML Help Workshop inserts HTML markup into topic files when you [split an HTML file](about-splitting-topics-in-an-html-file.md), or insert [Associative link (ALink) names](to-add-an-alink-name-to-a-target-html-file.md) or [Keyword link (KLink) keywords](to-add-a-klink-keyword-to-an-html-file.md) into HTML files. This markup information is used by the compiler to enable those features.

For example, this information enables ALinks added to HTML files to be resolved with their targets during compilation, allowing the user to click the ALink and see a list of topics.

The markup information is only used in compiled help (.chm) files. It includes a special CLASSID attribute that is referenced by the HTML Help compiler.

## Notes

-   If you use the **Split File** command, insert an ALink name, or insert a KLink keyword into an uncompiled HTML file, it will be ignored by the Web browser.
-   HTML markup appears inside an **&lt;OBJECT&gt;** tag, which is not to be confused with the **&lt;OBJECT&gt;** tag used by the HTML Help ActiveX control.

## Related topics

<dl> <dt>

[About Compiling a Help Project](compile-a-help-project.md)
</dt> </dl>

 

 




