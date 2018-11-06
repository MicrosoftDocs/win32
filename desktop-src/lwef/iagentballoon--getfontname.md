---
title: IAgentBalloon GetFontName
description: IAgentBalloon GetFontName
ms.assetid: 7d057571-bb6e-4b79-bc4a-5691779ace51
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontName(
   BSTR * pbszFontName  // address of variable for font displayed 
);                      // in word balloon
```

Retrieves the value for the font displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszFontName"></span><span id="pbszfontname"></span><span id="PBSZFONTNAME"></span>*pbszFontName*
</dt> <dd>

The address of a BSTR that receives the font name displayed in a word balloon.

</dd> </dl>

The default font used in a character word balloon is defined in the Microsoft Agent Character Editor. You can change it with [**IAgentBalloon::SetFontName**](https://www.bing.com/search?q=**IAgentBalloon::SetFontName**). The user can override the font setting for all characters using the Microsoft Agent property sheet.

 

 




