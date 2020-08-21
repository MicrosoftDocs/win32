---
title: The Balloon Object
description: The Balloon Object
ms.assetid: d5b52310-0b4e-4fe3-a481-53687be4a89c
ms.topic: article
ms.date: 05/31/2018
---

# The Balloon Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Microsoft Agent supports textual captioning of [**Speak**](speak-method.md) method using a cartoon word balloon. The [**Think**](think-method.md) method enables you to display text without audio output in a "thought" word balloon.

A character's initial word balloon window defaults are defined and compiled in the Microsoft Agent Character Editor. Once running, the balloon's [**Enabled**](enabled-property.md) and [**Font**](https://www.bing.com/search?q=**Font**) properties may be overridden by the user. If a user changes the word balloon's properties, they affect all characters. Both the [**Speak**](speak-method.md) and [**Think**](think-method.md) word balloons use the same property settings for size. You can access the properties for a character's word balloon through the [**Balloon**](/windows/desktop/lwef/the-balloon-object) object, which is a child of the [**Character**](/windows/desktop/lwef/the-characters-object) object.

The [**Balloon**](/windows/desktop/lwef/the-balloon-object) object supports the following properties:

-   [**BackColor**](backcolor-property.md)
-   [**BorderColor**](bordercolor-property.md)
-   [**CharsPerLine**](charsperline-property.md)
-   [**Enabled**](enabled-property.md)
-   [**FontCharSet**](fontcharset-property.md)
-   [**FontName**](fontname-property-bal.md)
-   [**FontBold**](fontbold-property.md)
-   [**FontItalic**](fontitalic-property.md)
-   [**FontSize**](fontsize-property-bal.md)
-   [**FontStrikeThru**](fontstrikethru-property.md)
-   [**FontUnderline**](fontunderline-property.md)
-   [**ForeColor**](forecolor-property.md)
-   [**NumberOfLines**](numberoflines-property.md)
-   [**Style**](style-property.md)
-   [**Visible**](visible-property-bal.md)

 

 