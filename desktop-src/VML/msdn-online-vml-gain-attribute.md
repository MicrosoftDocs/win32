---
title: VML Gain Attribute
description: VML Gain Attribute
ms.assetid: '2ac034ff-f3dd-4e98-ad9d-4d9cdad28f3c'
---

# VML Gain Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the intensity of all colors in an image. Read/write. **VgNumber**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

&lt;v: *element* gain=" *expression* "&gt;

**Script Syntax**

*element* .gain="*expression*"

*expression*=*element*.gain

**Remarks**

This attribute defines how bright the color white is, affecting all other colors. Values range from 0 to infinity. The default value is 1.0. A value of 0 displays no image. Values greater than 1 lighten the picture and values less than 1 make the picture seem grayer.

This attribute can be used to create interesting effects.

*VML Standard Attribute*

**Example**

The image will be displayed with all the colors tending toward gray.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata gain=".5" src="kids.jpg"/>
   </v:shape>
```



[Show Me](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/image/x_image.md)

 

 




