---
title: VML Visibility Attribute
description: VML Visibility Attribute
ms.assetid: 1a15335b-e7e9-4bf1-9c0c-8d2e4704f256
ms.topic: article
ms.date: 05/31/2018
---

# VML Visibility Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a shape is displayed. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="visibility: *expression* ">

**Script Syntax**

*element* .style.visibility="*expression*"

*expression*=*element*.style.visibility

**Remarks**

The **Visibility** attribute is similar to the standard HTML **Visibility** attribute for styles.

Values include:



| Value    | Description                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| visible  | The shape is visible.                                                                                                                                                                   |
| hidden   | The shape is not visible, but is still part of the flow of the objects in the browser. Mouse events are not processed.                                                                  |
| inherit  | Default. The visibility state is inherited from the parent of the shape. Microsoft Office applications only use **inherit** and **hidden**; any other values are mapped to **inherit**. |
| collapse | Used for graphical editing applications that can collapse groups of shapes; for example, outliners.                                                                                     |



 

*VML Standard Attribute*

**Example**

The following code creates a shape but makes it hidden. Other objects in the document will flow around it, leaving a space the same size as the shape.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;visibility:hidden">
   </v:rect>
```



[Visibility Attribute Example](/previous-versions/bb264100(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 