---
title: N (RPC)
description: Words starting with N in Remote Procedure Call (RPC) glossary.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: b004002f-ae52-4ae8-a570-19241bfcee51
ms.topic: article
ms.date: 05/31/2018
---

# N (RPC)

[A](a-glos.md) [B](b-glos.md) [C](c-glos.md) [D](d-glos.md) [E](e-glos.md) [F](f-glos.md) G H [I](i-glos.md) J K [L](l-glos.md) [M](m-glos.md) N [O](o-glos.md) [P](p-glos.md) [Q](q.md) [R](r-glos.md) [S](s-glos.md) [T](t-glos.md) [U](u-glos.md) [V](v-glos.md) [W](w-glos.md) X Y Z

<dl> <dt>

<span id="_rpc_name_service_glos"></span><span id="_RPC_NAME_SERVICE_GLOS"></span>**name service**
</dt> <dd>

Service that maps names to objects and stores the name/object pairs in a database. For example, the RPC name service maps a logical name to a [*binding handle*](b-glos.md) so client applications can refer to that logical name, rather than a protocol sequence and network address. See also name service–interface daemon ([nsid)](/windows), Client Directory Service ([*CDS)*](c-glos.md), [*Locator*](l-glos.md).

</dd> <dt>

<span id="_rpc_nca_glos"></span><span id="_RPC_NCA_GLOS"></span>**Network Computing Architecture (NCA)**
</dt> <dd>

Collection of guidelines for distributed computing. The RPC communication protocols follow these guidelines.

</dd> <dt>

<span id="_rpc_nsi_glos"></span><span id="_RPC_NSI_GLOS"></span>**Name Service Independent (NSI)**
</dt> <dd>

Standard for API functions that allows a distributed application to access RPC name-service database elements through various name-service providers, such as OSF-DCE Cell Directory Service or Microsoft Locator. See also [–interface daemon](/windows) (nsid).

</dd> <dt>

<span id="_rpc_nsid_glos"></span><span id="_RPC_NSID_GLOS"></span>**name service–interface daemon (nsid)**
</dt> <dd>

Service that provides an interface between Microsoft [*Locator*](l-glos.md) and the OSF-DCE Cell Directory Service name service databases for RPC name-service functions.

</dd> <dt>

<span id="_rpc_named_pipe_glos"></span><span id="_RPC_NAMED_PIPE_GLOS"></span>**named pipe**
</dt> <dd>

Connection-oriented protocol, based on Server Message Blocks (SMBs) and [NetBIOS](/windows), used for communication between a server process and one or more client processes.

</dd> <dt>

<span id="_rpc_netbeui_glos"></span><span id="_RPC_NETBEUI_GLOS"></span>**NetBIOS Extended User Interface (NetBEUI)**
</dt> <dd>

LAN Manager native transport protocol and network device driver. See also [NetBIOS](/windows).

</dd> <dt>

<span id="_rpc_netbios_glos"></span><span id="_RPC_NETBIOS_GLOS"></span>**Network Basic Input/Output System (NetBIOS)**
</dt> <dd>

Software interface between the Microsoft MS-DOS operating system, the I/O bus, and a local area network.

</dd> <dt>

<span id="_rpc_ndr_glos"></span><span id="_RPC_NDR_GLOS"></span>**Network Data Representation (NDR)**
</dt> <dd>

Standard format used during network transmission that is independent of the data-type format on any particular computer architecture. Transmitted data includes information that specifies its NDR format.

</dd> <dt>

<span id="_rpc_network_address_glos"></span><span id="_RPC_NETWORK_ADDRESS_GLOS"></span>**network address**
</dt> <dd>

Address that identifies a server on a network.

</dd> <dt>

<span id="_rpc_nonencapsulated_union_glos"></span><span id="_RPC_NONENCAPSULATED_UNION_GLOS"></span>**nonencapsulated union**
</dt> <dd>

[*Discriminated union*](d-glos.md) that is less restrictive than an encapsulated union in that the discriminant and the union are not tightly bound. If the union is a parameter, the discriminant is another parameter; if the union is a structure field, the discriminant is another structure field. The IDL keywords \[[**switch\_is**](/windows/desktop/Midl/switch-is)\] and \[[**switch\_type**](/windows/desktop/Midl/switch-type)\] identify the discriminant and its type. See also [*encapsulated union*](e-glos.md).

</dd> <dt>

<span id="_rpc_nonidempotent_glos"></span><span id="_RPC_NONIDEMPOTENT_GLOS"></span>**nonidempotent**
</dt> <dd>

Indicator that a remote procedure call cannot be executed more than once because it will return a different value or change a state.

</dd> </dl>

 

 
