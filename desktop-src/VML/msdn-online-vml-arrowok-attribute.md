---
title: VML ArrowOK Attribute
description: VML ArrowOK Attribute
ms.assetid: 19b23544-4a72-4273-b48a-6aee39addcf6
ms.topic: article
ms.date: 05/31/2018
---

# VML ArrowOK Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether arrowheads will be displayed. Read/write. **VgTriState**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* arrowok=" *expression* ">

**Script Syntax**

*element* .arrowok="*expression*"

*expression*=*element*.arrowok

**Remarks**

If **False**, the path will not have arrowheads. The default is **False**. This attribute overrides all other arrowhead attributes in the parent or **Stroke** element.

*VML Standard Attribute*

**Example**

The path will not have an arrowhead.


```HTML
   <v:line id="whatsmyline"
   style="position:relative"
   from="114pt,66pt" to="402pt,66pt"
   strokecolor="black">
   <v:stroke startarrow="block" endarrow="block"/>
   <v:path arrowok="False"/>
   </v:line>
```



 

 