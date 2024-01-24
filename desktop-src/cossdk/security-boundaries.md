---
description: Security is checked only at application boundaries.
ms.assetid: 32a05150-a68a-4302-9983-b9c1269b368c
title: Security Boundaries
ms.topic: article
ms.date: 05/31/2018
---

# Security Boundaries

Security is checked only at application boundaries. That is, for two components in the same application, when one component calls the other, no security check will be done. However, if two applications share the same process and a component in one calls a component in the other, a security check is done because an application boundary is crossed. Likewise, if two applications reside in different server processes and a component in the first application calls a component in the second application, a security check is done.

Therefore, if you have two components and you want security checks to be done when one calls the other, you need to put the components in separate COM+ applications.

Because COM+ library applications are hosted by other processes, there is a security boundary between the library application and the hosting process. Additionally, the library application doesn't control process-level security, which affects how you need to configure security for it. For more information, see [Library Application Security](library-application-security.md).

Determining whether a security check must be carried out on a call into a component is based on the security property on the object context created when the configured component is instantiated. For more information, see [Security Context Property](security-context-property.md).

## Component-Level Access Checks

For a COM+ server application, you have the choice of enforcing access checks either at the component level or at the process level.

When you select component-level access checking, you enable fine-grained role assignments. You can assign roles to components, interfaces, and methods and achieve an articulated authorization policy. This will be the standard configuration for applications using role-based security.

For COM+ library applications, you must select component-level security if you want to use roles. Library applications cannot use process-level security.

You should select component-level access checking if you are using programmatic role-based security. Security call context information is available only when component-level security is enabled. For more information, see [Security Call Context Information](security-call-context-information.md).

Additionally, when you select component-level access checking, the security property will be included on the object context. This means that security configuration can play a role in how the object is activated. For more information, see [Security Context Property](security-context-property.md).

## Process-Level Access Checks

Process-level checks apply only to the application boundary. That is, the roles that you have defined for the whole COM+ application will determine who is granted access to any resource within the application. No finer-grained role assignments apply. Essentially, the roles are used to create a security descriptor against which any call into the application's components is validated. In this case, you would not want to construct a detailed authorization policy with multiple roles. The application will use a single security descriptor.

For COM+ library applications, you would not select process-level access checks. The library application will run hosted in the client's process and hence will not control process-level security. For more information, see [Library Application Security](library-application-security.md).

With process-level access checks enabled, security call context information is not available. This means that you cannot do programmatic security when using only process-level security. For more information, see [Security Call Context Information](security-call-context-information.md).

Additionally, the security property will not be included on the object context. This means that when using only process-level access checks, security configuration will never play a role in how the object is activated. For more information, see [Security Context Property](security-context-property.md).

## Related topics

<dl> <dt>

[Designing Roles Effectively](designing-roles-effectively.md)
</dt> <dt>

[Security Call Context Information](security-call-context-information.md)
</dt> <dt>

[Security Context Property](security-context-property.md)
</dt> <dt>

[Using Roles for Client Authorization](using-roles-for-client-authorization.md)
</dt> </dl>

 

 



