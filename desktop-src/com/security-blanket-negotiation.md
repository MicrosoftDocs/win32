---
title: Security Blanket Negotiation
description: Security Blanket Negotiation
ms.assetid: 5a01912d-611c-4a6e-ab9d-0243cba331f1
ms.topic: article
ms.date: 05/31/2018
---

# Security Blanket Negotiation

A security blanket is a group of values that describe the security settings that apply to all proxies in a process or to just a particular interface proxy. A security blanket comprises the following values:

-   Authentication service
-   Authorization service
-   Principal name
-   Authentication level
-   Impersonation level
-   Authentication identity
-   Capabilities
-   An access control list (ACL) (servers only)

Security blanket negotiation is the process that COM uses to choose the security settings for a proxy when it is created. This process involves comparing the server's security blanket with the client's security blanket and using those values to create an appropriate default security blanket for the proxy. The following paragraphs explain where the client's and the server's security blankets come from and describe how COM negotiates the security blanket for the proxy using the client's and server's security blankets.

The client and the server can each call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to specify their respective security blankets. If an application doesn't call **CoInitializeSecurity** explicitly, COM calls it implicitly for the application, using appropriate default values. For more information about these default values, see [COM Security Defaults](com-security-defaults.md).

Some parameters to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) apply when the application is a server, and some apply when the application is a client. When the application is acting as a server, these parameters are relevant: an ACL, a list of authentication service/authorization service/principal name tuples, and an authentication level. A server's call to **CoInitializeSecurity**, whether implicit or explicit, determines the server's security blanket, which remains fixed.

When the application is acting as a client, the following values passed to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) are relevant: an authentication level, an impersonation level, the authentication identity, and capabilities. A client's implicit or explicit call to **CoInitializeSecurity** indicates the security blanket that the client wants.

When a proxy is created, COM uses the values specified by the server's security blanket and the client's security blanket to negotiate a default security blanket that is appropriate for the proxy. COM picks an authentication service that works on both the client and server. The authorization service and principal name are chosen to work with the authentication service. For the authentication level, COM chooses the higher of the authentication levels specified by the client and the server. The impersonation level and the capabilities chosen by COM are the ones specified by the client. The authentication identity is the one specified by the client for the chosen authentication service.

Once the default security blanket has been computed, its values are assigned to the newly created proxy. The client can override the security settings for the proxy by calling [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket). The values specified to **SetBlanket** are not negotiated; they are simply assigned to the specified proxy. However, if default parameters (such as RPC\_C\_IMP\_LEVEL\_DEFAULT) are passed to **SetBlanket**, COM uses the previously described security blanket negotiation algorithm to compute the default parameters.

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 