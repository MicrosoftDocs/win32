---
title: VML Target Attribute
description: VML Target Attribute
ms.assetid: 2e1cc002-65c9-4945-8c07-f23dc704d867
ms.topic: article
ms.date: 05/31/2018
---

# VML Target Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a frame or window that a URL is displayed in. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* target=" *expression* ">

**Remarks**

The **Target** attribute is similar to the standard HTML **Target** attribute of anchors.

Values include:



| Value      | Description                                                                                                                                                                                                                                                      |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetName | String containing the name of the frame or window in which to load the document.                                                                                                                                                                                 |
| \_blank    | Specifies that the linked document is loaded into a new blank window. This window is not named.                                                                                                                                                                  |
| \_media    | As of Internet Explorer 6 for Windows XP Service Pack 2, the \_media attribute is obsolete and is no longer supported. First available in Internet Explorer 6, this value specified that the linked document should be loaded into the Media Bar.                |
| \_parent   | Specifies that the linked document is loaded into the immediate parent of the document containing the link.                                                                                                                                                      |
| \_search   | As of Internet Explorer 7 for Windows XP Service Pack 2, : The \_search attribute is obsolete and is no longer supported. First available in Internet Explorer 6, this value specified that the linked document was to be loaded into the browser's search pane. |
| \_self     | Specifies that the linked document is loaded into the window in which the link was clicked (the active window).                                                                                                                                                  |
| \_top      | Specifies that the linked document is loaded into the topmost window.                                                                                                                                                                                            |



 

*VML Standard Attribute*

**Example**

When the rectangle is clicked, the browser loads the Microsoft Corporation home page in the same window.


```HTML
   <v:rect id=myrect fillcolor="red"
   href="https://www.microsoft.com" target="_self"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



[Target Attribute Example](/previous-versions/bb264096(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 