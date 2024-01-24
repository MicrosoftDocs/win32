---
description: A mailslot is a pseudofile that resides in memory, and you use standard file functions to access it.
ms.assetid: 9a68905d-c235-4c72-bc71-1cccdf5cdadc
title: About Mailslots
ms.topic: article
ms.date: 05/31/2018
---

# About Mailslots

A mailslot is a pseudofile that resides in memory, and you use standard file functions to access it. The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and all the data it contains are deleted.

A *mailslot server* is a process that creates and owns a mailslot. When the server creates a mailslot, it receives a mailslot handle. This handle must be used when a process reads messages from the mailslot. Only the process that creates a mailslot or has obtained the handle by some other mechanism (such as inheritance) can read from the mailslot. All mailslots are local to the process that creates them. A process cannot create a remote mailslot.

A *mailslot client* is a process that writes a message to a mailslot. Any process that has the name of a mailslot can put a message there. New messages follow any existing messages in the mailslot.

Mailslots can broadcast messages within a domain. If several processes in a domain each create a mailslot using the same name, every message that is addressed to that mailslot and sent to the domain is received by the participating processes. Because one process can control both a server mailslot handle and the client handle retrieved when the mailslot is opened for a write operation, applications can easily implement a simple message-passing facility within a domain.

To send messages that are larger than 424 bytes between computers, use [named pipes](named-pipes.md) or [Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2) instead.

## Related topics

<dl> <dt>

[Mailslot Names](mailslot-names.md)
</dt> <dt>

[Mailslot Operations](mailslot-operations.md)
</dt> </dl>

 

 
