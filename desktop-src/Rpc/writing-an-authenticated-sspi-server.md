---
title: Writing an Authenticated SSPI Server
description: Before authenticated communication can take place between the client and server programs, the server must register its authentication information.
ms.assetid: 723ae1ee-d729-4748-9ef1-062a0c6f60d0
keywords:
- Remote Procedure Call RPC , tasks, writing an authenticated SSPI server
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Authenticated SSPI Server

Before authenticated communication can take place between the client and server programs, the server must register its authentication information. In particular, the server must register its principal name and specify the authentication service it uses. For more information on principal names, see [Principal Names](principal-names.md). For details about authentication services, see [Authentication Services](authentication-services.md).

To register its authentication information, servers call the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function. Pass a pointer to the principal name as the value of the first parameter. Set the second parameter to a constant indicating the authentication service that the application will use. For a description of authentication services, see [Authentication-Service Constants](authentication-service-constants.md).

The server may also pass the address of a key acquisition function as the value of the third parameter. See [Key Acquisition Functions](key-acquisition-functions.md). To use the default key acquisition function for the selected authentication service, set the third parameter to **NULL**. The last parameter to the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function is a pointer data to pass to the key acquisition function, if you provide a key acquisition function. A call to **RpcServerRegisterAuthInfo** is shown in the following code fragment.


```C++
dwStatus = DsMakeSpn(
    "ldap",
    "ServerName.domain.com",
    NULL,
    0,
    NULL,
    &pcSpnLength,
    pszSpn);

rpcStatus = RpcServerRegisterAuthInfo (
    psz,                                   // Server principal name
    RPC_C_AUTHN_GSS_NEGOTIATE,             // Authentication service
    NULL,                                  // Use default key function
    NULL);                                 // No arg for key function
```



In addition, the server may provide the RPC run-time library with an authorization function. To set an authorization function, call the [**RpcMgmtSetAuthorizationFn**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtsetauthorizationfn) function.

The server portion of a distributed application can call the function [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) or [**RpcBindingInqAuthClientEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclientex) to query a binding handle for authentication information.

If your server registers with a security support provider, client calls with invalid credentials will not be dispatched. However, calls with no credentials will be dispatched. There are three ways to prevent this from happening:

-   Register the interface using [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), with a security callback function; this will cause the RPC run-time library to automatically reject unauthenticated calls to that interface. Registering a callback function is compatible with other methods of checking access credentials; the callback function can itself call the [**RpcImpersonateClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcimpersonateclient), [**RpcGetAuthorizationContextForClient**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcgetauthorizationcontextforclient), or [**RpcBindingInqAuthClientEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) functions, or others. However, these functions cannot use the arguments passed to the function, as they are not unmarshalled at that point.

> [!IMPORTANT]
> Registering the interface using [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) with a security callback function is the most heavily recommended method of checking client credentials.

 

-   Call [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) to determine the security level that the client is using. Your stub can then return an error if the client is unauthenticated.

 

 




