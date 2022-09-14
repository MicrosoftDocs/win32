---
title: NTLMSSP
description: NTLMSSP
ms.assetid: ae434165-4429-4ef0-b083-60abdfc50de0
ms.topic: article
ms.date: 05/31/2018
---

# NTLMSSP

NTLMSSP, whose authentication service identifier is RPC\_C\_AUTHN\_WINNT, is a security support provider that is available on all versions of DCOM. It uses the NTLM protocol for authentication. NTLM never actually transmits the user's password to the server during authentication. Therefore, the server cannot use the password during impersonation to access network resources that the user would have access to. Only local resources can be accessed.

NTLM works both locally and across computers. That is, if the client and server are on different computers, NTLM can still make sure the client is who it claims to be.

With NTLM, the client's identity is represented by a domain name, user name, and a password or token. When a server calls [**CoQueryClientBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryclientblanket), the client's domain name and user name are returned. However, when a server calls [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient), the client's token is returned. If there is no trust relationship between client and server and if the server has a local account with the same name and password as the client, that account will be used to represent the client.

NTLM supports mutual authentication cross-thread and cross-process (locally only). If the client specifies the principal name of the server in the form domain\\user in a call to [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket), the server's identity must match that principal name or the call will fail. If the client specifies **NULL**, the server's identity will not be checked.

NTLM additionally supports the delegate impersonation level cross-thread and cross-process (locally only).

## Related topics

<dl> <dt>

[COM and Security Packages](com-and-security-packages.md)
</dt> </dl>

 

 