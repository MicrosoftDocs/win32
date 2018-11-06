---
title: IAgentBalloon GetNumCharsPerLine
description: IAgentBalloon GetNumCharsPerLine
ms.assetid: ae0c7fff-8c58-465e-9b4f-3260f7574b57
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetNumCharsPerLine

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetNumCharsPerLine(
   long * plCharsPerLine  // address of variable for characters per line
);                        // displayed in word balloon
```

Retrieves the value for the average number of characters per line displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbCharsPerLine"></span><span id="pbcharsperline"></span><span id="PBCHARSPERLINE"></span>*pbCharsPerLine*
</dt> <dd>

The address of a variable that receives the number of characters per line.

</dd> </dl>

The Microsoft Agent server automatically scrolls the lines displayed for spoken output in the word balloon. The average number of characters per line for a character's word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application.

## See Also

[**IAgentBalloon::GetNumLines**](iagentballoon--getnumlines.md)


 

 




