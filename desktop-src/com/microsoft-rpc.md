---
title: Microsoft RPC
description: Microsoft RPC
ms.assetid: a9ca629a-2766-43d5-89da-73d0628b3c5e
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft RPC

Microsoft RPC is a model for programming in a distributed computing environment. The goal of RPC is to provide transparent communication so that the client appears to be directly communicating with the server. Microsoft's implementation of RPC is compatible with the Open Software Foundation (OSF) Distributed Computing Environment (DCE) RPC.

You can configure RPC to use one or more transports, one or more name services, and one or more security servers. The interfaces to those providers are handled by RPC. Because Microsoft RPC is designed to work with multiple providers, you can choose the providers that work best for your network. The transport is responsible for transmitting the data across the network. The name service takes an object name, such as a moniker, and finds its location on the network. The security server offers applications the option of denying access to specific users and/or groups. See [Interface Design Rules](interface-design-rules.md) for more detailed information about application security.

In addition to the RPC run-time libraries, Microsoft RPC includes the Interface Definition Language (IDL) and its compiler. Although the IDL file is a standard part of RPC, Microsoft has enhanced it to extend its functionality to support custom COM interfaces. The Microsoft Interface Definition Language (MIDL) compiler uses the IDL file that describes your custom interface to generate several files discussed in [Building and Registering a Proxy DLL](building-and-registering-a-proxy-dll.md).

## Related topics

<dl> <dt>

[Channel](channel.md)
</dt> <dt>

[Inter-Object Communication](inter-object-communication.md)
</dt> <dt>

[Marshaling Details](marshaling-details.md)
</dt> <dt>

[Proxy](proxy.md)
</dt> <dt>

[Stub](stub.md)
</dt> </dl>

 

 




