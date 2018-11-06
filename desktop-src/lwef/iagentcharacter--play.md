---
title: IAgentCharacter Play
description: IAgentCharacter Play
ms.assetid: a0158693-ff62-4da4-8b68-402e8d5b1c2a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Play

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Play(
   BSTR bszAnimation,  // name of an animation
   long * pdwReqID     // address of request ID
);
```

Plays the specified animation.

-   Returns S\_OK to indicate the operation was successful. When the function returns, *pdwReqID* contains the ID of the request.

<dl> <dt>

<span id="bszAnimation"></span><span id="bszanimation"></span><span id="BSZANIMATION"></span>*bszAnimation*
</dt> <dd>

The name of an animation.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the **IAgentCharacter::Play** request ID.

</dd> </dl>

An animation's name is defined when the character is compiled with the Microsoft Agent Character Editor. Before playing the specified animation, the server attempts to play the **Return** animation for the previous animation (if one has been assigned).

When a character's animation data is stored on the user's local machine, you can use the **IAgentCharacter::Play** method and specify the name of the animation. When using the HTTP protocol to access animation data, use the [**Prepare**](iagentcharacter--prepare.md) method to ensure the availability of the animation before calling this method.

## See Also

[**IAgentCharacter::Prepare**](iagentcharacter--prepare.md)


 

 




