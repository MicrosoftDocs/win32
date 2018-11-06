---
title: IAgentCharacterEx GetOriginalSize
description: IAgentCharacterEx GetOriginalSize
ms.assetid: a27ae88f-3655-4375-b563-0cc320d012cb
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetOriginalSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetOriginalSize(
   long * plWidth,  // address of variable for character width 
   long * plHeight  // address of variable for character height
);
```

Retrieves the original size of the character's animation frame.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plWidth"></span><span id="plwidth"></span><span id="PLWIDTH"></span>*plWidth*
</dt> <dd>

Address of a variable that receives the original width of the character animation frame in pixels.

</dd> <dt>

<span id="plHeight"></span><span id="plheight"></span><span id="PLHEIGHT"></span>*plHeight*
</dt> <dd>

Address of a variable that receives the original height of the character animation frame in pixels.

</dd> </dl>

This call returns the original size of the character frame as built in the Microsoft Agent Character Editor.

## See Also

[**IAgentCharacter::GetSize**](iagentcharacter--getsize.md)


 

 




