---
title: IAgent
description: IAgent
ms.assetid: 35b12006-a938-450c-969a-7b73a3768a4d
ms.topic: article
ms.date: 05/31/2018
---

# IAgent

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

**IAgent** defines an interface that allows applications to load characters, receive events, and check the current state of the Microsoft Agent Server. These functions are also available from [**IAgentEx**](iagentex.md).

The GetSuspended method included in previous versions is obsolete and returns **False** for backward compatibility.

**Methods in Vtable Order**



| IAgent Methods                               | Description                                                   |
|----------------------------------------------|---------------------------------------------------------------|
| [**Load**](load-method.md)                  | Loads a character's data file.                                |
| [**Unload**](unload-method.md)              | Unloads a character's data file.                              |
| [**Register**](iagent--register.md)         | Registers a notification sink for the client.                 |
| [**Unegister**](iagent--unregister.md)      | Unregisters a client's notification sink.                     |
| [**GetCharacter**](iagent--getcharacter.md) | Returns the IAgentCharacter interface for a loaded character. |



 

 

 




