---
title: Writing an Authenticated SSPI Client
description: Writing an authenticated SSPI client and Remote Procedure Call (RPC).
ms.assetid: db39d3bf-84fa-466e-9ba1-ba17f64c8f8d
keywords:
- Remote Procedure Call RPC , tasks, writing an authenticated SSPI client
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Authenticated SSPI Client

All RPC client/server sessions require a binding between the client and the server. To add security to client/server applications, the programs must use an authenticated binding. This section describes the process of creating an authenticated binding between the client and the server.

-   [Creating Client-side Binding Handles](#creating-client-side-binding-handles)
-   [Providing Client Credentials to the Server](#providing-client-credentials-to-the-server)

For related information, see [Procedures Used with Most Security Packages and Protocols](/windows/desktop/SecAuthN/procedures-used-with-most-security-packages-and-protocols) in the Platform Software Development Kit (SDK).

## Creating Client-side Binding Handles

To create an authenticated session with a server program, client applications must provide authentication information with their binding handle. To set up an authenticated binding handle, clients invoke the [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) or [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) function. These two functions are nearly identical. The only difference between them is that the client can specify the quality of service with the **RpcBindingSetAuthInfoEx** function.

The following code fragment shows how a call to [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) might look.


```C++
// This code fragment assumes that rpcBinding is a valid binding 
// handle between the client and the server. It also assumes that
// pAuthCredentials is a valid pointer to a data structure which
// contains the user's authentication credentials.

dwStatus = DsMakeSpn(
    "ldap",
    "ServerName.domain.com",
    NULL,
    0,
    NULL,
    &pcSpnLength,
    pszSpn);

//...

rpcStatus = RpcBindingSetAuthInfo(
    rpcBinding,                       // Valid binding handle
    pszSpn,                           // Principal name 
    RPC_C_AUTHN_LEVEL_PKT_INTEGRITY,  // Authentication level
    RPC_C_AUTHN_GSS_NEGOTIATE,        // Use Negotiate SSP
    NULL,                             // Authentication credentials <entity type="ndash"/> use current thread credentials
    RPC_C_AUTHZ_NAME);                // Authorization service
```



After the client successfully calls the [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) or [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) functions, the RPC run-time library automatically authenticates all RPC calls on the binding. The level of security and authentication that the client selects applies only to that binding handle. Context handles derived from the binding handle will use the same security information, but subsequent modifications to the binding handle will not be reflected in the context handles. For more information, see [Context Handles](context-handles.md).

The authentication level stays in effect until the client chooses another level, or until the process terminates. Most applications will not require a change in the security level. The client can query any binding handle to obtain its authorization information by invoking [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) and passing it the binding handle.

## Providing Client Credentials to the Server

Servers use the client's binding information to enforce security. Clients always pass a binding handle as the first parameter of a remote procedure call. However, servers cannot use the handle unless it is declared as the first parameter to remote procedures in either the IDL file or in the server's application configuration file (ACF). You can choose to list the binding handle in the IDL file, but this forces all clients to declare and manipulate the binding handle rather than using automatic or implicit binding. For further information, see [The IDL and ACF Files](the-idl-and-acf-files.md).

Another method is to leave the binding handles out of the IDL file and to place the **explicit\_handle** attribute into the server's ACF. In this way, the client can use the type of binding best suited to the application, while the server uses the binding handle as though it were declared explicitly.

The process of extracting the client credentials from the binding handle occurs as follows:

-   RPC clients call [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo) and include their authentication information as part of the binding information passed to the server.
-   Usually, the server calls [**RpcImpersonateClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcimpersonateclient) in order to behave as though it were the client. If the binding handle is not authenticated, the call fails with RPC\_S\_NO\_CONTEXT\_AVAILABLE. To obtain the client's user name, call [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) while impersonating, or on Windows XP or later versions of Windows, call [**RpcGetAuthorizationContextForClient**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcgetauthorizationcontextforclient) to get the authorization context, then use Authz functions to retrieve the name.
-   The server will normally call [**CreatePrivateObjectSecurity**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-createprivateobjectsecurity) to create objects with ACLs. After this is accomplished, later security checks become automatic.

 

 