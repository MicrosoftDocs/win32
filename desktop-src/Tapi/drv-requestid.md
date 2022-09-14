---
description: The DRV\_REQUESTID datatype is used to supply a unique identifier for a request to the service provider.
ms.assetid: cef6a42a-2e40-4f65-8fab-79cfba143206
title: DRV_REQUESTID
ms.topic: article
ms.date: 05/31/2018
---

# DRV\_REQUESTID

The **DRV\_REQUESTID** datatype is used to supply a unique identifier for a request to the service provider. A value of this type is passed as a parameter to every function that allows for asynchronous operation. If the operation is asynchronous, the service provider returns this value as the return value of the function. Whenever the service provider flags a request as asynchronous in this way, it must eventually report the operation is complete by calling the [*Completion\_Proc*](/windows/win32/api/tspi/nc-tspi-async_completion) callback function.

TAPI ensures that the **DRV\_REQUESTID** values it supplies are strictly positive, that is, between the values of 0x00000001 and 0x7FFFFFFF, inclusive. Furthermore, the values are unique in that no value returned from a function to flag the request as asynchronous will be re-used before the operation is reported complete.

 

 
