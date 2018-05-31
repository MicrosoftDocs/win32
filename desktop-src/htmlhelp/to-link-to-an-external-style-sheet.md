---
title: To link to an external style sheet
description: To link to an external style sheet
ms.assetid: BB785AF3-1C06-4adf-BB36-F074A9DF8EFF
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To link to an external style sheet

Add the &lt;LINK&gt; tag, between the &lt;HEAD&gt; start and end tags, to each help file or Web page where you want to attach the style sheet. For example:


```
<LINK REL = "stylesheet"
TYPE = "<code><b class="cfe">mime/type</b></mark>"
HREF = "<code><b class="cfe">url</b></mark>"> 
```



where the value `REL= "stylesheet"` indicates that the target source is a style sheet, `mime/type `is the MIME type for the style sheet, and `url` is the address of the style sheet file.

> [!Note]  
> Each style sheet has its own MIME type. Cascading style sheets have the MIME type **text/css**.

 

## Related topics

<dl> <dt>

[About Using Cascading Style Sheets](use-cascading-style-sheets.md)
</dt> </dl>

 

 




