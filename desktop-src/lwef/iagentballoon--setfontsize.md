---
title: IAgentBalloon SetFontSize
description: IAgentBalloon SetFontSize
ms.assetid: c38779a6-bd7f-4d3a-9cb0-9d9fac1c7996
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::SetFontSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetFontSize(
   long lFontSize  // font size displayed in word balloon
); 
```

Sets the size of the font displayed in the word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="lFontSize"></span><span id="lfontsize"></span><span id="LFONTSIZE"></span>*lFontSize*
</dt> <dd>

The size of the font.

</dd> </dl>

The default font size used in a character's word balloon is defined in the Microsoft Agent Character Editor. You can change it with **IAgentBalloon::SetFontSize**. However, the user can override the font size setting for all characters using the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::GetFontSize**](iagentballoon--getfontsize.md)


 

 




