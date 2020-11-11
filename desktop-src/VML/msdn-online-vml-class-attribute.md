---
title: VML Class Attribute
description: VML Class Attribute
ms.assetid: 4030b8b7-fcc9-4153-8004-81935a347a09
ms.topic: article
ms.date: 05/31/2018
---

# VML Class Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Refers to a definition of a CSS style. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* class=" *expression* ">

**Script Syntax**

*element* .classname="*expression*"

*expression*=*element*.classname

**Remarks**

The **class** attribute is similar to the standard HTML **class** attribute used with CSS style sheets.

Note that **classname** is used instead of **class** for scripting. Also note that for scripting, the **classname** can only be read; changing the value of **classname** will not change the rendering of the shape.

*VML Standard Attribute*

**See Also**

[Shape](shape-element--vml.md)

**Example**

A class for **width** is created with the style


```HTML
   .narrowstyle {width:50;height:100}
```



Then the width is referenced by including the style. Note that the width andheight is not defined in the **style** attribute, but will be defined by the style.


```HTML
   <v:shape id="rect01" class="narrowstyle"
   fillcolor="red" strokecolor="red"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



Note that **Class** only applies to CSS-type attributes.

 

 