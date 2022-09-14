---
title: Impersonation Levels (COM)
description: If impersonation succeeds, it means that the client has agreed to let the server be the client to some degree.
ms.assetid: 7539bbee-063f-4788-aece-7b70684826c8
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation Levels

If impersonation succeeds, it means that the client has agreed to let the server be the client to some degree. The varying degrees of impersonation are called *impersonation levels*, and they indicate how much authority is given to the server when it is impersonating the client.

Currently, there are four impersonation levels: *anonymous*, *identify*, *impersonate*, and *delegate*. The following list briefly describes each impersonation level:

<dl> <dt>

<span id="anonymous__RPC_C_IMP_LEVEL_ANONYMOUS_"></span><span id="anonymous__rpc_c_imp_level_anonymous_"></span><span id="ANONYMOUS__RPC_C_IMP_LEVEL_ANONYMOUS_"></span>anonymous (RPC\_C\_IMP\_LEVEL\_ANONYMOUS)
</dt> <dd>

The client is anonymous to the server. The server process can impersonate the client, but the impersonation token does not contain any information about the client. This level is only supported over the local interprocess communication transport. All other transports silently promote this level to identify.

</dd> <dt>

<span id="identify__RPC_C_IMP_LEVEL_IDENTIFY_"></span><span id="identify__rpc_c_imp_level_identify_"></span><span id="IDENTIFY__RPC_C_IMP_LEVEL_IDENTIFY_"></span>identify (RPC\_C\_IMP\_LEVEL\_IDENTIFY)
</dt> <dd>

The system default level. The server can obtain the client's identity, and the server can impersonate the client to do ACL checks.

</dd> <dt>

<span id="impersonate__RPC_C_IMP_LEVEL_IMPERSONATE_"></span><span id="impersonate__rpc_c_imp_level_impersonate_"></span><span id="IMPERSONATE__RPC_C_IMP_LEVEL_IMPERSONATE_"></span>impersonate (RPC\_C\_IMP\_LEVEL\_IMPERSONATE)
</dt> <dd>

The server can impersonate the client's security context while acting on behalf of the client. The server can access local resources as the client. If the server is local, it can access network resources as the client. If the server is remote, it can access only resources that are on the same computer as the server.

</dd> <dt>

<span id="delegate__RPC_C_IMP_LEVEL_DELEGATE_"></span><span id="delegate__rpc_c_imp_level_delegate_"></span><span id="DELEGATE__RPC_C_IMP_LEVEL_DELEGATE_"></span>delegate (RPC\_C\_IMP\_LEVEL\_DELEGATE)
</dt> <dd>

The most powerful impersonation level. When this level is selected, the server (whether local or remote) can impersonate the client's security context while acting on behalf of the client. During impersonation, the client's credentials (both local and network) can be passed to any number of computers.

For impersonation to work at the delegate level, the following requirements must be met:

-   The client must set the impersonation level to RPC\_C\_IMP\_LEVEL\_DELEGATE.
-   The client account must not be marked "Account is sensitive and cannot be delegated" in the Active Directory Service.
-   The server account must be marked with the "Trusted for delegation" attribute in the Active Directory Service.
-   The computers hosting the client, the server, and any "downstream" servers must all be running in a domain.

</dd> </dl>

By choosing the impersonation level, the client tells the server how far it can go in impersonating the client. The client sets the impersonation level on the proxy it uses to communicate with the server.

## Setting the Impersonation Level

There are two ways to set the impersonation level:

-   The client can set it processwide, through a call to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).
-   A client can set proxy-level security on an interface of a remote object through a call to [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket) (or the helper function [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket)).

You set the impersonation level by passing an appropriate RPC\_C\_IMP\_LEVEL\_xxx value to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) through the *dwImpLevel* parameter.

Different authentication services support delegate-level impersonation to different extents. For instance, NTLMSSP supports cross-thread and cross-process delegate-level impersonation, but not cross-computer. On the other hand, the Kerberos protocol supports delegate-level impersonation across computer boundaries, while Schannel does not support any impersonation at the delegate level. If you have a proxy at impersonate level and you want to set the impersonation level to delegate, you should call [**SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket) using the default constants for every parameter except the impersonation level. COM will choose NTLM locally and the Kerberos protocol remotely (when the Kerberos protocol will work).

## Related topics

<dl> <dt>

[Delegation and Impersonation](delegation-and-impersonation.md)
</dt> </dl>

 

 