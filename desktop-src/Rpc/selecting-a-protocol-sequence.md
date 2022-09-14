---
title: Selecting a Protocol Sequence
description: A protocol sequence is the language that a network operating system uses to talk over the network to other computers.
ms.assetid: 9c788b9b-82c5-4a4b-86c6-e9a9df699da3
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a Protocol Sequence

A protocol sequence is the language that a network operating system uses to talk over the network to other computers. In more specific terms, RPC applications must specify a string that represents a combination of an RPC protocol, a transport protocol, and a network protocol.

Microsoft RPC supports three RPC protocols:

-   Network Computing Architecture connection-oriented protocol (NCACN)
-   Network Computing Architecture datagram protocol (NCADG)
-   Network Computing Architecture local remote procedure call (NCALRPC)

RPC applications can use the NCALRPC protocol to invoke procedures offered by server programs running on the same computer that the client program runs on. This is, by far, the most efficient method for calling functionality in a different process on the same computer.

The transport and network protocols that your application uses depend on which protocols the network supports. Many networks today, including the Internet, support TCP/IP. Other common transport and network protocols are IPX/SPX, NetBIOS, and AppleTalk DSP. Microsoft RPC supports these and other transport and network protocols. For a complete list, see [Protocol Sequence Constants](protocol-sequence-constants.md).

When your application uses automatic binding handles, it does not need to specify the protocol sequence. If it uses implicit or explicit handles, it must obtain or specify the protocol sequence. Each distributed system must examine the environment in which it will be deployed to determine which protocol sequence is best suited for that environment.

Not all protocol sequences have equivalent functionality. Developers should verify that the chosen protocol sequence supports the required features. In general, **ncalrpc** for local communications and **ncacn\_ip\_tcp** or **ncacn\_http** for remote communications are recommended; they work in all environments, they have optimal performance, and they support all necessary, best-practice features.

Clients can also specify protocol sequence information that they obtain from Active Directory, the registry, environment variables created and initialized by the setup program, application-specific configuration files, or from literal strings in the program source code.

After your client program has a valid protocol sequence string, it can pass that information to the [**RpcStringBindingCompose**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingcompose) and [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) functions to create the binding handle.

 

 




