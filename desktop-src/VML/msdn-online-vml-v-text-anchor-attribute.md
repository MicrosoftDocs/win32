---
title: VML V-Text-Anchor Attribute
description: VML V-Text-Anchor Attribute
ms.assetid: d6e2f60c-5cc7-4340-a9cd-b6c2b0b5b0be
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Anchor Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the vertical anchoring of text in a textbox. Read/write. **String**.

**Applies To**

[TextBox](msdn-online-vml-textbox-element.md)

**Tag Syntax**

<v: *element* v-text-anchor=" *expression* ">

**Remarks**

Values include:

-   **top** (default)
-   **middle**
-   **bottom**
-   **top-center**
-   **middle-center**
-   **bottom-center**
-   **top-baseline**
-   **bottom-baseline**
-   **top-center-baseline**
-   **bottom-center-baseline**

The text will be anchored to a vertical position in the textbox as indicated by the attribute value. The alignment of a text anchor only becomes evident if [MSO-Fit-Text-To-Shape](msdn-online-vml-mso-fit-text-to-shape-attribute.md) is **False**. This attribute is different from the **Vertical-Align** Style attribute, which is used for ideographic languages.

This attribute is used by Microsoft Office to store data in Web documents but does not render in Microsoft Internet Explorer 5 or greater.

*VML Standard Attribute*

**Example**

The text is aligned to the bottom of the textbox.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:10pt;left:10pt;width:50pt;height:50pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:textbox style="v-text-anchor:bottom" id="mytextbox">
   VML
   </v:textbox/>
   </v:shape>
```



 

 