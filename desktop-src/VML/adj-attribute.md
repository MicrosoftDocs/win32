---
title: Adj Attribute
description: Adj Attribute
ms.assetid: f0f31e6c-9dde-4082-88a2-da2d0012b9ae
ms.topic: article
ms.date: 05/31/2018
---

# Adj Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies an adjustment value used to define values for a formula. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* adj=" *expression* ">

**Script Syntax**

*element* .adj="*expression*"

*expression*=*element*.adj

**Remarks**

**Adj** is used to provide adjustable points for a formula. If used in tags, **Adj** is a comma-delimited string of up to 8 values. Some values may be omitted. For example, "0,1,2,,4,5,,7" would be a valid string but the fourth and seventh items would not have values (items are counted starting from 0).

For scripting, **Adj** uses the [IVgAdjustments](msdn-online-vml-ivgadjustments-data-type.md) data type.

*VML Standard Attribute*

**See Also**

[Formula](msdn-online-vml-formulas-element.md)

**Example**

A simple square is created with adjustments. First the **Adj** string is created to define eight adjustment values. Then each adjustment value is referenced by one of the eight formulas, with each adjustment value preceeded by a number sign (\#) symbol. Finally a path is defined by a string that references the formulas, with each formula preceeded by the "at" sign (@) symbol.


```HTML
   <v:shape id="rect01" type="#myshape"
   fillcolor="red" strokecolor="red"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:30;left:30;width:20;height:20"
   adj="1, 1, 1, 200, 200, 200, 200, 1">
   <v:path v="m @0,@1 l @2,@3, @4,@5, @6,@7 x e"/>
   <v:formulas>
   <v:f eqn="val #0"/>
   <v:f eqn="val #1"/>
   <v:f eqn="val #2"/>
   <v:f eqn="val #3"/>
   <v:f eqn="val #4"/>
   <v:f eqn="val #5"/>
   <v:f eqn="val #6"/>
   <v:f eqn="val #7"/>
   </v:formulas>
   </v:shape>
```



[Adj Attribute Example](/previous-versions/bb229662(v=vs.85)) (Requires Microsoft Internet Explorer 5 or greater.)

 

 