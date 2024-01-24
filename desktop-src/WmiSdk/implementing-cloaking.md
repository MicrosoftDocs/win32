---
description: Cloaking is an extension to impersonation that allows for better control over how COM impersonates a client over a proxy. Like many forms of WMI security, you set cloaking through the CoSetProxyBlanket and CoInitializeSecurity interfaces.
ms.assetid: e094aecc-e940-43aa-87c2-ea8cc86d1051
ms.tgt_platform: multiple
title: Implementing Cloaking
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Cloaking

Cloaking is an extension to impersonation that allows for better control over how COM impersonates a client over a proxy. Like many forms of WMI security, you set cloaking through the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) interfaces.

COM provides the following forms of cloaking:

-   Static

    COM establishes the token identity by the thread or process token on the first call to the proxy. If you use static cloaking with [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket), you set the identity of the proxy for the life of the proxy.

-   Dynamic

    COM reestablishes the token identity from the thread or process token on each call to the proxy. Because COM checks the identity on each call, dynamic cloaking allows for finer control over the client identity. However, dynamic cloaking is less efficient than static cloaking.

When you set cloaking in conjunction with the delegation level of impersonation, a server can propagate the identity of a client across servers, even if the servers are remote. If you do not enable cloaking, COM makes any call from a local server to a remote server under the context of the actual server process.

Cloaking lets WMI impersonate a client to access both local and remote network resources across multiple computer boundaries. WMI can pass the identity of the client to local and remote servers, such as other remote instances of WMI. Those remote servers can then perform operations under the initial client context.

The following procedure describes how to use cloaking and delegation together.

**To use cloaking and delegation together**

1.  Set the authentication service to Kerberos.

    Kerberos is the only authentication service that supports remote cloaking and delegation. This means that cloaking and delegation can only be used on remote servers.

2.  Mark the server login account as "Trusted for Delegation" in the Active Directory services.
3.  Mark the client login account as "Account is sensitive and cannot be delegated" in Active Directory services.

For example, a call to the View Provider, which may return objects from multiple instances of WMI on multiple computers, can benefit from delegation and cloaking.

 

 
