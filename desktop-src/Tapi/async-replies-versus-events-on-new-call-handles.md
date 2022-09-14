---
description: TSPI includes a number of operations that start the lifetime of a call handle.
ms.assetid: 28e171a3-db47-40fd-9c5a-d7b76d834a99
title: Async Replies versus Events on New Call Handles
ms.topic: article
ms.date: 05/31/2018
---

# Async Replies versus Events on New Call Handles

TSPI includes a number of operations that start the lifetime of a call handle. If the service provider returns SUCCESS for such an operation, it must fill in the opaque handle of type **HDRVCALL**, which it uses for the new call before it returns. TAPI never performs operations on the call before the matching [*Completion\_Proc*](/windows/win32/api/tspi/nc-tspi-async_completion) has been received. If the service provider returns FAILURE, the handle automatically becomes invalid (that is, without [**TSPI\_lineCloseCall**](/windows/win32/api/tspi/nf-tspi-tspi_lineclosecall)). In effect, TAPI treats the handle as "not yet valid" until the asynchronous completion.

The service provider must also treat the handle as "not yet valid" until after the matching [*Completion\_Proc*](/windows/win32/api/tspi/nc-tspi-async_completion) is received. In other words, it must not issue any [*Line\_Event*](/windows/win32/api/tspi/nc-tspi-lineevent) functions for the new call or include it in call counts in messages or status data structures for the line.

The TAPI level also conforms to these life cycle restrictions; a new call handle is not returned or valid until the matching [**LINE\_REPLY**](./line-reply.md) message, and no events for the new call are delivered to the application until after the LINE\_REPLY message.

The TSPI operations to which this "start lifetime" principle applies are the following:

-   [**TSPI\_lineCompleteTransfer**](/windows/win32/api/tspi/nf-tspi-tspi_linecompletetransfer)
-   [**TSPI\_lineForward**](/windows/win32/api/tspi/nf-tspi-tspi_lineforward)
-   [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall)
-   [**TSPI\_linePickup**](/windows/win32/api/tspi/nf-tspi-tspi_linepickup)
-   [**TSPI\_linePrepareAddToConference**](/windows/win32/api/tspi/nf-tspi-tspi_lineprepareaddtoconference)
-   [**TSPI\_lineSetupConference**](/windows/win32/api/tspi/nf-tspi-tspi_linesetupconference)
-   [**TSPI\_lineSetupTransfer**](/windows/win32/api/tspi/nf-tspi-tspi_linesetuptransfer)
-   [**TSPI\_lineUnpark**](/windows/win32/api/tspi/nf-tspi-tspi_lineunpark)

 

 
