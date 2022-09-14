---
title: Using the Handles Element
description: Using the Handles Element
ms.assetid: d748f74c-40e5-499a-bb61-94862eb3811c
keywords:
- Web workshop,handles element
- designing Web pages,handles element
- Vector Markup Language (VML),handles element
- VML (Vector Markup Language),handles element
- vector graphics,handles element
- handles element
- VML elements,handles
- VML shapes,handles element
- Vector Markup Language (VML),attaching text to shapes
- VML (Vector Markup Language),attaching text to shapes
- vector graphics,attaching text to shapes
- VML shapes,attaching text
- attaching text to shapes
ms.topic: article
ms.date: 05/31/2018
---

# Using the Handles Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

In this topic, we will illustrate how to use the `<handles>` element to attach text to a shape.

You can place the `<handles>` sub-element inside `<shape>` or `<shapetype>` to define user interface elements that can vary the **adj** values on the shape.

For example, as shown the following VML representation, you can provide an adjust handle (yellow box) that users can simply drag to adjust the shape.

Note: the handles are available when this VML shape is viewed in Microsoft Office applications, where the shape is intended to be manipulable.

![shape1.gif (564 bytes)](images/shape1h.gif)


```HTML
<v:shape style='width:90pt;height:54pt;'strokecolor="red"
strokeweight="2pt" coordsize="21600,21600" adj="16200,5400"
path="m@0,0l@0@1,0@1,0@2@0@2@0,21600,21600,10800xe">
<v:formulas>
<v:f eqn="val #0"/>
<v:f eqn="val #1"/>
<v:f eqn="sum height 0 #1"/>
<v:f eqn="sum 10800 0 #1"/>
<v:f eqn="sum width 0 #0"/>
<v:f eqn="prod @4 @3 10800"/>
<v:f eqn="sum width 0 @5"/>
</v:formulas>
<v:handles>
<v:h position="#0,#1" xrange="0,21600" yrange="0,10800"/>
</v:handles>
</v:shape>
```





Notice that the only difference between the preceding VML representation and the following one is the **adj** value.

![shape2.gif (1361 bytes)](images/shape2h.gif)


```HTML
<v:shape style='width:90pt;height:54pt;'strokecolor="red"
strokeweight="2pt" coordsize="21600,21600" adj="11304,6600"
path="m@0,0l@0@1,0@1,0@2@0@2@0,21600,21600,10800xe">
<v:formulas>
<v:f eqn="val #0"/>
<v:f eqn="val #1"/>
<v:f eqn="sum height 0 #1"/>
<v:f eqn="sum 10800 0 #1"/>
<v:f eqn="sum width 0 #0"/>
<v:f eqn="prod @4 @3 10800"/>
<v:f eqn="sum width 0 @5"/>
</v:formulas>
<v:handles>
<v:h position="#0,#1" xrange="0,21600" yrange="0,10800"/>
</v:handles>
</v:shape>
```





For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858393) .

 

 