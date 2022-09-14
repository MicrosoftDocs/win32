---
description: There are other circumstances where a read or write operation can be completed with fewer than the requested number of characters, even though a time-out has not occurred.
ms.assetid: 05f84661-34ff-4e1f-9ec8-e4682138dfee
title: Communications Errors
ms.topic: article
ms.date: 05/31/2018
---

# Communications Errors

There are other circumstances where a read or write operation can be completed with fewer than the requested number of characters, even though a time-out has not occurred. Following are some examples:

-   Some drivers support the use of special characters, which complete a read operation immediately with only the characters that have been read up to the point when they are received.
-   The [**PurgeComm**](/windows/desktop/api/Winbase/nf-winbase-purgecomm) function can be called to prematurely terminate pending read or write operations. This function can also delete the contents of the output or input buffers, or both.
-   If a communications error occurs during a read or write operation, all I/O operations on the communications resource are terminated. Break conditions, parity errors, or framing errors are examples of such errors. When an error occurs, the process must call the [**ClearCommError**](/windows/desktop/api/Winbase/nf-winbase-clearcommerror) function to clear the error flag before it can begin additional I/O operations. **ClearCommError** reports the specific error that occurred and the current status of the device.

 

 



