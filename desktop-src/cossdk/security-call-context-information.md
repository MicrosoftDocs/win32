---
Description: Security Call Context Information
ms.assetid: 9fc0a9e5-934c-4510-8fbb-1fb2817aa0ea
title: Security Call Context Information
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security Call Context Information

Role-based security is built on a general mechanism that enables you to retrieve security information regarding all upstream callers in the chain of calls to your component. This information is available only when you have component-level role checking enabled. For details about how to set component-level security, see [Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md).

You can use the [**ISecurityCallContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallcontext) interface to access security call context information programmatically. For a description, see [Programmatic Component Security](programmatic-component-security.md).

Security call context is passed along every time a security boundary is crossed. For calls between components within an application, which reside within the same security boundary, no call context information is passed. For calls between processes or between applications within a process, call context information flows along.

This facility is particularly useful if you wish to do detailed auditing and logging. You can retrieve and record security information for every upstream caller.

## Related topics

<dl> <dt>

[Designing Roles Effectively](designing-roles-effectively.md)
</dt> <dt>

[Security Boundaries](security-boundaries.md)
</dt> <dt>

[Security Context Property](security-context-property.md)
</dt> <dt>

[Using Roles for Client Authorization](using-roles-for-client-authorization.md)
</dt> </dl>

 

 



