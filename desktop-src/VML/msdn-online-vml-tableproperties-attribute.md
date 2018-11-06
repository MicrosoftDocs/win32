---
title: VML TableProperties Attribute
description: VML TableProperties Attribute
ms.assetid: 10355742-13b9-4c08-bff7-f7f7501762e9
ms.topic: article
ms.date: 05/31/2018
---

# VML TableProperties Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

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

 

 




