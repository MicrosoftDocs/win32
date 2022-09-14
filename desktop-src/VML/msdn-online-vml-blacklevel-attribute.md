---
title: VML BlackLevel Attribute
description: VML BlackLevel Attribute
ms.assetid: b30446c2-f4f3-49f5-aa60-4119f211add2
ms.topic: article
ms.date: 05/31/2018
---

# VML BlackLevel Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the intensity of black in an image. Read/write. **VgNumber**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* blacklevel=" *expression* ">

**Script Syntax**

*element* .blacklevel="*expression*"

*expression*=*element*.blacklevel

**Remarks**

Allows the color level to be modified so that blacks appear as true blacks, and all other colors are visible as shades above black. The default value is 0. While any number between positive and negative infinity is permitted, values less than -0.5 will display as all black and values greater than 0.5 will display as all white.

*VML Standard Attribute*

**Example**

The image will be displayed with very dark tones.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata blacklevel="-0.2" src="kids.jpg"/>
   </v:shape>
```



 

 