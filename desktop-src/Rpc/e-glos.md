---
title: E
description: Words starting with E in Remote Procedure Call (RPC) glossary.
Robots: noindex, nofollow
ms.assetid: 76e35c3c-91dd-42e3-9699-6767e37b2699
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# E

[A](a-glos.md) [B](b-glos.md) [C](c-glos.md) [D](d-glos.md) E [F](f-glos.md) G H [I](i-glos.md) J K [L](l-glos.md) [M](m-glos.md) [N](n-glos.md) [O](o-glos.md) [P](p-glos.md) [Q](q.md) [R](r-glos.md) [S](s-glos.md) [T](t-glos.md) [U](u-glos.md) [V](v-glos.md) [W](w-glos.md) X Y Z

<dl> <dt>

<span id="_rpc_embedded_pointer_glos"></span><span id="_RPC_EMBEDDED_POINTER_GLOS"></span>**embedded pointer**
</dt> <dd>

Pointer embedded in a parameter that is a data structure such as an array, structure, or union. See also [*top-level pointer*](t-glos.md#-rpc-top-level-pointer-glos).

</dd> <dt>

<span id="_rpc_encoding_services_glos"></span><span id="_RPC_ENCODING_SERVICES_GLOS"></span>**encoding services**
</dt> <dd>

MIDL-generated stub routines that provide support for data encoding and decoding (also known as *pickling* or *serialization*). Allow programmers to control buffers containing data to be marshaled and unmarshaled. See also [*type serialization*](t-glos.md#-rpc-type-serialization-glos), [*procedure serialization*](p-glos.md#-rpc-procedure-serialization-glos).

</dd> <dt>

<span id="_rpc_endpoint_glos"></span><span id="_RPC_ENDPOINT_GLOS"></span>**endpoint**
</dt> <dd>

Network-specific address of a server process for remote procedure calls. The actual name of the endpoint depends on the protocol sequence being used. See also [*dynamic endpoint*](d-glos.md#-rpc-dynamic-endpoint-glos) and [*well-known endpoint*](w-glos.md#-rpc-well-known-endpoint-glos).

</dd> <dt>

<span id="_rpc_endpoint_mapper_glos"></span><span id="_RPC_ENDPOINT_MAPPER_GLOS"></span>**endpoint mapper**
</dt> <dd>

Part of the RPC subsystem (RPCSS) that allows the run-time library to dynamically assign and resolve endpoints. See also [endpoint](#-rpc-endpoint-glos).

</dd> <dt>

<span id="_rpc_encapsulated_union_glos"></span><span id="_RPC_ENCAPSULATED_UNION_GLOS"></span>**encapsulated union**
</dt> <dd>

MIDL construct that allows unions to be passed as part of a remote procedure call by embedding the union in a structure in which the discriminant is the first field of the structure, and the union is the second (and final) field of the structure. The [*IDL*](i-glos.md#-rpc-idl-glos) keyword **switch** specifies that a union is encapsulated. See also [*nonencapsulated union*](n-glos.md#-rpc-nonencapsulated-union-glos).

</dd> <dt>

<span id="_rpc_epv_glos"></span><span id="_RPC_EPV_GLOS"></span>**entry point vector (EPV)**
</dt> <dd>

Array of pointers to functions that implement the operations specified in the interface. Each element in the array corresponds to a function defined in the IDL file. Entry-point vectors allow distributed applications to support more than one implementation of the functions defined in the IDL file.

</dd> </dl>

 

 




