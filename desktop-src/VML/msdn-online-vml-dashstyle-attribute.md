---
title: VML DashStyle Attribute
description: VML DashStyle Attribute
ms.assetid: 7d6c7cbf-9ccc-4117-af0a-ca8f36684f88
ms.topic: article
ms.date: 05/31/2018
---

# VML DashStyle Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the dot and dash pattern for a stroke. Read/write. **VgLineDashStyle**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* dashstyle=" *expression* ">

**Script Syntax**

*element* .dashstyle="*expression*"

*expression*=*element*.dashstyle

**Remarks**

Values include:

-   Solid (default)
-   ShortDash
-   ShortDot
-   ShortDashDot
-   ShortDashDotDot
-   Dot
-   Dash
-   LongDash
-   DashDot
-   LongDashDot
-   LongDashDotDot

The **DashStyle** attribute allows the user to specify a custom-defined dash pattern. This is done using a series of numbers. Dash styles are defined in terms of the length of the dash (the drawn part of the stroke) and the length of the space between the dashes. The lengths are relative to the line width: a length of "1" is equal to the line width. The **EndCap** style is applied to each dash, the arrow style is not. The string first defines the length of the dash then the length of the space. This may be repeated to form complex dash styles. The string should always contain a pair of numbers; if it contains an odd number of numbers the last may be disregarded.

The following table lists some typical values and a description of the intended effect. "0" implies a dot that should be fourfold symmetrical (with round end caps it should be a circle). If the line end cap is "flat," a viewer should choose a built-in operating system dash where possible (in other words. something that is fast to draw.). The following table shows some examples.



| DashStyle     | Description                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| "2 2"         | Short-dashes. Each dash and the space between is twice the width of the line.                        |
| "0 2"         | Dots. Space between is twice the width of the line.                                                  |
| "2 2 0 2"     | Short dash dot.                                                                                      |
| "2 2 0 2 0 2" | Short dash dot dot.                                                                                  |
| "1 2"         | Dot. Each dash is the width of the line, while each space is twice the width of the line.            |
| "4 2"         | Dash. Each dash is four times the width of the line while each space is twice the width of the line. |
| "8 2"         | Long dash.                                                                                           |
| "4 2 1 2"     | Dash dot.                                                                                            |
| "8 2 1 2"     | Long dash dot.                                                                                       |
| "8 2 1 2 1 2" | Long dash dot dot.                                                                                   |



 

*VML Standard Attribute*

**Example**

The shape has a dash style of alternating dashes and dots.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200,200,200, 200,1 x e">
   <v:stroke dashstyle="dashdot"/>
   </v:shape>
```



 

 