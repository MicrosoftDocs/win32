---
title: VML Bilevel Attribute
description: VML Bilevel Attribute
ms.assetid: 5b87e928-6f0a-4b00-833a-3c2add2d5677
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML Bilevel Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether an image will be displayed in black and white. Read/write. **VgTriState**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

&lt;v: *element* bilevel=" *expression* "&gt;

**Script Syntax**

*element* .bilevel="*expression*"

*expression*=*element*.bilevel

**Remarks**

If **True**, the image will be displayed using two colors (black and white). The default is **False**. This creates an effect similar to posterization.

*VML Standard Attribute*

**Example**

The image will be displayed in black and white only.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata bilevel="True" src="kids.jpg"/>
   </v:shape>
```



 

 




