---
Description: 'An RSM library request is a request for an operation to be performed on a library.'
ms.assetid: 'de2af387-c80e-4c29-bc44-2be819502f08'
title: Library Requests
---

# Library Requests

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

An RSM library request is a request for an operation to be performed on a library. When applications make a library request , RSM places these requests in a queue and processes them as resources become available. For example, a request to mount a tape in a library results in a mount work queue item, which might wait until a drive is available.

 

 



