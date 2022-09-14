---
title: Mutual Authentication in RPC Applications
description: RPC services can use service connection points to publish themselves, or they can use the RPC name service (RpcNs) APIs.
ms.assetid: 9f575aef-0a4b-4e1b-8ea9-5f40e6c3d9c7
ms.tgt_platform: multiple
keywords:
- Mutual Authentication in RPC Applications AD
- Active Directory, Using, Mutual Authentication, RPC
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Authentication in RPC Applications

RPC services can use service connection points to publish themselves, or they can use the RPC name service (RpcNs) APIs. This topic discusses how to perform mutual authentication with an RPC service that publishes itself using the RPC name service (RpcNs) APIs.

**To register an SPN in the directory**

1.  Call the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) function to compose a service principal name (SPN) for the service.
2.  Call the [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) function to register the SPN on the service account or computer account in whose context the service will run.

**To register a service with the RPC naming service**

1.  Verify that the appropriate SPNs are registered on the account under which the service is running. For more information, see [Logon Account Maintenance Tasks](logon-account-maintenance-tasks.md).
2.  Call the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function to register the service SPN with the RPC authentication service, and specify **RPC\_C\_AUTHN\_GSS\_NEGOTIATE** as the authentication service to use.

For more information about performing mutual authentication in an RPC service, see [Writing an Authenticated SSPI Server](/windows/desktop/Rpc/writing-an-authenticated-sspi-server).

**To authenticate the service from the client**

1.  Extract the host name from the RPC Binding.
2.  Compose the SPN for the service by calling the [**DsMakeSpn**](/windows/desktop/api/Dsparse/nf-dsparse-dsmakespna) function with the service class, the DNS host name, and the service name; that is the distinguished name of the connection point in the case of RpcNs.

    For more information about composing an SPN for an RpcNs service, see [Composing SPNs for an RpcNs Service](composing-spns-for-an-rpcns-service.md).

3.  Set up an [**RPC\_SECURITY\_QOS**](/windows/desktop/api/rpcdce/ns-rpcdce-rpc_security_qos) structure to request mutual authentication.
4.  Call the [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) function to set the authentication data for the RPC binding. The client must request at least **RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY** to ensure that communications have not been tampered. For increased security, the client should specify **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** to request encryption.
5.  Perform the RPC call.

For more information about performing mutual authentication in an RPC client, see [Writing an Authenticated SSPI Client](/windows/desktop/Rpc/writing-an-authenticated-sspi-client).

**To authenticate the client from the service**

1.  Call the [**RpcBindingInqAuthClient**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindinginqauthclient) function to verify the authentication parameters specified by the client. If the client has not requested the desired level of authentication, reject the call. Be aware that an RPC service must verify the authentication level, authentication service, and client identity on every call to ensure that the client has been properly authenticated.
2.  Call the [**RpcImpersonateClient**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcimpersonateclient) function to impersonate the client.
3.  Perform the requested operation.
4.  Call the [**RpcRevertToSelf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcreverttoself) function to revert to the service security context.

For more information about RPC client impersonation, see [Client Impersonation](/windows/desktop/Rpc/client-impersonation).

For more information, see:

-   [Publishing with the RPC Name Service (RpcNs)](publishing-with-the-rpc-name-service-rpcns.md)
-   [RPC Security Essentials](/windows/desktop/Rpc/rpc-security-essentials)

 

 