---
title: IAgentBalloon GetFontStrikethru
description: IAgentBalloon GetFontStrikethru
ms.assetid: b5c253e8-dca7-44a6-b63b-a33e6e793a40
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontStrikethru

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontStrikethru(
   long * pbFontStrikethru  // address of variable for strikethrough setting 
);                          // for font displayed in word balloon 
```

Indicates whether the font used in a word balloon has the strikethrough style set.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbFontStrikethru"></span><span id="pbfontstrikethru"></span><span id="PBFONTSTRIKETHRU"></span>*pbFontStrikethru*
</dt> <dd>

The address of a value that receives **True** if the font strikethrough style is set and **False** if not.

</dd> </dl>

The font style used in a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can override the font settings for all characters using the Microsoft Agent property sheet.

 

 




