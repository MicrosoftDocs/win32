---
title: IAgentCharacter GetSize
description: IAgentCharacter GetSize
ms.assetid: bc2d6fe4-5945-4a35-b603-409c66f8aa2a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSize(
   long * plWidth,  // address of variable for character width 
   long * plHeight  // address of variable for character height
);
```

Retrieves the size of the character's animation frame.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plWidth"></span><span id="plwidth"></span><span id="PLWIDTH"></span>*plWidth*
</dt> <dd>

Address of a variable that receives the width of the character animation frame in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="plHeight"></span><span id="plheight"></span><span id="PLHEIGHT"></span>*plHeight*
</dt> <dd>

Address of a variable that receives the height of the character animation frame in pixels, relative to the screen origin (upper left).

</dd> </dl>

Even though the character appears in an irregularly shaped region window, the location of the character is based on its rectangular animation frame.

## See Also

[**IAgentCharacter::SetSize**](iagentcharacter--setsize.md)


 

 




