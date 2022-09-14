---
title: Making and Processing Asynchronous Calls
description: COM objects can support asynchronous calling.
ms.assetid: bf7f9f8e-66ce-41a4-854c-62dbe840a89e
ms.topic: article
ms.date: 05/31/2018
---

# Making and Processing Asynchronous Calls

COM objects can support asynchronous calling. When a client makes an asynchronous call, control returns to the client immediately. While the server processes the call, the client is free to do other work. When the client can no longer proceed without the results of the call, it can get the results of the call at that time.

For example, a request for a large or complex recordset can be time-consuming. A client can request the recordset by an asynchronous call and then do other work. When the recordset is available, the client can obtain it quickly without blocking.

Clients do not make asynchronous calls directly on the server object. Instead, they obtain a call object that implements an asynchronous version of a synchronous interface on the server object. The asynchronous interface on the call object has a name of the form Async*InterfaceName*. For example, if a server object implements a synchronous interface named IMyInterface, there will be a call object that implements an asynchronous interface named AsyncIMyInterface.

> [!Note]  
> Asynchronous support is not available for **IDispatch** or for interfaces that inherit **IDispatch**.

 

Server objects that support asynchronous calls implement the [**ICallFactory**](/windows/win32/api/objidlbase/nn-objidlbase-icallfactory) interface. This interface exposes a single method, [**CreateCall**](/windows/win32/api/objidlbase/nf-objidlbase-icallfactory-createcall), which creates an instance of a specified call object. Clients can query for **ICallFactory** to determine whether an object supports asynchronous calling.

For each method on a synchronous interface, the corresponding asynchronous interface implements two methods. These methods attach the prefixes Begin\_ and Finish\_ to the name of the synchronous method. For example, if an interface named ISimpleStream has a Read method, the AsyncISimpleStream interface will have a Begin\_Read and a Finish\_Read method. To begin an asynchronous call, the client calls the Begin\_ method.

When you implement a server object, you do not have to provide a call object for every interface the object implements. If the server object implements the [**ICallFactory**](/windows/win32/api/objidlbase/nn-objidlbase-icallfactory) interface and uses standard marshaling, a marshaled client can always obtain a proxy call object, even if there is no call object on the server side. This proxy will marshal the Begin\_ method as a synchronous call, the server will process the call synchronously, and the client can obtain the out parameters by calling the Finish\_ method.

Conversely, if a client makes a marshaled synchronous call on an interface for which there is a call object on the server side, the server will always process the call asynchronously. This behavior will not be apparent to the client, because the client will receive the same out parameters and the same return value it would have received from the synchronous method.

In either case, the interaction between client and server is marshaled as if the call were synchronous: The output of synchronous and asynchronous proxies is indistinguishable, as is the output of the corresponding stubs. This behavior greatly simplifies the programming model both of clients and of servers. If a server object implements [**ICallFactory**](/windows/win32/api/objidlbase/nn-objidlbase-icallfactory), a marshaled client does not have to attempt to create a call object that may not be available — to the client, a call object is always available.

When client and server are in the same apartment, the server object will process whichever call the client makes. If a call object is not available, the client must explicitly obtain the synchronous interface and make a synchronous call.

For more information, see the following topics:

-   [Making an Asynchronous Call](making-an-asynchronous-call.md)
-   [Canceling an Asynchronous Call](canceling-an-asynchronous-call.md)
-   [Canceling Method Calls](canceling-method-calls.md)
-   [Call Synchronization](call-synchronization.md)

 

 