---
title: Single-Threaded Apartments
description: Single-Threaded Apartments
ms.assetid: 2f345ae2-8314-4067-a6d6-5a0275941ed4
ms.topic: article
ms.date: 05/31/2018
---

# Single-Threaded Apartments

Using single-threaded apartments (the apartment model process) offers a message-based paradigm for dealing with multiple objects running concurrently. It enables you to write more efficient code by allowing a thread, while it waits for some time-consuming operation to complete, to allow another thread to be executed.

Each thread in a process that is initialized as an apartment model process, and that retrieves and dispatches window messages, is a single-threaded apartment thread. Each thread lives within its own apartment. Within an apartment, interface pointers can be passed without marshaling, and therefore, all objects in one single-threaded apartment thread communicate directly.

A logical grouping of related objects that all execute on the same thread, and therefore must have synchronous execution, could live on the same single-threaded apartment thread. However, an apartment model object cannot reside on more than one thread. Calls to objects in other threads must be made within the context of the owning thread, so distributed COM switches threads for you automatically when you call on a proxy.

The interprocess and interthread models are similar. When it is necessary to pass an interface pointer to an object in another apartment (on another thread) within the same process, you use the same marshaling model that objects in different processes use to pass pointers across process boundaries. By getting a pointer to the standard marshaling object, you can marshal interface pointers across thread boundaries (between apartments) in the same way you do between processes. (Interface pointers must be marshaled when passed between apartments.)

Rules for single-threaded apartments are simple, but it is important to follow them carefully:

-   Every object should live on only one thread (within a single-threaded apartment).
-   Initialize the COM library for each thread.
-   Marshal all pointers to objects when passing them between apartments.
-   Each single-threaded apartment must have a message loop to handle calls from other processes and apartments within the same process. Single-threaded apartments without objects (client only) also need a message loop to dispatch the broadcast messages that some applications use.
-   DLL-based or in-process objects do not call the COM initialization functions; instead, they register their threading model with the **ThreadingModel** named-value under the [InprocServer32](inprocserver32.md) key in the registry. Apartment-aware objects must also write DLL entry points carefully. There are special considerations that apply to threading in-process servers. For more information, see [In-Process Server Threading Issues](in-process-server-threading-issues.md).

While multiple objects can live on a single thread, no apartment model object can live on more than one thread.

Each thread of a client process or out-of-process server must call [**CoInitialize**](/windows/desktop/api/Objbase/nf-objbase-coinitialize), or call [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) and specify COINIT\_APARTMENTTHREADED for the *dwCoInit* parameter. The main apartment is the thread that calls **CoInitializeEx** first. For information on in-process servers, see [In-Process Server Threading Issues](in-process-server-threading-issues.md).

All calls to an object must be made on its thread (within its apartment). It is forbidden to call an object directly from another thread; using objects in this free-threaded manner could cause problems for applications. The implication of this rule is that all pointers to objects must be marshaled when passed between apartments. COM provides the following two functions for this purpose:

-   [**CoMarshalInterThreadInterfaceInStream**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterthreadinterfaceinstream) marshals an interface into a stream object that is returned to the caller.
-   [**CoGetInterfaceAndReleaseStream**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetinterfaceandreleasestream) unmarshals an interface pointer from a stream object and releases it.

These functions wrap calls to [**CoMarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterface) and [**CoUnmarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-counmarshalinterface) functions, which require the use of the MSHCTX\_INPROC flag.

In general, the marshaling is accomplished automatically by COM. For example, when passing an interface pointer as a parameter in a method call on a proxy to an object in another apartment, or when calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance), COM does the marshaling automatically. However, in some special cases, where the application writer is passing interface pointers between apartments without using the normal COM mechanisms, the writer must handle the marshaling manually.

If one apartment (Apartment 1) in a process has an interface pointer and another apartment (Apartment 2) requires its use, Apartment 1 must call [**CoMarshalInterThreadInterfaceInStream**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterthreadinterfaceinstream) to marshal the interface. The stream that is created by this function is thread-safe and must be stored in a variable that is accessible by Apartment 2. Apartment 2 must pass this stream to [**CoGetInterfaceAndReleaseStream**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetinterfaceandreleasestream) to unmarshal the interface and will get back a pointer to a proxy through which it can access the interface. The main apartment must remain alive until the client has completed all COM work (because some in-process objects are loaded in the main apartment, as described in [In-Process Server Threading Issues](in-process-server-threading-issues.md)). After one object has been passed between threads in this manner, it is very easy to pass interface pointers as parameters. That way, distributed COM does the marshaling and thread switching for the application.

To handle calls from other processes and apartments within the same process, each single-threaded apartment must have a message loop. This means that the thread's work function must have a GetMessage/DispatchMessage loop. If other synchronization primitives are being used to communicate between threads, the [**MsgWaitForMultipleObjects**](/windows/desktop/api/winuser/nf-winuser-msgwaitformultipleobjects) function can be used to wait both for messages and for thread synchronization events. The documentation for this function has an example of this sort of combination loop.

COM creates a hidden window using the Windows class "OleMainThreadWndClass" in each single-threaded apartment. A call to an object is received as a window message to this hidden window. When the object's apartment retrieves and dispatches the message, the hidden window will receive it. The window procedure will then call the corresponding interface method of the object.

When multiple clients call an object, the calls are queued in the message queue and the object will receive a call each time its apartment retrieves and dispatches messages. Because the calls are synchronized by COM and the calls are always delivered by the thread that belongs to the object's apartment, the object's interface implementations need not provide synchronization. Single-threaded apartments can implement [**IMessageFilter**](/windows/desktop/api/ObjIdl/nn-objidl-imessagefilter) to permit them to cancel calls or receive window messages when necessary.

The object can be reentered if one of its interface method implementations retrieves and dispatches messages or makes an ORPC call to another thread, thereby causing another call to be delivered to the object (by the same apartment). OLE does not prevent reentrancy on the same thread, but it can help provide thread safety. This is identical to the way in which a window procedure can be reentered if it retrieves and dispatches messages while processing a message. However, calling an out-of-process single-threaded apartment server that calls another single-threaded apartment server will allow the first server to be reentered.

## Related topics

<dl> <dt>

[Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)
</dt> <dt>

[Choosing the Threading Model](choosing-the-threading-model.md)
</dt> <dt>

[Multithreaded Apartments](multithreaded-apartments.md)
</dt> <dt>

[In-Process Server Threading Issues](in-process-server-threading-issues.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
</dt> </dl>

 

 