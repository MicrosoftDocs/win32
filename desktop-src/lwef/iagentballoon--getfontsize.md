---
title: IAgentBalloon GetFontSize
description: IAgentBalloon GetFontSize
ms.assetid: 4d342ee9-abb4-431b-bd28-f62ab76705ec
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetFontSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetFontSize(
   long * plFontSize  // address of variable for font size 
);                    // for font displayed in word balloon 
```

Retrieves the value for the size of the font displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plFontSize"></span><span id="plfontsize"></span><span id="PLFONTSIZE"></span>*plFontSize*
</dt> <dd>

The address of a value that receives the size of the font.

</dd> </dl>

The default font size used in a character word balloon is defined in the Microsoft Agent Character Editor. You can change it with [**IAgentBalloon::SetFontSize**](https://www.bing.com/search?q=**IAgentBalloon::SetFontSize**). However, the user can override the font size settings for all characters using the Microsoft Agent property sheet.

 

 




