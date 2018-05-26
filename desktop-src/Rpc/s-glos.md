---
title: S
description: Words starting with S in Remote Procedure Call (RPC) glossary.
Robots: noindex, nofollow
ms.assetid: ba3c7959-2acd-4a38-b996-cfe7dac20241
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# S

[A](a-glos.md) [B](b-glos.md) [C](c-glos.md) [D](d-glos.md) [E](e-glos.md) [F](f-glos.md) G H [I](i-glos.md) J K [L](l-glos.md) [M](m-glos.md) [N](n-glos.md) [O](o-glos.md) [P](p-glos.md) [Q](q.md) [R](r-glos.md) S [T](t-glos.md) [U](u-glos.md) [V](v-glos.md) [W](w-glos.md) X Y Z

<dl> <dt>

<span id="rpc.s_glos_1_gly"></span><span id="RPC.S_GLOS_1_GLY"></span>**scalability**
</dt> <dd>

Ability to fully utilize the additional processing power on a multiprocessor system (2, 4, 8, 32, or more processors). Scalability is also the ability to service a large number of clients.

</dd> <dt>

<span id="_rpcl_spp_glos"></span><span id="_RPCL_SPP_GLOS"></span>**Sequenced Packet Protocol (SPP)**
</dt> <dd>

Banyan Vines [*connection-oriented*](c-glos.md#-rpc-connection-oriented-glos) communication protocol for routing information packets over local area networks.

</dd> <dt>

<span id="_rpc_spx_glos"></span><span id="_RPC_SPX_GLOS"></span>**Sequenced Packet Exchange (SPX)**
</dt> <dd>

Novell NetWare [*connection-oriented*](c-glos.md#-rpc-connection-oriented-glos) communication protocol for routing information packets over local area networks and wide area networks.

</dd> <dt>

<span id="_rpc_serialization_glos"></span><span id="_RPC_SERIALIZATION_GLOS"></span>**serialization**
</dt> <dd>

Process of marshaling data to (encoding) and unmarshaling data from (decoding) buffers that you control. This is in contrast to traditional RPC usage, where the stubs and the RPC runtime control the marshaling buffers. Also called pickling. See also [*procedure serialization*](p-glos.md#-rpc-procedure-serialization-glos), [*type serialization*](t-glos.md#-rpc-type-serialization-glos).

</dd> <dt>

<span id="_rpc_server_stub_glos"></span><span id="_RPC_SERVER_STUB_GLOS"></span>**server stub**
</dt> <dd>

MIDL-generated C-language source code that contains all the functions necessary for the server application to handle remote requests using local procedure calls. See also [*client stub*](c-glos.md#-rpc-client-stub-glos).

</dd> <dt>

<span id="_rpc_session_glos"></span><span id="_RPC_SESSION_GLOS"></span>**session**
</dt> <dd>

Established relationship between a client application and a server application. See also [*bind*](b-glos.md#-rpc-bind-glos), [*binding handle*](b-glos.md#-rpc-binding-handle-glos).

</dd> <dt>

<span id="_rpc_static_callback_function_glos"></span><span id="_RPC_STATIC_CALLBACK_FUNCTION_GLOS"></span>**static callback function**
</dt> <dd>

Remote procedure that is part of the client side of a distributed application, that a server can call to obtain information from the client. The \[ [callback](https://msdn.microsoft.com/library/windows/desktop/aa366746)\] attribute designates a static callback function.

</dd> <dt>

<span id="_rpc_static_identity_tracking_glos"></span><span id="_RPC_STATIC_IDENTITY_TRACKING_GLOS"></span>**static identity tracking**
</dt> <dd>

Static identity tracking specifies that the RPC run-time uses the security credentials in the client's binding handle for all RPC calls. See also [*dynamic identity tracking*](d-glos.md#-rpc-dynamic-identity-tracking-glos).

</dd> <dt>

<span id="_rpc_string_binding_glos"></span><span id="_RPC_STRING_BINDING_GLOS"></span>**string binding**
</dt> <dd>

Character string that consists of the object [*UUID*](u-glos.md#-rpc-uuid-glos), [*protocol sequence*](p-glos.md#-rpc-protocol-sequence-glos), [*network address*](n-glos.md#-rpc-network-address-glos), [*endpoint*](e-glos.md#-rpc-endpoint-glos), and endpoint options, all of which can be used to create a [*binding handle*](b-glos.md#-rpc-binding-handle-glos) to the specified server.

</dd> <dt>

<span id="_rpc_strong_typing_glos"></span><span id="_RPC_STRONG_TYPING_GLOS"></span>**strong typing**
</dt> <dd>

Compiler enforcement of strict control over data types. In MIDL and RPC, strong typing is used to ensure that data is interpreted consistently by different computers in a distributed environment.

</dd> </dl>

 

 




