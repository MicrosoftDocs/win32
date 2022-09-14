---
title: Quality of Service (RPC)
description: Client programs can use the RpcBindingSetAuthInfoEx function rather than the RpcBindingSetAuthInfo function to create an authenticated binding.
ms.assetid: bc3d47ba-3c1b-4aba-8fe3-b4501a621931
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Service (RPC)

Client programs can use the [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) function rather than the [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) function to create an authenticated binding. If they do, they pass a pointer to an [**RPC\_SECURITY\_QOS**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_security_qos) structure as the final parameter of **RpcBindingSetAuthInfoEx**. This structure contains information about the quality of service. Client programs can also specify the identity tracking and select the impersonation type.

Use the **Capabilities** member of the [**RPC\_SECURITY\_QOS**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_security_qos) structure to set which portions of the client/server application are authenticated. If RPC\_C\_QOS\_CAPABILITIES\_DEFAULT is selected, the RPC run-time library authenticates the client or server according to the default for the SSP. By default, the Kerberos protocol SSP authenticates both the client and the server. The default for all other SSPs that Microsoft provides is to authenticate the client to the server, but not to authenticate the server to the client.

If the client and the server should always authenticate to each other, set the **Capabilities** member of the [**RPC\_SECURITY\_QOS**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_security_qos) structure to RPC\_C\_QOS\_CAPABILITIES\_MUTUAL\_AUTH. Some security providers may not support mutual authentication. If RPC\_C\_QOS\_CAPABILITIES\_MUTUAL\_AUTH is specified for such security providers, an error is returned when a remote procedure call is made. When using the SCHANNEL SSP, it is possible to also set the **Capabilities** member to RPC\_C\_QOS\_CAPABILITIES\_ANY\_AUTHORITY. This constant specifies that the SSP shall validate the remote procedure call even if the certificate authority that issued the client's authentication certificate is not in the SSP's root certificate store. The default is to reject the certificate if the SSP does not recognize the certificate authority. The certificate authority is an independent company or organization, such as VeriSign, that issues authentication certificates.

Applications can also set the identity tracking that the RPC run-time library uses. Programs generally use [*static identity tracking*](s-glos.md). With static tracking, the client's credentials are set when it calls the [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) function. The RPC run-time library then uses those credentials for all RPC calls on the binding, regardless of changes in the identity of the calling thread or the calling process. Applications can also select [*dynamic identity tracking*](d-glos.md). Dynamic identity tracking instructs the RPC run-time library to use the credentials of the calling thread at the time of each call, rather than the binding handle. The default identity tracking is static.

If the identity of the client is not going to change, static identity tracking can have better performance characteristics, and can save the RPC run time from checking each time whether the identity on the calling thread is the same as the identity given to the security system. If the identity of the calling thread may change between calls, and the server needs to recognize those changes, it is best to specify dynamic identity tracking—the RPC run time quietly and efficiently tracks the identity for you, and if the identity changes, manages that change on your behalf.

> [!Note]  
> For **ncalrpc** calls, static and dynamic identity tracking have different performance characteristics, and depending on the circumstances, either may be faster.

 

As part of the QOS specification, the client program can also set the type of impersonation that a server program can perform on its behalf. For more information, see [Client Impersonation](client-impersonation.md).

The version number field of the [**RPC\_SECURITY\_QOS**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_security_qos) structure should always be set to RPC\_C\_SECURITY\_QOS\_VERSION.

 

 




