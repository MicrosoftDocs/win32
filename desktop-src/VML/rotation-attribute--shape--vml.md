---
title: Rotation Attribute (Shape)(VML)
description: Rotation Attribute (Shape)(VML)
ms.assetid: e1a648a4-1e87-4bec-90b2-6d3a57c0dba0
ms.topic: article
ms.date: 05/31/2018
---

# Rotation Attribute (Shape)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the angle that a shape is rotated. Read/write. [VgAngleInDegrees](msdn-online-vml-vgangleindegrees-data-type.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="rotation: *expression* ">

**Script Syntax**

*element* .rotation="*expression*"

*expression*=*element*.rotation

**Remarks**

The value in degrees can be positive or negative, and values greater than 360 are modularized to a 360-degree circle. Positive angles are clockwise. The default value is 0.

Note that the shape is repositioned after the rotation to reflect the new bounding box coordinates.

Also note that for scripting, the **style** attribute is not used and that **Rotation** is treated as a direct attribute of the shape.

The **Rotation** attribute is similar to the standard HTML **Rotation** attribute for styles.

*VML Standard Attribute*

**See Also**

**Example**

The rectangle will be tilted 45 degrees.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;rotation:45">
   </v:rect>
```



[Rotation Attribute Example](/previous-versions/bb264091(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 