---
title: To insert the tag for an instance of the section
description: To insert the tag for an instance of the section
ms.assetid: 32CE3648-30F1-4e97-991B-7A6C8C1A4525
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To insert the tag for an instance of the section

Insert the following tag in an HTML file at the location where you want the section to appear:


```
<a href="<i>filename.htm</i>" onmouseover="<i>functionOn(id1)</i>" onmouseout="<i>functionOff(id1)</i>">
<span ID="<i>id1</i>" class="<i>classname</i>">GO</span></a>
```



Where filename.htm is the name of the HTML file to which you want to link, functionOn is the name of the JavaScript function that is triggered when a user moves their cursor over the section, and functionOff is the name of the JavaScript function that is triggered when the user's cursor moves out of the section. id1 is the ID for this instance of the &lt;SPAN&gt;, and classname is the style class.

## Example

The following is a tag used for the dynamic "Go" link in the HTML Help documentation:


```
<a href="overbig.htm" onmouseover="liteGo(go1)" onmouseout="liteOff(go1)">
<span ID="go1" class="endlink">GO</span></a>
```



## Note

If you place multiple elements on the same page, each one must have a unique ID.

## Related topics

<dl> <dt>

[Insert the JavaScript Code](to-insert-the-javascript-code.md)
</dt> </dl>

 

 




