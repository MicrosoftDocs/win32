---
title: Color Attribute (Fill)(VML)
description: Color Attribute (Fill)(VML)
ms.assetid: 38e75bf5-4da9-4c58-af86-3554d03a6b7b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Color Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the color of a fill. Read/write. **VgColor**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

&lt;v: *element* color=" *expression* "&gt;

**Script Syntax**

*element* .color="*expression*"

*expression*=*element*.color

**Remarks**

Overrides the **FillColor** attribute of a shape. The default value is **White**.

*VML Standard Attribute*

**Example**

The fill color of the shape is green.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill color="green"/>
   </v:shape>
```



 

 




