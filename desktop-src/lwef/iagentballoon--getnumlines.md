---
title: IAgentBalloon GetNumLines
description: IAgentBalloon GetNumLines
ms.assetid: 82deeed0-d4a7-46e4-9077-edd933dcf4e2
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetNumLines

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetNumLines(
   long * pcLines  // address of variable for number of lines 
);                  // displayed in word balloon
```

Retrieves the value of the number of lines displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pcLines"></span><span id="pclines"></span><span id="PCLINES"></span>*pcLines*
</dt> <dd>

The address of a variable that receives the number of lines displayed.

</dd> </dl>

The Microsoft Agent server automatically scrolls the lines displayed for spoken output in the word balloon. The number of lines for a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application.

## See Also

[**IAgentBalloon::GetNumCharsPerLine**](iagentballoon--getnumcharsperline.md)


 

 




