---
title: Using the Textbox Element
description: Using the Textbox Element
ms.assetid: e0022722-a504-47da-aa3f-62aa7fb4ac4d
keywords:
- Web workshop,textbox element
- designing Web pages,textbox element
- Vector Markup Language (VML),textbox element
- VML (Vector Markup Language),textbox element
- vector graphics,textbox element
- textbox element
- VML elements,textbox
- VML shapes,textbox element
- Vector Markup Language (VML),attaching text
- VML (Vector Markup Language),attaching text
- vector graphics,attaching text
- VML shapes,attaching text
- attaching text
ms.topic: article
ms.date: 05/31/2018
---

# Using the Textbox Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

## Examples:

To attach text to a rectangle, you can type the following lines in the `<BODY>` region of your Web page:


```HTML
<body>
<v:rect style='width:120pt;height:80pt;' fillcolor="red">
<v:textbox>
I'm attaching some text to this shape!!!
</v:textbox>
</v:rect>
</body>
```





To attach a hyperlink to a rounded rectangle that is gradient-filled, you can type the following lines in the `<BODY>` region of your Web page:

![textbox2.gif (1147 bytes)](images/textbox2.gif)


```HTML
<body>
<v:roundrect style='width:80pt;height:30pt;' fillcolor="red">
<v:fill type="gradient" />
<v:textbox>
<a href="https://home.microsoft.com/"> Click here</a>
</v:textbox>
</v:roundrect>
</body>
```





For more information about this element, see the [VML specification](https://www.w3.org/TR/NOTE-VML#-toc416858397) .

 

 