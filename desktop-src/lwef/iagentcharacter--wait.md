---
title: IAgentCharacter Wait
description: IAgentCharacter Wait
ms.assetid: 4edb9a47-9385-49da-83ff-144780853ae7
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Wait

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Wait(
   long dwReqID,    // request ID
   long * pdwReqID  // address of request ID
);
```

Holds the character's animation queue at the specified animation (request) until another request for another character completes.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwReqID"></span><span id="dwreqid"></span><span id="DWREQID"></span>*dwReqID*
</dt> <dd>

The ID of the request to wait for.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the **Wait** request ID.

</dd> </dl>

Use this method only when you support multiple (simultaneous) characters and want to sequence their interaction. (For a single character, each animation request is played sequentially--after the previous request completes.) If you have two characters and want one character's animation request to wait until the other character's animation completes, set the **Wait** method to the other character's animation request ID.

 

 




