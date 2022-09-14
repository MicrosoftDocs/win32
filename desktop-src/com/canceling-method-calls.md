---
title: Canceling Method Calls
description: With the introduction of distributed and Web-based applications, some method calls can take an unacceptably long time to return.
ms.assetid: 18228ff1-8c1c-430a-ae5f-0e9a56b0fe3c
ms.topic: article
ms.date: 05/31/2018
---

# Canceling Method Calls

With the introduction of distributed and Web-based applications, some method calls can take an unacceptably long time to return. The latency of the network connection may be high, the server machine may be serving many clients, or the server component may be passing a large amount of data, such as a multimedia file. Users should be able to cancel a request that is taking too long, and the application should be able to handle cancellation requests and continue with its other work. In COM, you can use the [**IMessageFilter**](/windows/desktop/api/ObjIdl/nn-objidl-imessagefilter) interface to cancel a pending call that originates from a single-threaded apartment.

When a call is marshaled, the proxy creates a cancel object, which implements the [**ICancelMethodCalls**](/windows/win32/api/objidlbase/nn-objidlbase-icancelmethodcalls) interface. The cancel object is associated with both the call and the thread on which the call is pending.

To cancel the pending call, the client passes a cancellation request through the cancel object, which handles the details of notifying the server object that the call has been canceled. If the called method has not returned, the server object, on detecting the cancellation request, cleans up any program resources it has allocated and notifies its client, by returning an appropriate **HRESULT** value, that it canceled execution of the call. If the called method has already returned, the cancel object notifies the client. In either case, the client thread is unblocked and can continue processing.

How the server object responds to a cancellation request is at the discretion of the server implementer, but the calling thread on the client will always be unblocked and will ignore whatever results the server tries to pass to it. Cancel objects provide a means to request that a currently running method be canceled, but there is no guarantee that the server object will stop processing the call. For example, the call may have already returned, or the server object may not support cancel objects.

COM automatically provides a standard implementation of cancel objects for client objects and interfaces that use standard marshaling. For objects and interfaces that use custom marshaling, you will need to implement your own cancel object.

At this time, cancel objects handle only synchronous calls.

## Related topics

<dl> <dt>

[Canceling an Asynchronous Call](canceling-an-asynchronous-call.md)
</dt> <dt>

[**CoGetCancelObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetcancelobject)
</dt> <dt>

[**CoSetCancelObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetcancelobject)
</dt> <dt>

[**CoTestCancel**](/windows/desktop/api/combaseapi/nf-combaseapi-cotestcancel)
</dt> </dl>

 

 