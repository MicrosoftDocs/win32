---
title: IAgentCharacter SetPosition
description: IAgentCharacter SetPosition
ms.assetid: cc47b537-8154-4dfb-93e1-5ac3c3b50788
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetPosition

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetPosition(
   long lLeft,  // screen coordinate of the left edge of character 
   long lTop    // screen coordinate of the top edge of character 
);
```

Sets the position of the character's animation frame.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="lLeft"></span><span id="lleft"></span><span id="LLEFT"></span>*lLeft*
</dt> <dd>

Screen coordinate of the character animation frame's left edge in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="lTop"></span><span id="ltop"></span><span id="LTOP"></span>*lTop*
</dt> <dd>

Screen coordinate of the character animation frame's top edge in pixels, relative to the screen origin (upper left).

</dd> </dl>

This property's setting applies to all clients of the character. Even though the character appears in an irregularly shaped region window, the location of the character is based on its rectangular animation frame.

> [!Note]  
> Unlike the [**MoveTo**](https://www.bing.com/search?q=**MoveTo**) method, this function is not queued.

 

## See Also

[**IAgentCharacter::GetPosition**](iagentcharacter--getposition.md)


 

 




