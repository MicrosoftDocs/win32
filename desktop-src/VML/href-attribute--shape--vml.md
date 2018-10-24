---
title: HRef Attribute (Shape)(VML)
description: HRef Attribute (Shape)(VML)
ms.assetid: c44b3099-df3f-42e5-ad0c-10400630e884
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HRef Attribute (Shape)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines a URL for a shape. When the shape is clicked, the browser will load the URL. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* href=" *expression* ">

**Script Syntax**

*element* .href="*expression*"

*expression*=*element*.href

**Remarks**

The **HRef** attribute is similar to the standard HTML **HRef** attribute of anchors.

Using **HRef** makes it easy to create interesting buttons on a Web page.

*VML Standard Attribute*

**Example**

When the rectangle is clicked, the browser will load the Microsoft Corporation home page.


```HTML
   <v:rect id=myrect fillcolor="red"
   href="http://www.microsoft.com"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
   
```



[HRef Attribute Example](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/examples/x_href.md). (Requires Microsoft Internet Explorer 5 or greater.)

 

 




