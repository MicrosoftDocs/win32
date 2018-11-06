---
title: IAgentBalloonEx SetNumCharsPerLine
description: IAgentBalloonEx SetNumCharsPerLine
ms.assetid: 44025b6b-ed42-4476-b841-c244accf0f83
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloonEx::SetNumCharsPerLine

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetNumCharsPerLine(
   long lCharsPerLine,  // number of characters per line setting
);
```

Sets the number of characters per line that can be displayed in the character's word balloon.

-   Returns S\_OK to indicate the operation was successful.
-   Returns E\_INVALIDARG if the parameter is less than eight.

<dl> <dt>

<span id="lCharsPerLine"></span><span id="lcharsperline"></span><span id="LCHARSPERLINE"></span>*lCharsPerLine*
</dt> <dd>

Number of lines to display in the word balloon.

</dd> </dl>

The minimum setting is 8 and the maximum is 255. If the text specified in the [**Speak**](speak-method.md) or [**Think**](think-method.md) method exceeds the size of the current balloon, Agent automatically scrolls the text in the balloon.

The default setting is based on settings when the character is compiled with the Microsoft Agent Character Editor.

## See Also

[**IAgentBalloon::GetNumCharsPerLine**](iagentballoon--getnumcharsperline.md)


 

 




