---
title: About Creating Dynamic Hyperlinks
description: About Creating Dynamic Hyperlinks
ms.assetid: F8A5D176-6266-4c1b-AAF4-0E3938601687
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Creating Dynamic Hyperlinks

You can create a more dynamic help system, and bring greater emphasis to text links, by making your links change color or size when a user points to them.

For an example, point to the link at the bottom of this topic. The following hover style was added to the cascading style sheet for this help file to create the dynamic links:


```CSS
a:hover {<i>attribute:</i> <i>value</i>; }
```



where attribute is a stylesheet attribute, and value is the corresponding value. Use a semicolon to separate multiple attributes.

### Example

The following example shows an anchor that will turn red and become bold when a user moves their cursor over the link text:


```CSS
a:hover {color: red; font-weight: bold; }
```



## Related topics

<dl> <dt>

[Create Dynamic Links](example--create-dynamic-elements-with-dhtml.md)
</dt> </dl>

 

 




