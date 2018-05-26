---
title: To apply a style to a phrase in an HTML file
description: To apply a style to a phrase in an HTML file
ms.assetid: 16E33620-07B8-4895-81BD-7BE6130AF6A3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To apply a style to a phrase in an HTML file

In the HTML file, select the phrase you want to apply special formatting to.

Add the &lt;SPAN&gt; tag and the &lt;STYLE&gt; tag attributes you want. For example:


```
<SPAN STYLE= "{
font-family: times;
font-size: 12pt;
background: yellow;
color: red;
}">
Span this phrase</SPAN>
```



In this example, the font, and background &lt;STYLE&gt; tag attributes will be applied to the text Span this phrase.

> [!Note]  
> This allows a help author to format individual phrases, words, or letters.

 

## Related topics

<dl> <dt>

[About Using Cascading Style Sheets](use-cascading-style-sheets.md)
</dt> </dl>

 

 




