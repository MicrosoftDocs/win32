---
title: IAgentBalloon GetFontBold
description: IAgentBalloon GetFontBold
ms.assetid: 5a55f771-d68e-4f66-8001-47c141661b06
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontBold

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontBold(
   long * pbFontBold  // address of variable for bold setting for
);                    // font displayed in word balloon 
```

Indicates whether the font used in a word balloon is bold.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbFontBold"></span><span id="pbfontbold"></span><span id="PBFONTBOLD"></span>*pbFontBold*
</dt> <dd>

The address of a value that receives **True** if the font is bold and **False** if not bold.

</dd> </dl>

The font style used in a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can override the font settings for all characters through the Microsoft Agent property sheet.

 

 




