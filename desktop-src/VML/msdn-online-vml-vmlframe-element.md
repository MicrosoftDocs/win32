---
title: VML VMLFrame Element
description: VML VMLFrame Element
ms.assetid: a1582223-d6e2-42d1-95bb-97f6f1d453d2
ms.topic: article
ms.date: 05/31/2018
---

# VML VMLFrame Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a frame for an external shape.

The following attributes modify a frame.



| Attribute                                     | Description                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------|
| [Clip](msdn-online-vml-clip-attribute.md)    | Determines whether the image will be clipped.                         |
| [ID](id-attribute--vmlframe--vml.md)         | Defines a unique identifier for the frame.                            |
| [Origin](origin-attribute--vmlframe--vml.md) | Specifies the origin of the frame.                                    |
| [Size](size-attribute--vmlframe.md)          | Specifies the size of the frame.                                      |
| [Src](src-attribute--vmlframe--vml.md)       | Specifies the source of the data that will be displayed in the frame. |
| [Style](msdn-online-vml-style-attribute.md)  | Defines the normal CSS styles that can be used to position the frame. |



 

**Remarks**

The source data to be displayed in the frame can be contained in the same Web page or be part of another page. Through scripting, the source can be changed dynamically and the display characteristics can be modified.

Objects inside the **VMLFrame** are "zoom scaled." That is, they scale like metafiles, where line weights, shadow offsets, and text area are all scaled proportionally. This is different from a group, where object size and position are scaled proportionally, but line, shadow, etc. are not.

The following is the minimum code needed to load an image into a frame.


```HTML
   <v:vmlframe
     style="top:1;left:1;width:50;height:50">
     src="external.vml#rect01"/>
   </v:vmlframe>
```



If the file is external, it must be an XML file. The following code is the minimum code needed to specify an external source file that must contain an identifiable shape. This sample contains an image shape that displays a bitmap.


```HTML
   <xml xmlns:v = "urn:schemas-microsoft-com:vml">
   <v:image id="rect01"
     style="height:100;width:100;top:50;left:50">
     src="kids.jpg">
   </v:rect>
   </xml>
```



> [!Note]  
> In pre-release versions of VML, this element was called **VMLCanvas** .

 

**Examples**

-   [Simple VMLFrame Example](/previous-versions/bb263920(v=vs.85))
-   [Dynamic VMLFrame Example](/previous-versions/bb263902(v=vs.85))

 

 