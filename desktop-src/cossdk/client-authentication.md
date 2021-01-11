---
description: Authentication is the process of determining that callers are actually who they say they are&\#8212;verifying the authenticity of a claim of identity.
ms.assetid: c1b11f58-5bab-45d9-a686-86c95415990e
title: Client Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Client Authentication

Authentication is the process of determining that callers are actually who they say they are—verifying the authenticity of a claim of identity. In general, this can be done by both server and client, each authenticating the other. But it is especially important for a server application that is authorizing clients, as with role-based security, to do authentication as well. Authenticating clients is a prerequisite for a meaningful authorization policy. You can do all the role checking you want, but if you don't know for certain that the client identity you are checking is authentic, your application is basically relying on the honor system.

For COM+ applications, authentication is something you can turn on and configure administratively, after which it works transparently to the application. You specify an authentication level administratively by using the Component Services administrative tool or the Administrative functions. For details about setting authentication, see [Setting an Authentication Level for a Server Application](setting-an-authentication-level-for-a-server-application.md) and [Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md).

Setting authentication means different things depending on whether the type of application is a server or library application.

## Setting Authentication for COM+ Server Applications

For a COM+ server application, you set an authentication level that determines how authentication will be performed when clients call into components within the application. You can choose from several authentication levels that provide varying degrees of security, ranging from no authentication to encryption of every packet and all method call parameters. For more information, see [Setting an Authentication Level for a Server Application](setting-an-authentication-level-for-a-server-application.md).

Higher security comes with some performance cost, however, which you should take into consideration when configuring your application. COM+ will negotiate between the authentication level specified by client and server. The way this negotiation is carried out has the benefit of enabling you to administratively control authentication from the server side alone. For details, see [Negotiation of Authentication Level](negotiation-of-authentication-level.md).

> [!Note]  
> You should never specify an authentication level programmatically by using [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) within a COM+ application. COM+ calls **CoInitializeSecurity** for you, and this can be called only once per process.

 

The underlying authentication services are provided by COM and Microsoft Windows. In an authentication service, a third party supplies a certificate for a user, attesting to the authenticity of the user's identity. This certification is as credible as the certifying authority, and—in much the same way as a driver's license or a passport serves as a certifying document—it depends on the issuer's authority. For more detailed information about authentication services, see [COM and Security Packages](/windows/desktop/com/com-and-security-packages) in the COM documentation.

## Setting Authentication for COM+ Library Applications

For a COM+ library application, you enable or disable authentication to determine whether the application will be subject to the authentication performed by the hosting process. Although authentication for a COM+ library application is largely controlled by the hosting process, you can configure the library application so that it will not participate in authentication. That is, calls into the application can be authenticated or unauthenticated, and in the latter case, "authentication" of clients always succeeds. For more information, see [Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md).

Additionally, you may want or be required to authenticate the client at the database or at some downstream application—authenticating clients at the COM+ application alone might not suffice. If this is the case, you need to impersonate the client so that the client's identity is propagated downstream. For detailed information about impersonation, see [Client Impersonation and Delegation](client-impersonation-and-delegation.md). For a discussion of issues involved in deciding whether to do authentication at the data tier, see [Multi-Tier Application Security](multi-tier-application-security.md).

## Related topics

<dl> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Library Application Security](library-application-security.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 
