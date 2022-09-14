---
title: VML RuleInitiator Attribute
description: VML RuleInitiator Attribute
ms.assetid: 2c9b1131-b088-4b70-b132-bdb4296433ae
ms.topic: article
ms.date: 05/31/2018
---

# VML RuleInitiator Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a rules engine will be used. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:ruleinitiator=" *expression* ">

**Remarks**

The default value is **False**. If the value is **True**, a rules engine is used.

*Microsoft Office Extensions Attribute*

**Example**

The shape will be processed by a rules engine.


```HTML
   <v:rect id=myrect fillcolor="red" rulesinitiator="True"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 