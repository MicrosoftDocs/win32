---
title: IAgentNotifySink Size
description: IAgentNotifySink Size
ms.assetid: ef192234-bee6-4158-a5d8-4326b784e6cb
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::Size

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Size(
   long dwCharID,  // character ID
   long lWidth,    // new width
   long lHeight,   // new height
);                          
```

Notifies a client application when the character has been resized.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the character that has been resized.

</dd> <dt>

<span id="lWidth"></span><span id="lwidth"></span><span id="LWIDTH"></span>*lWidth*
</dt> <dd>

The width of the character's animation frame in pixels.

</dd> <dt>

<span id="lHeight"></span><span id="lheight"></span><span id="LHEIGHT"></span>*lHeight*
</dt> <dd>

The height of the character's animation frame in pixels.

</dd> </dl>

This event is sent to all clients of the character.

## See Also

[**IAgentCharacter::GetSize**](iagentcharacter--getsize.md), [**IAgentCharacter::SetSize**](iagentcharacter--setsize.md)


 

 




