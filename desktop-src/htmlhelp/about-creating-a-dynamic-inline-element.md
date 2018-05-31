---
title: About Creating a Dynamic Inline Element
description: About Creating a Dynamic Inline Element
ms.assetid: A0542E3F-668A-43ea-B8A0-2D2B6126A3F3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Creating a Dynamic Inline Element

Although &lt;DIV&gt; and &lt;SPAN&gt; tags are usually used for page layout purposes, you can also use them to make unique links. For example, we created the following dynamic link for the topic links on our home pages:


```JScript
function liteGo(spNo){
spNo.style.background="#00cc33";
spNo.style.color="#FFFFFF";
}
function liteOff(spNo){
spNo.style.background="transparent";
spNo.style.color="#000000";
}
```



There are three steps to creating a dynamic element:

1.  [Insert the tag for an instance of the section](to-insert-the-tag-for-an-instance-of-the-section.md)
2.  [Insert the JavaScript code](to-insert-the-javascript-code.md)
3.  [Update your style sheet to reflect the new section](to-update-your-style-sheet.md)

> [!Note]  
> When you use the &lt;SPAN&gt; tag inline with text, including other items in the span (such as graphics) limits the span's minimum height to 12 points.

 

## Related topics

<dl> <dt>

[Create Dynamic Links](example--create-dynamic-elements-with-dhtml.md)
</dt> </dl>

 

 




