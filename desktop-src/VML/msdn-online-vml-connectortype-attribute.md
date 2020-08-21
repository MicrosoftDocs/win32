---
title: VML ConnectorType Attribute
description: VML ConnectorType Attribute
ms.assetid: acb9050d-c9e4-4d87-96c2-0bd2a1cf6e6b
ms.topic: article
ms.date: 05/31/2018
---

# VML ConnectorType Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Indicates the type of connector used for joining shapes. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:connectortype=" *expression* ">

**Remarks**

Values include:



| Value    | Description                    |
|----------|--------------------------------|
| none     | No connector.                  |
| straight | Default. A straight connector. |
| elbow    | An elbow-shaped connector.     |
| curved   | A curved connector.            |



 

This attribute may also be used by a rules engine of a graphical editor.

*Microsoft Office Extensions Attribute*

**Example**

The shape uses a straight line as a connector.


```HTML
   <v:rect id=myrect fillcolor="red" o:connectortype="straight"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 