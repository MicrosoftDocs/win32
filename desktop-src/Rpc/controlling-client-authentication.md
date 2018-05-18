---
title: Controlling Client Authentication
description: The best method for authenticating a client is installing a security callback function using the RpcServerRegisterIf2 or RpcServerRegisterIfEx function; either accepts a security callback function as an argument.
ms.assetid: '3e858a71-9190-44a3-bc63-08cfbd02d443'
---

# Controlling Client Authentication

The best method for authenticating a client is installing a security callback function using the [**RpcServerRegisterIf2**](rpcserverregisterif2.md) or [**RpcServerRegisterIfEx**](rpcserverregisterifex.md) function; either accepts a security callback function as an argument. When the security callback function is called, make the necessary checks. The attributes on the connection, identity of the caller, or both, can be checked. To check the attributes of a connection, call the [**RpcServerInqCallAttributes**](rpcserverinqcallattributes.md) or [**RpcBindingInqAuthClient**](rpcbindinginqauthclient.md) function. This enables the filtering of clients that are not authenticated, clients that use a specific security provider, or clients that do not use strong enough protection (like privacy).

To allow access to a subset of the authenticated users, use [**RpcGetAuthorizationContextForClient**](rpcgetauthorizationcontextforclient.md). This function returns an Authz client context that can be used to make very sophisticated access checks. For example, this method could be used to allow access only to the vice presidents in an organization during normal business hours, and to the CEO during any hour using Active Directory services to map a user name to their title. The user can be impersonated, and their name obtained. Once their identity is known, any desired checks can be made.

 

 




