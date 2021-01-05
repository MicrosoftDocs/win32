---
description: Role-Based Security Administration
ms.assetid: 7247758e-f486-4ce2-afca-f0d10fffe626
title: Role-Based Security Administration
ms.topic: article
ms.date: 05/31/2018
---

# Role-Based Security Administration

Role-based security is an automatic service provided by COM+ that enables you to administratively construct and enforce an access control policy for your COM+ application. With a flexible and extensible security configuration model, role-based security offers a considerable advantage over enforcing all security within your components and provides the following benefits:

-   You can configure security administratively, using either the Component Services administrative tool or the Administrative functions.
-   You don't have to write security-related logic into your components when role protection at the method level provides you with fine enough access control.
-   You don't have to factor security into interface or component design. Instead, you can set security on a method-by-method basis.
-   You can focus on the structure of the security policy you want to enforce, and through roles, that policy can be clearly expressed to the administrators deploying your application.
-   You can easily modify a security policy to adapt to evolving security requirements for an application.
-   You can build more granular security policies programmatically if you need to, using role-based security as a supporting platform.
-   You can leverage role-based security to do detailed auditing, because you can obtain caller security information for an entire chain of upstream calls.

> [!Note]  
> Users in the Administrator role for the System Application must be members of the local administrators group. Also, as of Windows Server 2003, the authentication capability for the COM+ System Application includes the value EOAC\_DISABLE\_AAA. This value, which disables activate-as-activator (AAA) activations, is used in the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) call when launching the System Application. Setting the authentication capability to EOAC\_DISABLE\_AAA allows an application that runs under a privileged account (such as LocalSystem) to help prevent its identity from being used to launch untrusted components.

 

See the following topics in this section for information about how role-based security works and issues to consider when using it to construct a security policy for an application:

-   [Using Roles for Client Authorization](using-roles-for-client-authorization.md)
-   [Designing Roles Effectively](designing-roles-effectively.md)
-   [Security Boundaries](security-boundaries.md)
-   [Security Call Context Information](security-call-context-information.md)
-   [Security Context Property](security-context-property.md)

For detailed how-to descriptions of the steps involved in configuring role-based security for an application, see [Configuring Role-Based Security](configuring-role-based-security.md).

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Library Application Security](library-application-security.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 
