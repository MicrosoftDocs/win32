---
title: VML BWPure Attribute
description: VML BWPure Attribute
ms.assetid: 'a68e8197-bfd6-4b8e-8d4c-598590addff8'
---

# VML BWPure Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the black-and-white mode for pure black-and-white output devices. Read/write. [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

&lt;v: *element* o:bwpure=" *expression* "&gt;

**Remarks**

When [BWMode](msdn-online-vml-bwmode-attribute.md) is set to **auto**, this attribute is used to determine how to render the shape in pure black and white.

For more information about the values of this attribute, see the [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md) topic. The default is **auto**.

*Microsoft Office Extensions Attribute*

**Example**

The shape is processed as a high contrast image for pure black-and-white output.


```HTML
   <v:rect id=myrect fillcolor="red" o:bwpure="highcontrast" o:bwmode="auto"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 




