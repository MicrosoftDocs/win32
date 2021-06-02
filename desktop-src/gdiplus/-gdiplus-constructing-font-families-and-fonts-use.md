---
description: Windows GDI+ groups fonts with the same typeface but different styles into font families.
ms.assetid: 57428fae-6af4-47a5-a499-717dc378767a
title: Constructing Font Families and Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Constructing Font Families and Fonts

Windows GDI+ groups fonts with the same typeface but different styles into font families. For example, the Arial font family contains the following fonts:

-   Arial Regular
-   Arial Bold
-   Arial Italic
-   Arial Bold Italic

GDI+ uses four styles to form families: regular, bold, italic, and bold italic. Adjectives such as *narrow* and *rounded* are not considered styles; rather they are part of the family name. For example, Arial Narrow is a font family whose members are the following:

-   Arial Narrow Regular
-   Arial Narrow Bold
-   Arial Narrow Italic
-   Arial Narrow Bold Italic

Before you can draw text with GDI+, you need to construct a [**FontFamily**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-fontfamily) object and a [**Font**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-font) object. The **FontFamily** objects specifies the typeface (for example, Arial), and the **Font** object specifies the size, style, and units.

The following example constructs a regular style Arial font with a size of 16 pixels:


```
FontFamily fontFamily(L"Arial");
Font font(&fontFamily, 16, FontStyleRegular, UnitPixel);
            
```



In the preceding code, the first argument passed to the [**Font**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-font) constructor is the address of the [**FontFamily**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-fontfamily) object. The second argument specifies the size of the font measured in units identified by the fourth argument. The third argument identifies the style.

[****UnitPixel****](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-unit) is a member of the **Unit** enumeration, and [****FontStyleRegular****](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-fontstyle) is a member of the **FontStyle** enumeration. Both enumerations are declared in Gdiplusenums.h.

 

 



