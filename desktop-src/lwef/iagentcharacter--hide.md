---
title: IAgentCharacter Hide
description: IAgentCharacter Hide
ms.assetid: a8128fe8-9a3b-41a3-bfe3-82ace1baff6f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Hide

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Hide(
   long bFast,      // play Hiding state animation flag
   long * pdwReqID  // address of request ID
);
```

Hides the character.

-   Returns S\_OK to indicate the operation was successful. When the function returns, *pdwReqID* contains the ID of the request.

<dl> <dt>

<span id="bFast"></span><span id="bfast"></span><span id="BFAST"></span>*bFast*
</dt> <dd>

**Hiding** state animation flag. If this parameter is **True**, the **Hiding** animation does not play before the character frame is hidden; if **False**, the animation plays.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the **Hide** request ID.

</dd> </dl>

The server queues the animation associated with the **Hide** method in the character's queue. This allows you to use it to hide the character after a sequence of other animations. You can play the action immediately by using the [**Stop**](iagentcharacter--stop.md) method before calling the **Hide** method.

When using the HTTP protocol to access character and animation data, use the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method to ensure the availability of the **Hiding** state animation before calling this method.

Hiding a character can also result in triggering the [**IAgentNotifySink::ActivateInputState**](iagentnotifysink--activateinputstate.md) event of another visible character.

Hidden characters cannot access the audio channel. The server will pass back a failure status in the [**RequestComplete**](iagentnotifysink--requestcomplete.md) event if you generate an animation request and the character is hidden.

## See Also

[**IAgentCharacter::Show**](iagentcharacter--show.md)


 

 