---
title: Stub
description: The stub, like the proxy, is made up of one or more interface pieces and a manager.
ms.assetid: 45e2a4c3-6a78-4018-9f32-ce5523682c0f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stub

The stub, like the proxy, is made up of one or more interface pieces and a manager. Each interface stub provides code to unmarshal the parameters and code that calls one of the object's supported interfaces. Each stub also provides an interface for internal communication. The stub manager keeps track of the available interface stubs.

There are, however, the following differences between the stub and the proxy:

-   The most important difference is that the stub represents the client in the object's address space.
-   The stub is not implemented as an aggregate object because there is no requirement that the client be viewed as a single unit; each piece in the stub is a separate component.
-   The interface stubs are private rather than public.
-   The interface stubs implement [**IRpcStubBuffer**](https://msdn.microsoft.com/en-us/library/ms678504(v=VS.85).aspx), not [**IRpcProxyBuffer**](https://msdn.microsoft.com/en-us/library/ms693743(v=VS.85).aspx).
-   Instead of packaging parameters to be marshaled, the stub unpackages them after they have been marshaled and then packages the reply.

## Structure of the Stub

The following diagram shows the structure of the stub. Each interface stub is connected to an interface on the object. The channel dispatches incoming messages to the appropriate interface stub. All the components talk to the channel through [**IRpcChannelBuffer**](https://msdn.microsoft.com/en-us/library/ms679738(v=VS.85).aspx), the interface that provides access to the RPC run-time library.

![](images/98714a22-733e-432f-bb90-408bbeecc23f.png)

## Related topics

<dl> <dt>

[Channel](channel.md)
</dt> <dt>

[Inter-Object Communication](inter-object-communication.md)
</dt> <dt>

[Marshaling Details](marshaling-details.md)
</dt> <dt>

[Microsoft RPC](microsoft-rpc.md)
</dt> <dt>

[Proxy](proxy.md)
</dt> </dl>

 

 




