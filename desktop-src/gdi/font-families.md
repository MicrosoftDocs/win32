---
description: A font family is a set of fonts having common stroke width and serif characteristics. There are five font families. A sixth family allows an application to use the default font. The following table describes the font-families.
ms.assetid: 3c462000-4f65-43d0-8937-059081a8c417
title: Font Families
ms.topic: article
ms.date: 05/31/2018
---

# Font Families

A *font family* is a set of fonts having common stroke width and serif characteristics. There are five font families. A sixth family allows an application to use the default font. The following table describes the font-families.



| Font family | Description                                                                                                                                   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Decorative  | Specifies a novelty font. An example is Old English.                                                                                          |
| Dontcare    | Specifies a generic family name. This name is used when information about a font does not exist or does not matter. The default font is used. |
| Modern      | Specifies a monospace font with or without serifs. Monospace fonts are usually modern; examples include Pica, Elite, and Courier New.         |
| Roman       | Specifies a proportional font with serifs. An example is Times New Roman.                                                                     |
| Script      | Specifies a font that is designed to look like handwriting; examples include Script and Cursive.                                              |
| Swiss       | Specifies a proportional font without serifs. An example is Arial.                                                                            |



 

These font families correspond to constants found in the Wingdi.h file: FF\_DECORATIVE, FF\_DONTCARE, FF\_MODERN, FF\_ROMAN, FF\_SCRIPT, and FF\_SWISS. An application uses these constants when it creates a font, selects a font, or retrieves information about a font.

Fonts within a family are distinguished by size (10 point, 24 point, and so on) and style (regular, italic, and so on).

 

 



