---
title: IAgentNotifySink Idle
description: IAgentNotifySink Idle
ms.assetid: 7770a698-31d9-4f3a-9c7e-858c480b640e
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::Idle

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Idle(
   long dwCharID,  // character ID
   long bStart     // start flag
);                          
```

Notifies a client application when a character's **Idling** state has changed.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the request that started.

</dd> <dt>

<span id="bStart"></span><span id="bstart"></span><span id="BSTART"></span>*bStart*
</dt> <dd>

Start flag. This Boolean value is **True** when the character begins idling and **False** when it stops idling.

</dd> </dl>

This event enables you to track when the Microsoft Agent server starts or stops idle processing for a character.

## See Also

[**IAgentCharacter::GetIdleOn**](iagentcharacter--getidleon.md), [**IAgentCharacter::SetIdleOn**](iagentcharacter--setidleon.md)


 

 




