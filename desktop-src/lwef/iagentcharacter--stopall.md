---
title: IAgentCharacter StopAll
description: IAgentCharacter StopAll
ms.assetid: cb0ce220-7b35-45c0-b587-30939d26740f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::StopAll

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT StopAll();
   long lType,  // request type
```

Stops all animations (requests) and removes them from the character's animation queue.

<dl> <dt>

<span id="lType"></span><span id="ltype"></span><span id="LTYPE"></span>*lType*
</dt> <dd>

A bitfield that indicates the types of requests to stop (and remove from the character's queue), comprised from the following:



| Value                                                                                  |  Description                                                                                                        |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **const unsigned long** **STOP\_TYPE\_ALL = 0xFFFFFFFF;**<br/>              | Stops all animation requests, including non-queued [**Prepare**](iagentcharacter--prepare.md) requests. |
| **const unsigned long** **STOP\_TYPE\_PLAY = 0x00000001;**<br/>             | Stops all Play requests.                                                                                 |
| **const unsigned long** **STOP\_TYPE\_MOVE = 0x00000002;**<br/>             | Stops all [**Move**](https://www.bing.com/search?q=**Move**) requests.                                               |
| **const unsigned long** **STOP\_TYPE\_SPEAK = 0x00000004;**<br/>            | Stops all [**Speak**](iagentcharacter--speak.md) requests.                                              |
| **const unsigned long** **STOP\_TYPE\_PREPARE = 0x00000008;**<br/>          | Stops all queued [**Prepare**](iagentcharacter--prepare.md) requests.                                   |
| **const unsigned long** **STOP\_TYPE\_NONQUEUEDPREPARE = 0x00000010;**<br/> | Stops all non-queued [**Prepare**](iagentcharacter--prepare.md) requests.                               |
| **const unsigned long** **STOP\_TYPE\_VISIBLE = 0x00000020;**<br/>          | Stops all [**Hide**](iagentcharacter--hide.md) or [**Show**](iagentcharacter--show.md) requests.       |



 

</dd> </dl>

## See Also

[**IAgentCharacter::Stop**](iagentcharacter--stop.md)


 

 





