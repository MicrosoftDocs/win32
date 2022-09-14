---
title: VML InvY Attribute
description: VML InvY Attribute
ms.assetid: 6c8c51ab-88ce-40b2-add7-1152e125ad8b
ms.topic: article
ms.date: 05/31/2018
---

# VML InvY Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the y position of the handle is inverted. Read/write. **VgTriState**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

<v: *element* invy=" *expression* ">

**Remarks**

If **True**, the y position of the handle is inverted by subtracting the y value from the y value of **CoordOrigin** added to the y value of **CoordSize**. The default value is **False**.

This attribute is the equivalent of


```HTML
coordorigin.y + coordsize.y - h.position.y
```



*VML Standard Attribute*

 

 