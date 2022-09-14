---
title: IAgentNotifySink RequestStart
description: IAgentNotifySink RequestStart
ms.assetid: acac2bf8-7472-4952-a984-a29654fb8b0b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::RequestStart

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT RequestStart(
   long dwRequestID  // request ID
);                          
```

Notifies a client application when a request begins.

-   No return value.

<dl> <dt>

<span id="dwRequestID"></span><span id="dwrequestid"></span><span id="DWREQUESTID"></span>*dwRequestID*
</dt> <dd>

Identifier of the request that started.

</dd> </dl>

This event enables you to track when a queued request begins using its request ID.

## See Also

[**IAgentNotifySink::RequestComplete**](iagentnotifysink--requestcomplete.md), [**IAgent::Load**](iagent--load.md), [**IAgentCharacter::GestureAt**](iagentcharacter--gestureat.md), [**IAgentCharacter::Hide**](iagentcharacter--hide.md), [**IAgentCharacter::Interrupt**](iagentcharacter--interrupt.md), [**IAgentCharacter::MoveTo**](iagentcharacter--moveto.md), [**IAgentCharacter::Prepare**](iagentcharacter--prepare.md), [**IAgentCharacter::Play**](iagentcharacter--play.md), [**IAgentCharacter::Show**](iagentcharacter--show.md), [**IAgentCharacter::Speak**](iagentcharacter--speak.md), [**IAgentCharacter::Wait**](iagentcharacter--wait.md)


 

 




