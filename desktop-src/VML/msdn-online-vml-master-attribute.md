---
title: VML Master Attribute
description: VML Master Attribute
ms.assetid: ec661dc6-8e1c-47a3-ad3a-e1ee7e64c840
ms.topic: article
ms.date: 05/31/2018
---

# VML Master Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a **ShapeType** element is a master element. Read/write. **VgTriState**.

**Applies To**

[ShapeType](msdn-online-vml-shapetype-element.md)

**Tag Syntax**

<v: *element* o:master=" *expression* ">

**Remarks**

If **True**, the **ShapeType** shape is rendered by the rendering engine. The default value is **False**.

*Microsoft Office Extensions Attribute*

**Example**

The **ShapeType** element is a master shape.


```HTML
   <v:shapetype id="laure"
   coordorigin= "0 0" coordsize="200 200"
   fillcolor= "red" o:master="True"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shapetype>
```



 

 