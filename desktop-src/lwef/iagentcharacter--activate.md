---
title: IAgentCharacter Activate
description: IAgentCharacter Activate
ms.assetid: a81eb62d-709b-46b4-9ff2-c9017f7f853e
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Activate

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Activate(
   short sState, // topmost character or client setting
);
```

Sets whether a client is active or a character is topmost.

-   Returns S\_OK to indicate the operation was successful.
-   Returns S\_FALSE to indicate the operation was not successful.

<dl> <dt>

<span id="sState"></span><span id="sstate"></span><span id="SSTATE"></span>*sState*
</dt> <dd>

You can specify the following values for this parameter:



| Value | Description                   |
|-------|-------------------------------|
| 0     | Set as not the active client. |
| 1     | Set as the active client.     |
| 2     | Make the topmost character.   |



 

</dd> </dl>

When multiple characters are visible, only one of the characters receives speech input at a time. Similarly, when multiple client applications share the same character, only one of the clients receives mouse input (for example, Microsoft Agent control click or drag events) at a time. The character set to receive mouse and speech input is the topmost character and the client that receives input is the character's active client. (The topmost character's window also appears at the top of the character window's z-order.) Typically, the user determines which character is topmost by explicitly selecting it. However, topmost activation also changes when a character is shown or hidden (the character becomes or is no longer topmost, respectively.)

You can also use this method to explicitly manage when your client receives input directed to the character, such as when your application itself becomes active. For example, setting **State** to 2 makes the character topmost, and your client receives all mouse and speech input events generated from user interaction with the character. Therefore, it also makes your client the input-active client of the character. However, you can also set the active client for a character without making the character topmost, by setting **State** to 1. This enables your client to receive input directed to that character when the character becomes topmost. Similarly, you can set your client to not be the active client (to not receive input) when the character becomes topmost, by setting **State** to 0. You can determine if a character has other current clients using [**IAgentCharacter::HasOtherClients**](iagentcharacter--hasotherclients.md).

Avoid calling this method directly after a [**Show**](iagentcharacter--show.md) method. **Show** automatically sets the input-active client. When the character is hidden, the **Activate** call may fail, if it gets processed before the **Show** method completes.

Attempting to call this method with the **State** parameter set to 2 (when the specified character is hidden) will fail. Similarly, if you set **State** to 0, and your application is the only client, this call fails. A character must always have a topmost client.

> [!Note]  
> Calling this method with **State** set to 1 does not typically generate an [**AgentNotifySink::ActivateInputState**](https://www.bing.com/search?q=**AgentNotifySink::ActivateInputState**) event unless there are no other characters loaded or your application is already input-active.

 

## See Also

[**IAgentCharacter::HasOtherClients**](iagentcharacter--hasotherclients.md)


 

 




