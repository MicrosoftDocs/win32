---
title: VML TableProperties Attribute
description: VML TableProperties Attribute
ms.assetid: 10355742-13b9-4c08-bff7-f7f7501762e9
ms.topic: article
ms.date: 05/31/2018
---

# VML TableProperties Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines table properties. Read/write. **Integer**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:tableproperties=" *expression* ">

**Remarks**

Used by Microsoft PowerPoint for native tables. Default value is 0. Only the first three bits of this integer are used.

Even though the value is stored in a shape, the attribute is only useful when the table is made up of shapes that are grouped.Bits may be combined.

The following bit values are included.



| Bit | Description                              |
|-----|------------------------------------------|
| 1   | Set if the group of shapes is a table.   |
| 2   | Set if the shape is a placeholder.       |
| 3   | Set if the table text is bi-directional. |



 

*Microsoft Office Extensions Attribute*

 

 