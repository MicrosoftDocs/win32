---
title: Disadvantages
description: Disadvantages
ms.assetid: ce6885d9-7056-42bc-85d1-27ce32b1be5e
ms.topic: article
ms.date: 05/31/2018
---

# Disadvantages

In-process servers provide the speed and size advantage of an object handler with the editing capability of a local server. So why would you ever choose to implement your OLE application as a local server rather than an in-process server? There are several reasons:

-   Security. Only a local server has its address space isolated from that of the client. An in-process server shares the address space and process context of the client and can therefore be less robust in the face of faults or malicious programming.
-   Granularity. A local server can host multiple instances of its object across many different clients, sharing server state between objects in multiple clients in ways that would be difficult or impossible if implemented as an in-process server, which is simply a DLL loaded into each client.
-   Compatibility. If you choose to implement an in-process server, you relinquish compatibility with OLE 1, which does not support such servers. This will not be a consideration for many developers, but if it is, then it is of critical concern.
-   Inability to support links. An in-process server cannot serve as a link source. Since a DLL cannot run by itself, it cannot create a file object to be linked to.

Despite these disadvantages, an in-process server can be an excellent choice for its speed and size — if it fits all your other requirements.

## Related topics

<dl> <dt>

[Advantages](advantages.md)
</dt> <dt>

[In-Process Servers](in-process-servers.md)
</dt> </dl>

 

 




