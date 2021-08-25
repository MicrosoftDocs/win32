---
title: Using the Formulas Element
description: Using the Formulas Element
ms.assetid: f5a381b4-4132-4b66-b41a-3cada26b41e2
keywords:
- Web workshop,formulas element
- designing Web pages,formulas element
- Vector Markup Language (VML),formulas element
- VML (Vector Markup Language),formulas element
- vector graphics,formulas element
- formulas element
- VML elements,formulas
- VML shapes,formulas element
- Vector Markup Language (VML),defining paths for shapes
- VML (Vector Markup Language),defining paths for shapes
- vector graphics,defining paths for shapes
- VML shapes,defining paths
- defining paths for shapes
ms.topic: article
ms.date: 05/31/2018
---

# Using the Formulas Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

In this topic, we will illustrate how to use the `&lt;formulas&gt;` sub-element to define an adjustable path for a shape.

You can place the &lt;formulas&gt; sub-element inside `<shape>` or `<shapetype>` to define formulas that can vary the path of a shape. Inside the `&lt;formulas&gt;` sub-element, one **f** sub-element defines one formula so that one value is evaluated based upon that formula. For example, the formula, `<v:f eqn="prod 10 4 5"/>` defines a value that is equivalent to "10 x 4 / 5".

You can place many **f** sub-elements inside one`&lt;formulas&gt;` sub-element. Formulas can reference the values that are defined earlier in other formulas within the same `&lt;formulas&gt;` sub-element. The value that is defined in the first formula can be referred to as @0, the value that is defined in the second formula can be referred to as @1, and so on.

In addition, you can specify the **adj** property attribute of the `<shape>` element, such as adj="100, 200, 150". Inside the `&lt;formulas&gt;` element, you can then reference those values in the **adj** list. The first value (100) in the **adj** list can be referred to as \#0, the second value (200) can be referred to as \#1, and so on.

For example, to draw a smiling face, you can type the following VML representation:

![shape1.gif (735 bytes)](images/shape1f.gif)


```HTML
<v:shape style='width:1in;height:1in;' strokecolor="red"
strokeweight="2pt" coordsize="21600,21600" adj="17520"
path="m10800,0qx0,10800,10800,21600,21600,10800,10800,0xe
m7340,6445qx6215,7570,7340,8695,8465,7570,7340,6445xnfe
m14260,6445qx13135,7570,14260,8695,15385,7570,14260,6445xnfe
m4960@0c8853@3,12747@3,16640@0nfe">
<v:formulas>
<v:f eqn="sum 33030 0 #0"/>
<v:f eqn="prod #0 4 3"/>
<v:f eqn="prod @0 1 3"/>
<v:f eqn="sum @1 0 @2"/>
</v:formulas>
</v:shape>
```





-   `adj="17520"` defines a value (= 17520). This value can be referenced as \#0.
-   The first formula, `<v:f eqn="sum 33030 0 #0"/>`, defines the value (= 33030 + 0 - \#0). This value can be referenced as @0.
-   The second formula, `<v:f eqn="prod #0 4 3"/>`, defines the value (= \#0 \* 4 / 3). This value can be referenced as @1.
-   The third formula, `<v:f eqn="prod @0 1 3"/>`, defines the value (= @0 \* 1 / 3). This value can be referenced as @2.
-   The fourth formula, `<v:f eqn="sum @1 0 @2"/>`, defines the value (=@1 + 0 -@2). This value can be referenced as @3.
-   Inside the `<path>` element, the values defined in the first (@0) and the fourth (@3) formulas are used to determine the outline of the shape.

If you change the **adj** list, such as `adj="20000"`, the values of the formulas that reference the **adj** list will be changed as well, affecting the smiling face as follows:

![shape2.gif (765 bytes)](images/shape2f.gif)


```HTML
<v:shape style='width:1in;height:1in;' strokecolor="red"
strokeweight="2pt" coordsize="21600,21600" adj="20000"
path="m10800,0qx0,10800,10800,21600,21600,10800,10800,0xe
m7340,6445qx6215,7570,7340,8695,8465,7570,7340,6445xnfe
m14260,6445qx13135,7570,14260,8695,15385,7570,14260,6445xnfe
m4960@0c8853@3,12747@3,16640@0nfe">
<v:formulas>
<v:f eqn="sum 33030 0 #0"/>
<v:f eqn="prod #0 4 3"/>
<v:f eqn="prod @0 1 3"/>
<v:f eqn="sum @1 0 @2"/>
</v:formulas>
</v:shape>
```





For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858392) .

 

 
