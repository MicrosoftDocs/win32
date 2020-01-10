---
Description: TSPI includes a number of operations that start the lifetime of a call handle.
ms.assetid: 28e171a3-db47-40fd-9c5a-d7b76d834a99
title: Async Replies versus Events on New Call Handles
ms.topic: article
ms.date: 05/31/2018
---

# Async Replies versus Events on New Call Handles

TSPI includes a number of operations that start the lifetime of a call handle. If the service provider returns SUCCESS for such an operation, it must fill in the opaque handle of type **HDRVCALL**, which it uses for the new call before it returns. TAPI never performs operations on the call before the matching [*Completion\_Proc*](https://msdn.microsoft.com/library/ms725180(v=VS.85).aspx) has been received. If the service provider returns FAILURE, the handle automatically becomes invalid (that is, without [**TSPI\_lineCloseCall**](https://msdn.microsoft.com/library/ms725532(v=VS.85).aspx)). In effect, TAPI treats the handle as "not yet valid" until the asynchronous completion.

The service provider must also treat the handle as "not yet valid" until after the matching [*Completion\_Proc*](https://msdn.microsoft.com/library/ms725180(v=VS.85).aspx) is received. In other words, it must not issue any [*Line\_Event*](https://msdn.microsoft.com/library/ms725228(v=VS.85).aspx) functions for the new call or include it in call counts in messages or status data structures for the line.

The TAPI level also conforms to these life cycle restrictions; a new call handle is not returned or valid until the matching [**LINE\_REPLY**](https://msdn.microsoft.com/library/ms736570(v=VS.85).aspx) message, and no events for the new call are delivered to the application until after the LINE\_REPLY message.

The TSPI operations to which this "start lifetime" principle applies are the following:

-   [**TSPI\_lineCompleteTransfer**](https://msdn.microsoft.com/library/ms725535(v=VS.85).aspx)
-   [**TSPI\_lineForward**](https://msdn.microsoft.com/library/ms725546(v=VS.85).aspx)
-   [**TSPI\_lineMakeCall**](https://msdn.microsoft.com/library/ms725576(v=VS.85).aspx)
-   [**TSPI\_linePickup**](https://msdn.microsoft.com/library/ms725585(v=VS.85).aspx)
-   [**TSPI\_linePrepareAddToConference**](https://msdn.microsoft.com/library/ms725586(v=VS.85).aspx)
-   [**TSPI\_lineSetupConference**](https://msdn.microsoft.com/library/ms725608(v=VS.85).aspx)
-   [**TSPI\_lineSetupTransfer**](https://msdn.microsoft.com/library/ms725609(v=VS.85).aspx)
-   [**TSPI\_lineUnpark**](https://msdn.microsoft.com/library/ms725613(v=VS.85).aspx)

 

 



