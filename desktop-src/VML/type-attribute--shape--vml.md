---
title: Type Attribute (Shape)(VML)
description: Type Attribute (Shape)(VML)
ms.assetid: 41f0d1d3-3a2c-47cf-b2ec-d983b14aea87
ms.topic: article
ms.date: 05/31/2018
---

# Type Attribute (Shape)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a reference to the ID of a [ShapeType](msdn-online-vml-shapetype-element.md) element. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

``` syntax
<v:
          element 
          type=" expression ">
```

**Script Syntax**

``` syntax
element 
          .type="#expression"
```

``` syntax
expression=element .type
```

**Remarks**

If the **Type** attribute references the ID of a **ShapeType** element, the fills, paths, and strokes of the **ShapeType** are used as templates to create the shape. Values derived from **ShapeType** can be overridden by individual shape values.

If used in tags, the string value must begin with a number sign (\#) symbol.

**VML Standard Attribute**

**Example**

A **ShapeType** shape is created with the "mytype" as an ID.


```HTML
   <v:shapetype id="mytype"
   fillcolor="red" strokecolor="blue"
   coordorigin="0 0" coordsize="200 200">
   <v:path v="m 0,0 l 0,200, 200,200, 200,0 x e"/>
   </v:shapetype>
```



Then if you create a shape using the **ShapeType** values, the shape will have the attributes of the "mytype" **ShapeType**; that is, "shape01" will have a red fill with a blue stroke.


```HTML
   <v:shape id="shape01" type="#mytype"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:shape>
```



You can override the inherited values, for example, by changing the color to green.


```HTML
   <v:shape id="shape02" type="#mytype"
   fillcolor="green"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:shape>
```



[Type Attribute Example](/previous-versions/bb264099(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 