---
title: VML TableLimits Attribute
description: VML TableLimits Attribute
ms.assetid: eef855de-23c5-4894-b7cf-2ea39e372e08
ms.topic: article
ms.date: 05/31/2018
---

# VML TableLimits Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

List of minimum height values for each row in a table. Read/write. **VgLengthArray**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:tablelimits=" *expression* ">

**Remarks**

Used by Microsoft PowerPoint for native tables. Default value is **Null**.

Even though the value is stored in a shape, the attribute is only useful when the table is made up of shapes that are grouped. When text is added to table cells, the row height may increase. The **TableLimits** attribute stores the original row height so that if text is deleted, the row height will not fall below the original value.

*Microsoft Office Extensions Attribute*

 

 