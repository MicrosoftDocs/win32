---
title: VML Curve Element
description: VML Curve Element
ms.assetid: 37197ef0-7597-465a-bc37-7ffcde2e736b
ms.topic: article
ms.date: 05/31/2018
---

# VML Curve Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Predefined curve shape.

**Curve** uses the [to](to-attribute--curve--vml.md), [from](from-attribute--curve--vml.md), [control1](msdn-online-vml-control1-attribute.md), and [control2](msdn-online-vml-control2-attribute.md) attributes.

The following is the minimum code needed to produce an image.


```HTML
   <v:curve
   from="10pt,10pt" to="100pt,10pt"
   control1="40pt,30pt" control2="70pt,30pt">
   </v:curve>
```





 

 