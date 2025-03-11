---
description: Since sockets are not represented by the UNIX-style, small, non-negative integer, the implementation of the select function was changed in Windows Sockets.
ms.assetid: 97c7996c-c541-4673-b26f-d66f3fc0b62e
title: Select, fd_set, and FD_XXX Macros
ms.topic: reference
ms.date: 05/31/2018
---

# Select, fd\_set, and FD\_XXX Macros

Since sockets are not represented by the UNIX-style, small, non-negative integer, the implementation of the [**select**](/windows/desktop/api/winsock2/nf-winsock2-select) function was changed in Windows Sockets. Each set of sockets is still represented by the [**fd\_set**](/windows/desktop/api/winsock2/ns-winsock2-fd_set) structure, but instead of being stored as a bitmask, the set is implemented as an array of sockets. To avoid potential problems, applications must adhere to the use of the FD\_XXX macros to set ([**FD_SET**](/windows/desktop/api/winsock2/nf-winsock2-fd_set)), initialize (**FD_ZERO**), clear (**FD_CLR**), and check (**FD_ISSET**) the **fd\_set** structures.

## Related topics

<dl> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



