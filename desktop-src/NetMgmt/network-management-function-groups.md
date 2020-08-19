---
title: Network Management Function Groups
description: The network management functions can be divided into the following groups.
ms.assetid: 4b5d3554-f81a-4ecf-bf31-ee4753509f38
ms.topic: article
ms.date: 05/31/2018
---

# Network Management Function Groups

The network management functions can be divided into the following groups:

-   [Alert functions](alert-functions.md)
-   [ApiBuffer functions](apibuffer-functions.md)
-   [Directory Service functions](directory-service-functions.md)
-   [Distributed File System (Dfs) functions](/previous-versions/windows/desktop/dfs/distributed-file-system-dfs-functions)
-   [Get functions](get-functions.md)
-   [Group functions](group-functions.md)
-   [Local group functions](local-group-functions.md)
-   [Message functions](message-functions.md)
-   [NetFile functions](netfile-functions.md)
-   [Remote Utility functions](remote-utility-functions.md)
-   [Schedule functions](schedule-functions.md)
-   [Server functions](server-functions.md)
-   [Server and workstation transport functions](server-and-workstation-transport-functions.md)
-   [Session functions](session-functions.md)
-   [Share functions](share-functions.md)
-   [Statistics functions](/windows/desktop/NetShare/statistics-functions)
-   [Use functions](use-functions.md)
-   [User functions](user-functions.md)
-   [User modal functions](user-modal-functions.md)
-   [Workstation and workstation user functions](workstation-and-workstation-user-functions.md)

If you are programming for Active Directory, you may be able to call certain ADSI interface methods to achieve the same functionality you can achieve by calling certain network management functions. For more information, see [Mapping ADSI Interfaces to the Network Management Functions](mapping-adsi-interfaces-to-the-network-management-functions.md).

The system also provides a network-independent set of network functions ([WNet functions](/windows/desktop/WNet/wnet-functions)) that allow network functions to work across different network vendors' products. If your application could be converted to use a WNet function, you should perform the conversion. There are reasons to make the change:

-   The WNet functions are network independent, while the network management functions work only on Microsoft networks.
-   Some of the functions may not be supported in future releases of Microsoft operating systems if they have been superseded. Microsoft does not plan to remove specific functions unless equivalent or better functionality is available.

 

 