---
title: VML Locks Element
description: VML Locks Element
ms.assetid: 1dfdc23a-0ad1-468f-a850-2068f3cc1803
ms.topic: article
ms.date: 05/31/2018
---

# VML Locks Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a lock for a shape.

The following attributes modify a lock.



| Attribute                                                    | Description                                                                 |
|--------------------------------------------------------------|-----------------------------------------------------------------------------|
| [AdjustHandles](msdn-online-vml-adjusthandles-attribute.md) | Determines whether the handles of a shape can be edited.                    |
| [AspectRatio](msdn-online-vml-aspectratio-attribute.md)     | Determines whether the aspect ratio of a shape can be changed by an editor. |
| [Cropping](msdn-online-vml-cropping-attribute.md)           | Determines whether cropping will be allowed in an editor.                   |
| [Ext](ext-attribute--lock--vml.md)                          | Defines the behavior of locking actions for a graphical editor.             |
| [Grouping](msdn-online-vml-grouping-attribute.md)           | Determines whether shapes can be grouped in an editor.                      |
| [Position](position-attribute--lock--vml.md)                | Determines whether the position of a shape is locked in an editor.          |
| [Rotation](rotation-attribute--lock--vml.md)                | Determines whether rotation of shapes will be allowed in an editor.         |
| [Selection](msdn-online-vml-selection-attribute.md)         | Determines whether the shape is selectable in an editor.                    |
| [ShapeType](msdn-online-vml-shapetype-attribute.md)         | Determines whether the AutoShapes type can be changed by an editor.         |
| [Text](msdn-online-vml-text-attribute.md)                   | Determines whether the text attached to a shape can be edited.              |
| [Vertices](msdn-online-vml-vertices-attribute.md)           | Determines whether the vertices of a path can be changed by an editor.      |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

The **Locks** element is a Microsoft Office Extension to VML.

 

 