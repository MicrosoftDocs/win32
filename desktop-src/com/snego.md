---
title: Snego
description: Snego, whose authentication service identifier is RPC\_C\_AUTHN\_GSS\_NEGOTIATE, does not actually provide authentication services itself.
ms.assetid: 2087a84c-d302-4511-9f02-2d20ee9e0d8e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Snego

Snego, whose authentication service identifier is RPC\_C\_AUTHN\_GSS\_NEGOTIATE, does not actually provide authentication services itself. Instead, it takes a list of authentication services and negotiates a service that will work between the client and server. The authentication parameters are not used by Snego but are passed to the chosen authentication service, which does the actual authentication. Snego was standardized by the Internet Engineering Task Force (IETF) in December 1998, in document [RFC 2478](http://go.microsoft.com/fwlink/p/?linkid=103724).

Snego is useful when you don't know what authentication services the remote computer can provide.

To use Snego, both the client and the server must specify Snego as the authentication service. The server specifies RPC\_C\_AUTHN\_GSS\_NEGOTIATE as the **dwAuthnSvc** member of one of the [**SOLE\_AUTHENTICATION\_SERVICE**](https://msdn.microsoft.com/en-us/library/ms686648(v=VS.85).aspx) structures in the *asAuthSvc* array parameter that is passed to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). The client can specify Snego by calling [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) and passing RPC\_C\_AUTHN\_GSS\_NEGOTIATE as the *dwAuthnSvc* parameter. The client should also provide a list of possible authentication services for Snego through the **PackageList** member of the [**SEC\_WINNT\_AUTH\_IDENTITY\_EX**](https://msdn.microsoft.com/library/windows/desktop/aa380132) structure that is passed to the *pAuthInfo* parameter in the call to **CoSetProxyBlanket**. If *pAuthInfo* is **NULL**, Snego composes a list of authentication services from the security packages installed on the computer. Then Snego sends the list of authentication services to the server, compares the list to the server's available authentication services, and picks an authentication service to use for the connection.

> [!Note]  
> Schannel cannot be on the list of authentication services that Snego uses.

 

Clients can also specify Snego when they call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). The *dwAuthnSvc* and *pAuthInfo* parameters of [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) become members of a [**SOLE\_AUTHENTICATION\_INFO**](https://msdn.microsoft.com/en-us/library/ms680049(v=VS.85).aspx) structure that is passed to **CoInitializeSecurity** through its *pAuthList* parameter. The details of the values of those members are the same as described in the preceding paragraph.

If Snego is used, calls to [**CoQueryProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryproxyblanket) or [**CoQueryClientBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryclientblanket) will return Snego as the authentication service, rather than the actual authentication service that Snego picked for establishing the connection.

## Related topics

<dl> <dt>

[COM and Security Packages](com-and-security-packages.md)
</dt> </dl>

 

 




