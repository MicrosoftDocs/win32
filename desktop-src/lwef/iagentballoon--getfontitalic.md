---
title: IAgentBalloon GetFontItalic
description: IAgentBalloon GetFontItalic
ms.assetid: 03f40210-71b3-4488-9a44-5a9322db010a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontItalic

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontItalic(
   long * pbFontItalic  // address of variable for italic setting for 
);                      // font displayed in word balloon 
```

Indicates whether the font used in a word balloon is italic.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbFontItalic"></span><span id="pbfontitalic"></span><span id="PBFONTITALIC"></span>*pbFontItalic*
</dt> <dd>

The address of a value that receives **True** if the font is italic and **False** if not italic.

</dd> </dl>

The font style used in a character's word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can override the font settings for all characters through the Microsoft Agent property sheet.

 

 




