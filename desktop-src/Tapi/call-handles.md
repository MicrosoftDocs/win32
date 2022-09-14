---
description: As is mentioned in the Session Identifier overview, a call handle is the means by which a TAPI 2.2 application identifies a particular communications session.
ms.assetid: 5f6a7adf-c074-4bf6-9828-76604eb7609c
title: Call Handles
ms.topic: article
ms.date: 05/31/2018
---

# Call Handles

As is mentioned in the [Session Identifier](./session-identifier-ovr.md) overview, a call handle is the means by which a TAPI 2.2 application identifies a particular communications session. When an application initiates a session, TAPI returns a call handle for use in further operations or queries. When an application is notified of an incoming session, TAPI also passes in a call handle.

After a session has ended and the session state is idle, the call handle remains valid until the application deallocates the handle or the line is closed. The line might be closed by the application, or it may receive a [**LINE\_CLOSE**](line-close.md) message. If a line is closed, all call handles to calls on the line instantly become invalid.

After a call reverts to the *idle* state, the application is still allowed to read the call's information structure and status. This enables applications to use operations such as [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo) to retrieve call information for logging purposes.

When the application has no further use for the handle of an idle call, it must call [**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall) to free system-allocated memory related to the call. TAPI allocates memory for each call for each application that has a handle to the call. It is likely that service providers will allocate memory to hold call information as well. Deallocation of an application's call handle allows the library and the service provider to reclaim these memory resources. An application's handle for a call becomes void after a successful deallocation.

The application must itself free memory related to the call that it allocated for its own purposes.

 

 
