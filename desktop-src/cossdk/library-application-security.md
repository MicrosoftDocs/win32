---
description: Because a COM+ library application is hosted by another process, which may have its own security settings, security for library applications requires special consideration.
ms.assetid: a966020c-a0bd-467c-b6d3-e09267cf5574
title: Library Application Security
ms.topic: article
ms.date: 05/31/2018
---

# Library Application Security

Because a COM+ library application is hosted by another process, which may have its own security settings, security for library applications requires special consideration.

The following constraints apply to library application security:

-   Library applications run under the client process security token rather than under their own user identity. They have only as much privilege as the client has.
-   Library applications do not control process-level security. No users in roles will be added to the security descriptor for the process. The only way for a library application to perform its own access checks is to use component-level security. (See [Security Boundaries](security-boundaries.md).)
-   Library applications can be configured to either participate or not participate in host process authentication, by enabling or disabling authentication. (See [Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md).)
-   Library applications cannot set an impersonation level; they use that of the host process.

## Using Library Applications to Limit Application Privilege

In some cases, you may want to configure an application specifically as a library application so that it runs under the identity of the hosting process. Doing so fundamentally limits the application so that it can access only those resources that its client, the host process, can access. The threads that the library application components run on will use the process token by default, and therefore when they make calls outside of the application or access resources such as files guarded with a security descriptor, they will appear to be the client. For applications that perform sensitive work, this may be an easy way to control the scope of their actions.

## Effectively Securing Library Applications

There are special considerations in configuring role-based security and authentication for library applications so that they perform as expected. For details, see [Configuring Security for Library Applications](configuring-security-for-library-applications.md).

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 



