---
title: VML ConnectType Attribute
description: VML ConnectType Attribute
ms.assetid: 907803c8-687b-4823-8252-b59acbbd9aa4
ms.topic: article
ms.date: 05/31/2018
---

# VML ConnectType Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the type of connection points used for attaching shapes to other shapes. Read/write. **String**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* o:connecttype=" *expression* ">

**Remarks**

Values include:



| Value    | Description                                                                                                                           |
|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| none     | No connection sites. Default.                                                                                                         |
| rect     | Standard four connection points at midpoints of top, bottom, left, and right sides.                                                   |
| segments | The edit points of the shape are used. Edit points are the black dots in a graphical editor that are used to select parts of a shape. |
| custom   | A custom array of connection locations.                                                                                               |



 

*Microsoft Office Extensions Attribute*

 

 