---
title: Src Attribute (ImageData)(VML)
description: Src Attribute (ImageData)(VML)
ms.assetid: ef6b57d9-dca7-4f6e-8fd1-e846e4d09fb7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Src Attribute (ImageData)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines a source for the image. Read/write. **String**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

&lt;v: *element* src=" *expression* "&gt;

**Script Syntax**

*element* .src="*expression*"

*expression*=*element*.src

**Remarks**

This attribute must always be used with the [ImageData](msdn-online-vml-imagedata-element.md) element and point to valid image data for a picture to be displayed. If this attribute appears without [HRef](vml-msdn_online_vml_h_elementref_attribute__imagedata__vml) or [Title](title-attribute--imagedata--vml.md), then the image is linked.

*VML Standard Attribute*

**Example**

The source of the image is a file named "kids.jpg".


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata src="kids.jpg"/>
   </v:shape>
```



 

 




