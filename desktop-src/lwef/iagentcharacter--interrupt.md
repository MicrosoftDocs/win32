---
title: IAgentCharacter Interrupt
description: IAgentCharacter Interrupt
ms.assetid: ae05d317-e2d9-4d11-a6df-f9b25e43467a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Interrupt

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Interrupt(
   long dwReqID,    // request ID to interrupt
   long * pdwReqID  // address of request ID
);
```

Interrupts the specified animation (request) of another character.

-   Returns S\_OK to indicate the operation was successful. When the function returns, *pdwReqID* contains the ID of the request.

<dl> <dt>

<span id="dwReqID"></span><span id="dwreqid"></span><span id="DWREQID"></span>*dwReqID*
</dt> <dd>

An ID of the request to interrupt.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the **Interrupt** request ID.

</dd> </dl>

If you load multiple characters, you can use this method to sync up animation between characters. For example, if another character is in a looping animation, this method will stop the looping animation and start the next animation in the character's queue.

**Interrupt** halts the existing animation, but does not flush the character's animation queue. It starts the next animation in the character's queue. To halt and flush a character's queue, use the [**Stop**](/windows/desktop/lwef/iagentcharacter--stop) method.

You cannot use this method to have a character interrupt itself because the Microsoft Agent server queues the **Interrupt** method in the character's animation queue. Therefore, you can only use **Interrupt** to halt the animation of another character you have loaded.

 

 