---
description: Fonts from Multiple Resource Files
ms.assetid: 4625fe62-d55d-4828-9174-975a731a8f62
title: Fonts from Multiple Resource Files
ms.topic: article
ms.date: 05/31/2018
---

# Fonts from Multiple Resource Files

Typically, a font is contained in a single font resource file. However, the information for some fonts is spread among several files. For example, Type 1 multiple master fonts require two files:

-   .pfm for the font metrics
-   .pfb for the font bits

To add a font from multiple files to the system, use the [**AddFontResource**](/windows/win32/api/wingdi/nf-wingdi-addfontresourcea) or [**AddFontResourceEx**](/windows/win32/api/wingdi/nf-wingdi-addfontresourceexa) functions. The *lpszFilename* parameter in these functions must point to a string that contains the file names separated by the vertical bar or pipe ( \| ). For example, to specify abcxxxxx.pfm and abcxxxxx.pfb for a Type 1 font, use the string "abcxxxxx.pfm \| abcxxxxx.pfb."

[**AddFontResourceEx**](/windows/win32/api/wingdi/nf-wingdi-addfontresourceexa) differs from [**AddFontResource**](/windows/win32/api/wingdi/nf-wingdi-addfontresourcea) in that the application calling **AddFontResourceEx** can specify the font as private to itself or non-enumerable.

To add a font from a memory image, use [**AddFontMemResourceEx**](/windows/win32/api/wingdi/nf-wingdi-addfontmemresourceex). This allows an application to use a font that is embedded in a document or a webpage.

To remove a font that came from multiple resource files, call [**RemoveFontResource**](/windows/desktop/api/Wingdi/nf-wingdi-removefontresourcea) or [**RemoveFontResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-removefontresourceexa), depending on the function used to add the font. You must specify the same flags that were used to add the font. To remove a font that was added from a memory image, use [**RemoveFontMemResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-removefontmemresourceex).

Using a font that comes from multiple font-resource files is identical to using a font from a single resource file.

 

 
