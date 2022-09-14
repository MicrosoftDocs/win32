---
title: VML BWNormal Attribute
description: VML BWNormal Attribute
ms.assetid: 4d361fc8-e1a9-4af4-91d1-72cff898650c
ms.topic: article
ms.date: 05/31/2018
---

# VML BWNormal Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the black-and-white mode for normal black-and-white output devices. Read/write. [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:bwnormal=" *expression* ">

**Remarks**

When [BWMode](msdn-online-vml-bwmode-attribute.md) is set to **auto**, this attribute is used to determine how to render the shape in normal black and white.

For more information about the values of this attribute, see the [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md) topic. The default value is **auto**.

*Microsoft Office Extensions Attribute*

**Example**

The shape is processed as a grayscale image for normal black-and-white output.


```HTML
   <v:rect id=myrect fillcolor="red" o:bwnormal="grayscale" o:bwmode="auto"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 