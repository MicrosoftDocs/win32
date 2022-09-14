---
title: VML GrayScale Attribute
description: VML GrayScale Attribute
ms.assetid: 0715b78c-f529-422e-9064-7b99324e60de
ms.topic: article
ms.date: 05/31/2018
---

# VML GrayScale Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a picture will be displayed in grayscale mode. Read/write. **VgTriState**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* grayscale=" *expression* ">

**Script Syntax**

*element* .grayscale="*expression*"

*expression*=*element*.grayscale

**Remarks**

If **True**, the picture will be displayed in grayscale instead of color. The default is **False**.

The value is based according to CCIR recommendation 709, which favors more green weight and produces more pleasing results for natural color.

*VML Standard Attribute*

**Example**

The image will be displayed in grayscale instead of color.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata grayscale="True" src="kids.jpg"/>
   </v:shape>
```



 

 