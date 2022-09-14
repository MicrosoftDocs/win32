---
title: IAgentBalloon GetFontUnderline
description: IAgentBalloon GetFontUnderline
ms.assetid: 19886e94-8095-4650-bd88-34ea9d96ddaa
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontUnderline

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontUnderline(
   long * pbFontUnderline  // address of variable for underline setting
);                         // for font displayed in word balloon 
```

Indicates whether the font used in a word balloon has the underline style set.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbFontUnderline"></span><span id="pbfontunderline"></span><span id="PBFONTUNDERLINE"></span>*pbFontUnderline*
</dt> <dd>

The address of a value that receives **True** if the font underline style is set and **False** if not.

</dd> </dl>

The font style used in a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can override the font settings for all characters using the Microsoft Agent property sheet.

 

 




