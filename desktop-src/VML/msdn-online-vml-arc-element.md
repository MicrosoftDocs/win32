---
title: VML Arc Element
description: VML Arc Element
ms.assetid: 46b5b78a-9a69-432b-9008-0ce7a658b9dd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML Arc Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Predefined arc shape.

**Arc** uses the [startangle](msdn-online-vml-startangle-attribute.md) and [endangle](msdn-online-vml-endangle-attribute.md) attributes.

The following is the minimum code needed to produce an image.


```HTML
   <v:arc
   style="top:10;left:10;width:200;height:200"
   startangle="90" endangle="270">
   </v:arc>
```



[Show Me](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/predef/t_arc.md)

 

 




