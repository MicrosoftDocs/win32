---
title: VML ShadowOK Attribute
description: VML ShadowOK Attribute
ms.assetid: 88400bf5-f41c-4495-a5d0-9b35c1cae9f7
ms.topic: article
ms.date: 05/31/2018
---

# VML ShadowOK Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a shadow will be displayed. Read/write. **VgTriState**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* shadowok=" *expression* ">

**Script Syntax**

*element* .shadowok="*expression*"

*expression*=*element*.shadowok

**Remarks**

If **False**, the path cannot have a shadow. The default is **True**. This attribute overrides all other shadow attributes in the parent or **Shadow** element.

*VML Standard Attribute*

**Example**

The shape will not have a shadow.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="green"
   style="top:1;left:1;width:50;height:50">
   <v:shadow on="True" offset="5pt,5pt" color="blue"/>
   <v:path id= "myPath" shadowok="False" v="m 1,1 l 1,200, 200,200, 200,1 x e"/>
   </v:shape>
```



 

 