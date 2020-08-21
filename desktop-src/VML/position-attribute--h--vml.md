---
title: Position Attribute (H)(VML)
description: Position Attribute (H)(VML)
ms.assetid: 0bae708d-5409-4609-a102-7f799f2c1fbb
ms.topic: article
ms.date: 05/31/2018
---

# Position Attribute (H)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies thex and y values of the handle. Read/write **VgVector2D**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

<v: *element* position=" *expression* ">

**Remarks**

x and y values can be one of the following types:

-   constant
-   formula (for example, @2)
-   adjust (for example, \#3)
-   center
-   topleft
-   bottomright

If any of the above types except *adjust* are specified, the handle position is fixed in that dimension. If an adjust handle is specified, the handle is free to move in that dimension and the adjust value is determined by the position of the handle.

If a [Polar](msdn-online-vml-polar-attribute.md) attribute is specified, the **Position** attribute represents the radius and angle values of the handle instead of x and y.

The default value is 0,0.

*VML Standard Attribute*

 

 