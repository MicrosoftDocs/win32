---
title: Essential RPC Binding Terminology
description: To better aid in a discussion of the client/server connection process, it is helpful to know the following terms.
ms.assetid: 05aca325-87ee-4581-9152-a8a2ff7fb490
keywords:
- Remote Procedure Call RPC , described, binding
ms.topic: article
ms.date: 05/31/2018
---

# Essential RPC Binding Terminology

To better aid in a discussion of the client/server connection process, it is helpful to know the following terms.

## Parameters

<dl> <dt>

<span id="Protocol_Sequence"></span><span id="protocol_sequence"></span><span id="PROTOCOL_SEQUENCE"></span>Protocol Sequence
</dt> <dd>

When network operating systems communicate with each other, they must listen and speak the same language. These languages are called *protocol sequences*. Client and server programs must use protocol sequences that the network connecting them supports. Microsoft RPC supports a variety of protocol sequences. For details, see [Selecting a Protocol Sequence](selecting-a-protocol-sequence.md), [Specifying Protocol Sequences](specifying-protocol-sequences.md), and [**endpoint**](/windows/desktop/Midl/endpoint).

</dd> <dt>

<span id="Server_Host_Computer_or_Server_Host_System"></span><span id="server_host_computer_or_server_host_system"></span><span id="SERVER_HOST_COMPUTER_OR_SERVER_HOST_SYSTEM"></span>Server Host Computer or Server Host System
</dt> <dd>

The server program runs on the server host computer. However, much literature on client/server computing refers to both the server program and the server host computer as the "server." The result is that it is not always clear which is being discussed.

</dd> <dt>

<span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint
</dt> <dd>

Server programs listen to a port or a group of ports on the server host computer for client requests. Server host systems maintain a database of these ports, which are called endpoints in RPC. The database is called the endpoint map.

</dd> <dt>

<span id="Binding"></span><span id="binding"></span><span id="BINDING"></span>Binding
</dt> <dd>

Client programs create a binding to the server to establish a communication session. A binding contains all of the information the client applications needs to create the session.

</dd> </dl>

 

 