---
title: ID Attribute (TextBox)(VML)
description: ID Attribute (TextBox)(VML)
ms.assetid: b9eb75cc-4d0a-4e83-a897-e35995ae7c53
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID Attribute (TextBox)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

A name that provides a unique identifier for a textbox. Read/write. **String**.

**Applies To**

[TextBox](msdn-online-vml-textbox-element.md)

**Tag Syntax**

&lt;v: *element* id=" *expression* "&gt;

**Script Syntax**

*element* .id="*expression*"

*expression*=*element*.id

**Remarks**

Use **ID** to refer to a specific textbox. Once you have created a textbox and given it an ID, you can use the ID name when you want to manipulate the textbox.

*VML Standard Attribute*

**Example**

The shape has a textbox ID called "mytextbox".


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:10pt;left:10pt;width:50pt;height:50pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:textbox id="mytextbox">
   VML
   </v:textbox/>
   </v:shape>
```



 

 




