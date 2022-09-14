---
title: Making an Asynchronous Call
description: The procedure for making a synchronous call is straightforward The client obtains an interface pointer on the server object and calls methods through that pointer. Asynchronous calling involves a call object, so it involves a few more steps.
ms.assetid: ab65d38d-836a-48d4-87c1-8812cbc8ff92
ms.topic: article
ms.date: 05/31/2018
---

# Making an Asynchronous Call

The procedure for making a synchronous call is straightforward: The client obtains an interface pointer on the server object and calls methods through that pointer. Asynchronous calling involves a call object, so it involves a few more steps.

For each method on a synchronous interface, the corresponding asynchronous interface implements two methods. These methods attach the prefixes Begin\_ and Finish\_ to the name of the synchronous method. For example, if an interface named ISimpleStream has a Read method, the AsyncISimpleStream interface will have a Begin\_Read and a Finish\_Read method. To begin an asynchronous call, the client calls the Begin\_ method.

**To begin an asynchronous call**

1.  Query the server object for the [**ICallFactory**](/windows/win32/api/objidlbase/nn-objidlbase-icallfactory) interface. If [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) returns E\_NOINTERFACE, the server object does not support asynchronous calling.

2.  Call [**ICallFactory::CreateCall**](/windows/win32/api/objidlbase/nf-objidlbase-icallfactory-createcall) to create a call object corresponding to the interface you want, and then release the pointer to [**ICallFactory**](/windows/win32/api/objidlbase/nn-objidlbase-icallfactory).

3.  If you did not request a pointer to the asynchronous interface from the call to [**CreateCall**](/windows/win32/api/objidlbase/nf-objidlbase-icallfactory-createcall), query the call object for the asynchronous interface.

4.  Call the appropriate Begin\_ method.

The server object is now processing the asynchronous call, and the client is free to do other work until it needs the results of the call.

A call object can process only one asynchronous call at a time. If the same or a second client calls a Begin\_ method before a pending asynchronous call is finished, the Begin\_ method will return RPC\_E\_CALL\_PENDING.

If the client does not need the results of the Begin\_ method, it can release the call object at the end of this procedure. COM detects this condition and cleans up the call. The Finish\_ method is not called, and the client does not get any out parameters or a return value.

When the server object is ready to return from the Begin\_ method, it signals the call object that it is done. When the client is ready, it checks to see whether the call object has been signaled. If so, the client can complete the asynchronous call.

The mechanism for this signaling and checking between client and server is the [**ISynchronize**](/windows/win32/api/objidlbase/nn-objidlbase-isynchronize) interface on the call object. The call object normally implements this interface by aggregating a system-supplied synchronization object. The synchronization object wraps an event handle, which the server signals just before returning from the Begin\_ method by calling [**ISynchronize::Signal**](/windows/win32/api/objidlbase/nf-objidlbase-isynchronize-signal).

**To complete an asynchronous call**

1.  Query the call object for the [**ISynchronize**](/windows/win32/api/objidlbase/nn-objidlbase-isynchronize) interface.

2.  Call [**ISynchronize::Wait**](/windows/win32/api/objidlbase/nf-objidlbase-isynchronize-wait).

3.  If [**Wait**](/windows/win32/api/objidlbase/nf-objidlbase-isynchronize-wait) returns RPC\_E\_TIMEOUT, the Begin\_ method is not finished processing. The client can continue with other work and call **Wait** again later. It cannot call the Finish\_ method until **Wait** returns S\_OK.

    If [**Wait**](/windows/win32/api/objidlbase/nf-objidlbase-isynchronize-wait) returns S\_OK, the Begin\_ method has returned. Call the appropriate Finish\_ method.

The Finish\_ method passes the client any out parameters. The behavior of the asynchronous methods, including the return value of the Finish\_ method, should match exactly that of the corresponding synchronous method.

The client can release the call object as soon as the Finish\_ method returns, or it can hold a pointer to the call object to make additional calls. In either case, the client is responsible for releasing the call object when the object is no longer needed.

If you call a Finish\_ method when no call is in progress, the method will return RPC\_E\_CALL\_COMPLETE.

> [!Note]  
> If the client and server objects are in the same apartment, calls to [**ICallFactory::CreateCall**](/windows/win32/api/objidlbase/nf-objidlbase-icallfactory-createcall) are not guaranteed to succeed. If the server object does not support asynchronous calling on a particular interface, the attempt to create a call object will fail and the client must use the synchronous interface.

 

## Related topics

<dl> <dt>

[Canceling an Asynchronous Call](canceling-an-asynchronous-call.md)
</dt> <dt>

[Client Security During an Asynchronous Call](client-security-during-an-asynchronous-call.md)
</dt> <dt>

[Impersonation and Asynchronous Calls](impersonation-and-asynchronous-calls.md)
</dt> </dl>

 

 