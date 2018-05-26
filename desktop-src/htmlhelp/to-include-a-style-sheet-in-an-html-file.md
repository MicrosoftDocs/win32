---
title: To include a style sheet in an HTML file
description: To include a style sheet in an HTML file
ms.assetid: A5E82D4C-BC78-48b5-BD11-32189476FDEC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To include a style sheet in an HTML file

-   Open each HTML file you want to contain the style sheet, and add the style information between the &lt;HEAD&gt; start and end tags using the &lt;STYLE&gt; tag.

Here is an example of a style sheet created this way:


```
<STYLE>
BODY {
font-family: times, serif;
color: black;
margin-left: 10%;
margin-right: 10%;
}
A:link {
color: black;
text-decoration: underline;
}
A:visited {
color: black;
text-decoration: none;
}
</STYLE>
```



## Related topics

<dl> <dt>

[About Using Cascading Style Sheets](use-cascading-style-sheets.md)
</dt> </dl>

 

 




