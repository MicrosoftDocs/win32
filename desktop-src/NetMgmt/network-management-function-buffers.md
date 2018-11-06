---
title: Network Management Function Buffers
description: The RPC run-time library handles the buffers required by the 32-bit data retrieval network management functions as follows.
ms.assetid: f27e6cf5-f26a-4e6c-8d77-873bff6cc8e4
ms.topic: article
ms.date: 05/31/2018
---

# Network Management Function Buffers

The RPC run-time library handles the buffers required by the 32-bit data retrieval network management functions as follows:

-   **Sending data to the server** (data specified by \[in\] parameters).

    The caller must allocate and deallocate the buffer for the relevant information structure (or structures) and pass a pointer variable to the function. The caller does not need to specify the buffer length.

    Example: [**NetGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupadd)

-   **Retrieving data from the server** (data specified by \[out\] parameters).

    The system allocates the buffer for the returned information. The caller must pass a pointer variable to the function on input. On successful return, the pointer receives the address of the system-allocated buffer that contains the returned information. This simplifies the calling code, because the caller does not need to estimate the size of the buffer, or resize the buffer and reissue the function.

    When the caller has finished processing the returned information, it must free the system-allocated memory by calling the [**NetApiBufferFree**](/windows/desktop/api/Lmapibuf/nf-lmapibuf-netapibufferfree) function. For more information about specifying buffer sizes, see [Network Management Function Buffer Lengths](network-management-function-buffer-lengths.md).

    Example: [**NetGroupEnum**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgroupenum)

 

 




