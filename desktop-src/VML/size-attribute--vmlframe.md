---
title: Size Attribute (VMLFrame)
description: Size Attribute (VMLFrame)
ms.assetid: 95d953fa-cbe2-4ebc-9b23-408347232fee
ms.topic: article
ms.date: 05/31/2018
---

# Size Attribute (VMLFrame)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the size of the clipping region of the frame. Read/write. **VgVector2D**.

**Applies To**

[VMLFrame](msdn-online-vml-vmlframe-element.md)

**Tag Syntax**

<v: *element* size=" *expression* ">

**Script Syntax**

*element* .size="*expression*"

*expression*=*element*.size

**Remarks**

The default value is 0,0. Note that **Size** only works if [Clip](msdn-online-vml-clip-attribute.md) is **True**. In this attribute, the size is defined as the width and height of the frame.

*VML Standard Attribute*

**Example**

The size of the clipping region will be 50pt, 50pt.


```HTML
   <v:vmlframe id="frame01" clip="True"
   origin="100pt,100pt" size="50pt,50pt"
   src="external.vml#shape01"
   style='top:160pt; left:100pt; width:50pt; height:50pt'>
   </v:vmlframe>
```



 

 