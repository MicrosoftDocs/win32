---
title: VML Alt Attribute
description: VML Alt Attribute
ms.assetid: 6b7e778c-d8e2-432e-b69a-5d80fa62d105
ms.topic: article
ms.date: 05/31/2018
---

# VML Alt Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines alternative text to be displayed instead of a graphic. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* alt=" *expression* ">

**Script Syntax**

*element* .alt="*expression*"

*expression*=*element*.alt

**Remarks**

The **Alt** attribute is similar to the standard HTML **Alt** attribute. This attribute provides a way for browsers that convert text to speech to describe graphical elements on a page.

*VML Standard Attribute*

**See Also**

[Shape](shape-element--vml.md)

**Example**

The **Alt** element below will display the phrase "Red rectangle" in browsers that convert Web pages to spoken phrases.


```HTML
   <v:rect id=myrect fillcolor="red" alt="Red rectangle"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



[Alt Attribute Example](/previous-versions/bb229663(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 