---
title: IAgentCharacter SetSize
description: IAgentCharacter SetSize
ms.assetid: 8324ab84-2b59-4459-b375-700d72b621bc
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetSize(
   long * lWidth,  // width of the character frame
   long * lHeight  // height of the character frame
);
```

Sets the size of the character's animation frame.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="lWidth"></span><span id="lwidth"></span><span id="LWIDTH"></span>*lWidth*
</dt> <dd>

The width of the character's animation frame in pixels.

</dd> <dt>

<span id="lHeight"></span><span id="lheight"></span><span id="LHEIGHT"></span>*lHeight*
</dt> <dd>

The height of the character's animation frame in pixels.

</dd> </dl>

Changing the character's frame size scales the character to the size set with this method. This property's setting applies to all clients of the character.

Even though the character appears in an irregularly shaped region window, the location of the character is based on its rectangular animation frame.

## See Also

[**IAgentCharacter::GetSize**](iagentcharacter--getsize.md)


 

 




