---
title: IAgentCharacter Stop
description: IAgentCharacter Stop
ms.assetid: 3064bb3e-37a6-4022-bffb-130735736889
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Stop

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Stop(
   long dwReqID  // request ID
);
```

Stops the specified animation (request) and removes it from the character's animation queue.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwReqID"></span><span id="dwreqid"></span><span id="DWREQID"></span>*dwReqID*
</dt> <dd>

The ID of the request to stop.

</dd> </dl>

**Stop** can also be used to halt any queued [**Prepare**](iagentcharacter--prepare.md) calls.

## See Also

[**IAgentCharacter::Prepare**](iagentcharacter--prepare.md), [**IAgentCharacter::StopAll**](iagentcharacter--stopall.md)


 

 




