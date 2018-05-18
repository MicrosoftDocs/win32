---
title: MSMQ Security Services
description: Synchronous RPC messages can use any of the security features available from the RPC run time. See Security for more details.
ms.assetid: '0f4d45c4-7457-4449-8736-e141a95f6930'
---

# MSMQ Security Services

Synchronous RPC messages can use any of the security features available from the RPC run time. See [Security](security.md) for more details.

Asynchronous \[ [message](https://msdn.microsoft.com/library/windows/desktop/aa367077)\] calls cannot use RPC security because there is no handshake between client and server. In fact, the server may not even be running at the time of the call. To access the security services provided by Message Queuing Services (MSMQ), the client application should call [**RpcBindingSetAuthInfo**](rpcbindingsetauthinfo.md) to control the level of authentication and privacy for its calls to the server.

The server application can call [**RpcBindingInqAuthClient**](rpcbindinginqauthclient.md) from within a remote procedure call to determine the security level for that call. The mapping between RPC security constants and MSMQ security is shown in the following table.



| RPC security level                | Description                                                                                |
|-----------------------------------|--------------------------------------------------------------------------------------------|
| RPC\_AUTHN\_LEVEL\_NONE           | The call is not authenticated or encrypted.                                                |
| RPC\_AUTHN\_LEVEL\_PKT\_INTEGRITY | The call is authenticated using MSMQ security.                                             |
| RPC\_AUTHN\_LEVEL\_PKT\_PRIVACY   | The call is authenticated and encrypted as it travels between the client and server queue. |



 

The server can also force call authentication and encryption by calling [**RpcServerUseProtseqEpEx**](rpcserveruseprotseqepex.md) and setting the RPC\_C\_MQ\_AUTHN\_LEVEL\_NONE, RPC\_C\_MQ\_AUTHN\_LEVEL\_PKT\_INTEGRITY and RPC\_C\_MQ\_AUTHN\_LEVEL\_PKT\_PRIVACY flags in the [**RPC\_POLICY**](rpc-policy.md) structure.

 

 




