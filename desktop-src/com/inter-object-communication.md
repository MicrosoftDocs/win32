---
title: Inter-Object Communication
description: COM is designed to allow clients to communicate transparently with objects, regardless of where those objects are running in the same process, on the same computer, or on a different computer.
ms.assetid: dd4adafb-a7e4-44ba-ae4a-80585875ecb6
ms.topic: article
ms.date: 05/31/2018
---

# Inter-Object Communication

COM is designed to allow clients to communicate transparently with objects, regardless of where those objects are running&mdash;in the same process, on the same computer, or on a different computer. This provides a single programming model for all types of objects, and for both object clients and object servers.

From a client's point of view, all objects are accessed through interface pointers. A pointer must be in-process. In fact, any call to an interface function always reaches some piece of in-process code first. If the object is in-process, the call reaches it directly, with no intervening system-infrastructure code. If the object is out-of-process, the call first reaches what is called a "proxy" object provided either by COM or by the object (if the implementor wishes). The proxy packages call parameters (including any interface pointers) and generate the appropriate remote procedure call (or other communication mechanism in the case of custom generated proxies) to the other process or the other computer where the object implementation is located. This process of packaging pointers for transmission across process boundaries is called *marshaling*.

From a server's point of view, all calls to an object's interface functions are made through a pointer to that interface. Again, a pointer has context only in a single process, and the caller must always be some piece of in-process code. If the object is in-process, the caller is the client itself. Otherwise, the caller is a "stub" object provided either by COM or by the object itself. The stub receives the remote procedure call (or other communication mechanism in the case of custom generated proxies) from the "proxy" in the client process, unmarshals the parameters, and calls the appropriate interface on the server object. From the points of view of both clients and servers, they always communicate directly with some other in-process code.

COM provides an implementation of marshaling, referred to as *standard marshaling*. This implementation works very well for most objects and greatly reduces programming requirements, making the marshaling process effectively transparent.

The clear separation of interface from implementation of COM's process transparency can, however, get in the way in some situations. The design of an interface that focuses on its function from the client's point of view can sometimes lead to design decisions that conflict with efficient implementation of that interface across a network. In cases like this, what is needed is not pure process transparency but "process transparency, unless you need to care." COM provides this capability by allowing an object implementor to support *custom marshaling* (also called [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal) marshaling). Standard marshaling is, in fact, an instance of custom marshaling; it is the default implementation used when an object does not require custom marshaling.

You can implement custom marshaling to allow an object to take different actions when used from across a network than it takes under local access and it is completely transparent to the client. This architecture makes it possible to design client/object interfaces without regard to network performance issues and then later to address network performance issues without disrupting the established design.

COM does not specify how components are structured; it specifies how they interact. COM leaves the concern about the internal structure of a component to programming languages and development environments. Conversely, programming environments have no set standards for working with objects outside of the immediate application. Microsoft Visual C++, for example, works extremely well for manipulating objects inside an application but has no support for working with objects outside the application. Generally, all other programming languages are the same in this regard. Therefore, to provide networkwide interoperability, COM, through language-independent interfaces, picks up where programming languages leave off.

The double indirection of the vtbl structure means that the pointers in the table of function pointers do not need to point directly to the real implementation in the real object. This is the heart of process transparency.

For in-process servers, where the object is loaded directly into the client process, the function pointers in the table point directly to the actual implementation. In this case, a function call from the client to an interface method directly transfers execution control to the method. However, this cannot work for local, let alone remote, objects because pointers to memory cannot be shared between processes. Nevertheless, the client must be able to call interface methods as if it were calling the actual implementation. Thus, the client uniformly transfers control to a method in some object by making the call.

A client always calls interface methods in some in-process object. If the actual object is local or remote, the call is made to a proxy object, which then makes a remote procedure call to the actual object.

So what method is actually executed? The answer is that whenever there is a call to an out-of-process interface, each interface method is implemented by a proxy object. The proxy object is always an in-process object that acts on behalf of the object being called. This proxy object knows that the actual object is running in a local or remote server.

The proxy object packages up the function parameters in some data packets and generates an RPC call to the local or remote object. That packet is picked up by a stub object in the server's process on the local or a remote computer, which unpacks the parameters and makes the call to the real implementation of the method. When that function returns, the stub packages up any out-parameters and the return value and sends it back to the proxy, which unpacks them and returns them to the original client.

Thus, client and server always talk to each other as if everything was in-process. All calls from the client and all calls to the server are, at some point, in-process. But because the vtbl structure allows some agent, like COM, to intercept all function calls and all returns from functions, that agent can redirect those calls to an RPC call as necessary. Although in-process calls are faster than out-of-process calls, the process differences are completely transparent to the client and server.

For more information, see the following topics:

-   [Marshaling Details](marshaling-details.md)
-   [Proxy](proxy.md)
-   [Stub](stub.md)
-   [Channel](channel.md)
-   [Microsoft RPC](microsoft-rpc.md)

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> <dt>

[Interface Marshaling](interface-marshaling.md)
</dt> </dl>

 

 
