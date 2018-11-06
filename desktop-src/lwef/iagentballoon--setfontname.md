---
title: IAgentBalloon SetFontName
description: IAgentBalloon SetFontName
ms.assetid: 6babf5f6-2abd-46c2-ade0-899a8e4488bd
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::SetFontName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetFontName(
   BSTR bszFontName  // font displayed in word balloon
);
                   
```

Sets the font displayed in the word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszFontName"></span><span id="bszfontname"></span><span id="BSZFONTNAME"></span>*bszFontName*
</dt> <dd>

A BSTR that sets the font displayed in the word balloon.

</dd> </dl>

The default font used in a character's word balloon is defined in the Microsoft Agent Character Editor. You can change it with **IAgentBalloon::SetFontName**. However, the user can override the font setting for all characters using the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::GetVisible**](iagentballoon--getvisible.md)


 

 




