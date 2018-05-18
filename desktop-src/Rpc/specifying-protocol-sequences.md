---
title: Specifying Protocol Sequences
description: Server applications must select one or more protocol sequences to use when communicating with the client over the network. The choice of protocol sequences is network-dependent. See Interpreting Binding Information and Selecting a Protocol Sequence.
ms.assetid: 'bde26a86-dc4f-4d18-ba51-c6536c62bb75'
---

# Specifying Protocol Sequences

Server applications must select one or more protocol sequences to use when communicating with the client over the network. The choice of protocol sequences is network-dependent. See [Interpreting Binding Information](interpreting-binding-information.md) and [Selecting a Protocol Sequence](selecting-a-protocol-sequence.md).

Your server program may allow clients to connect using any protocol sequence that the network supports. To do this, invoke [**RpcServerUseAllProtseqs**](rpcserveruseallprotseqs.md) and pass RPC\_C\_PROTSEQ\_MAX\_REQS\_DEFAULT as the first parameter. However, that is not the recommended approach. Rather, using **ncalrpc** for local calls and **ncacn\_ip\_tcp** or **ncacn\_http** for remote calls is usually sufficient. Heterogenous networks are uncommon, and virtually all networks support TCP/IP.

If you want your client to restrict port allocation for dynamic endpoints to a specific port range, call [**RpcServerUseAllProtseqsEx**](rpcserveruseallprotseqsex.md) instead. This function is specific to Microsoft RPC, and is extremely useful for remote procedure calls that pass through a firewall. It uses an extra parameter to pass port allocation control flags to the function. See [Configuring the Registry for Port Allocations and Selective Binding](configuring-the-windows-xp-2000-nt-registry-for-port-allocations-and-selective-binding.md).

You can specify protocol sequences and endpoint information in your MIDL file when you develop the server's interfaces. If you do, your server should use [**RpcServerUseAllProtseqsIf**](rpcserveruseallprotseqsif.md) to register all the protocol sequences and associated endpoint information provided in the IDL file. In addition, there is a corresponding [**RpcServerUseAllProtseqsIfEx**](rpcserveruseallprotseqsifex.md) function that also allows the server to pass port allocation–control flags.

If you want to configure your client and server programs to communicate with a specified protocol sequence, the server application should call [**RpcServerUseProtseq**](rpcserveruseprotseq.md). For a complete list of Microsoft RPC protocol sequences, see [Protocol Sequence Constants](protocol-sequence-constants.md).

Microsoft RPC also provides [**RpcServerUseProtseqEx**](rpcserveruseprotseqex.md) to enable applications to select specific protocol sequences and control dynamic port allocation.

In addition to connection-oriented protocols, Microsoft RPC supports datagram (connectionless) protocols as well. Connection-oriented protocols are recommended; datagram protocols have different feature sets than connection-oriented protocols, and should only be used if a distributed system developer requires a feature available only in datagram protocols. Some of the features available when using datagram protocols are:

-   Datagrams support the UDP and IPX connectionless transport protocols.
-   Because it is not necessary to establish and maintain a connection, the datagram RPC protocol requires less resource overhead.
-   Datagrams enable faster binding.
-   As with connection-oriented RPC, datagram RPC calls are by default *nonidempotent*. This means the call is guaranteed not to be executed more than once. However, a function can be marked as idempotent in the IDL file telling RPC that it is harmless to execute the function more than once in response to a single, client request. This allows the run time to maintain less state on the server. Note that an idempotent call would be re-executed only in rare circumstances on an unstable network.
-   Datagram RPC supports the [broadcast](https://msdn.microsoft.com/library/windows/desktop/aa366741) IDL attribute. Broadcast enables a client to issue messages to multiple servers at the same time. This lets the client locate one of several available servers on the network, or control multiple servers simultaneously. Note that the datagram broadcast is valid only within the local link, and usually does not cross routers. Broadcast calls are implicitly idempotent. If the call contains \[**out**\] parameters, only the first server response is returned. Once a server responds, all future RPCs over that binding handle will be sent to that server only, including calls with the broadcast attribute. To send another broadcast, create a new binding handle or call [**RpcBindingReset**](rpcbindingreset.md) on the existing handle.
-   Datagram RPC supports the [maybe](https://msdn.microsoft.com/library/windows/desktop/aa367075) IDL attribute. This lets the client send a call to the server without waiting for a response or confirmation. The call cannot contain \[**out**\] parameters. Calls using the **\[maybe\]** calls are implicitly idempotent.

 

 




