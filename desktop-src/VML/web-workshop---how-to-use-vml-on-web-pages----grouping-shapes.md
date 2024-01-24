---
title: Grouping Shapes
description: This article describes grouping shapes in VML, a feature that is deprecated as of Windows Internet Explorer 9.
ms.assetid: 469c9e4d-d1ae-4285-b2cb-ac833ebe59ff
keywords:
- Web workshop,grouping shapes
- designing Web pages,grouping shapes
- Vector Markup Language (VML),grouping shapes
- VML (Vector Markup Language),grouping shapes
- vector graphics,grouping shapes
- VML shapes,grouping
- grouping shapes
- Vector Markup Language (VML),group element
- VML (Vector Markup Language),group element
- vector graphics,group element
- group element
- VML elements,group
- Vector Markup Language (VML),local coordinate space
- VML (Vector Markup Language),local coordinate space
- vector graphics,local coordinate space
- local coordinate space
ms.topic: article
ms.date: 05/31/2018
---

# Grouping Shapes

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

As you've learned, you can easily draw individual shapes by using VML. In this section, we will explain the benefits of grouping shapes together, and how to group shapes.

If you had many shapes that needed to be scaled, moved, or rotated together, you would find it tedious to set the attributes individually for each shape. Plus you would raise your margin for errors. It would be better if you could group the shapes, and then set the attributes for the entire group.

In VML, you can use the `<group>` element to group many shapes together so that they can be transformed as one unit. For example, as shown in the following VML representation, you can easily group two shapes together.


```HTML
<v:group id="GroupA" style='position:relative;left:10pt;top:20pt;
width:150pt;height:100pt; ...>
   <v:shape id="Shape1"...></v:shape>
   <v:shape id="Shape2"...></v:shape>
</v:group>
```



When shapes are grouped, they use the [local coordinate space](web-workshop---how-to-use-vml-on-web-pages----local-coordinate-space.md) of the group. Therefore, shapes within a group can be scaled and moved together. You will see more examples in the Use Local Coordinate Space topic.

Inside a group, you can have as many shapes or groups as you want. When a group is inside another group, it is called a "nested group". There is no limitation on the levels of nesting.

For example, the following lines demonstrate a 3-level nested group. Shape3 and Shape4 are in GroupC. Shape2 and GroupC are in GroupB. Shape1 and GroupB are in GroupA.


```HTML
<body>
   <v:group id="GroupA"...>
      <v:shape id="Shape1"...></v:shape>
      <v:group id="GroupB"...>
         <v:shape id="Shape2"...></v:shape>
         <v:group id="GroupC"...>
            <v:shape id="Shape3"...></v:shape>
            <v:shape id="Shape4"...></v:shape>
         </v:group>
      </v:group>
   </v:group>
</body>
```



For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858388) .

[![back to top](images/top.gif) Back to top](#top)

## Summary

You can use the `<group>` element to group many shapes together so that they can be transformed as one unit.

 

 