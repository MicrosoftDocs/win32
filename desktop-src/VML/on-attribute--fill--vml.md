---
title: On Attribute (Fill)(VML)
description: On Attribute (Fill)(VML)
ms.assetid: 9b7d42e5-4fd9-402d-8d1f-af01f6577475
ms.topic: article
ms.date: 05/31/2018
---

# On Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the fill will be displayed. Read/write. **VgTriState**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* on=" *expression* ">

**Script Syntax**

*element* .on="*expression*"

*expression*=*element*.on

**Remarks**

If **False**, the fill is not displayed. The default is **True**.

*VML Standard Attribute*

**Example**

Even though the fill is defined to be red, it is not displayed.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill color="red" on="False"/>
   </v:shape>
```



 

 