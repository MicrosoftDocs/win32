---
description: Since sockets are not represented by the UNIX-style, small, non-negative integer, the implementation of the select function was changed in Windows Sockets.
ms.assetid: 97c7996c-c541-4673-b26f-d66f3fc0b62e
title: Select, FD_SET, and FD_XXX Macros
ms.topic: article
ms.date: 05/31/2018
---

# Select, FD\_SET, and FD\_XXX Macros

Since sockets are not represented by the UNIX-style, small, non-negative integer, the implementation of the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function was changed in Windows Sockets. Each set of sockets is still represented by the **FD\_SET** structure, but instead of being stored as a bitmask, the set is implemented as an array of sockets. To avoid potential problems, applications must adhere to the use of the FD\_XXX macros to set, initialize, clear, and check the [**FD\_SET**](/windows/desktop/api/winsock/nf-winsock-fd_set) structures.

## Related topics

<dl> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



