---
title: Using the Background Element
description: Using the Background Element
ms.assetid: d11c1542-7f44-4ca7-9fb2-c8858fde3bc4
keywords:
- Web workshop,background element
- designing Web pages,background element
- Vector Markup Language (VML),background element
- VML (Vector Markup Language),background element
- vector graphics,background element
- background element
- VML elements,background
- VML shapes,background element
- Vector Markup Language (VML),customizing backgrounds
- VML (Vector Markup Language),customizing backgrounds
- vector graphics,customizing backgrounds
- VML shapes,customizing backgrounds
- customizing backgrounds
ms.topic: article
ms.date: 05/31/2018
---

# Using the Background Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

In this topic, we will illustrate how you can customize the background of a Web page by using the `<background>` element provided in VML.

As you've learned from the [Use `<fill>`](web-workshop---how-to-use-vml-on-web-pages-----fill--element.md) topic, you can place the `<fill>` sub-element inside the `<shape>`, `<shapetype>`, or any predefined shape element to describe how to fill the shape.

Similarly, you can place the `<fill>` sub-element inside the `<background>` element to describe how to fill the background of a Web page. You can then use the property attributes of the `<fill>` sub-element to customize the fill effect, such as [gradient fill](web-workshop---how-to-use-vml-on-web-pages-----fill--element.md), [pattern fill](web-workshop---how-to-use-vml-on-web-pages-----fill--element.md), or [picture fill](web-workshop---how-to-use-vml-on-web-pages-----fill--element.md).

For example, to draw a gradient-filled background, you can type the following lines in the `<BODY>` region of your Web page:


```HTML
<v:background fillcolor="red">
<v:fill type="gradient"/>
</v:background>
```





For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858389) .

 

 