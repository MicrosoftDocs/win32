---
description: Properly using the software restriction policy can make your business more agile because it provides a proactive framework for preventing problems, rather than a reactive framework that relies on the costly alternative of restoring a system after a problem has occurred. The software restriction policy was introduced with the release of Microsoft Windows XP to help protect systems from unknown and possibly dangerous code. The restriction policy provides a mechanism where only trusted code is given unrestricted access to a users privileges. Unknown code, which might contain viruses or code that conflicts with currently installed programs, is allowed to run only in a constrained environment (often called a sandbox) where it is disallowed from accessing any security-sensitive user privileges.
ms.assetid: 233483a0-ff16-4e21-a312-cc57a92124c3
title: Using the Software Restriction Policy in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Using the Software Restriction Policy in COM+

Properly using the software restriction policy can make your business more agile because it provides a proactive framework for preventing problems, rather than a reactive framework that relies on the costly alternative of restoring a system after a problem has occurred. The software restriction policy was introduced with the release of Microsoft Windows XP to help protect systems from unknown and possibly dangerous code. The restriction policy provides a mechanism where only trusted code is given unrestricted access to a user's privileges. Unknown code, which might contain viruses or code that conflicts with currently installed programs, is allowed to run only in a constrained environment (often called a *sandbox*) where it is disallowed from accessing any security-sensitive user privileges.

The software restriction policy depends on assigning trust levels to the code that can run on a system. Currently, two trust levels exist: Unrestricted and Disallowed. Code that has an Unrestricted trust level is given unrestricted access to the user's privileges, so this trust level should be applied only to fully trusted code. Code with a Disallowed trust level is disallowed from accessing any security-sensitive user privileges and can run only in a sandbox that helps prevent Unrestricted code from loading the Disallowed code into its address space.

Configuring the software restriction policy for a system is done through the Local Security Policy administrative tool, while the restriction policy configuration of individual COM+ applications is done either programmatically or through the Component Services administrative tool. If the restriction policy trust level is not specified for a COM+ application, the systemwide settings will be used to determine the application's trust level. The COM+ restriction policy settings must be carefully coordinated with the systemwide settings because a COM+ application that has an Unrestricted trust level can load only components with an Unrestricted trust level; a Disallowed COM+ application can load components with any trust level but cannot access all of the user's privileges.

In addition to the software restriction policy trust levels of individual COM+ applications, two other properties determine how the restriction policy is used for all COM+ applications. If [SRPRunningObjectChecks](/windows/desktop/com/srprunningobjectchecks) is enabled, attempts to connect to running objects will be checked for appropriate trust levels. The running object cannot have a less stringent trust level than the client object. For example, the running object cannot have a Disallowed trust level if the client object has an Unrestricted trust level.

The second property determines how the software restriction policy handles activate-as-activator connections. If [SRPActivateAsActivatorChecks](/windows/desktop/com/srpactivateasactivatorchecks) is enabled, the trust level that is configured for the server object is compared with the trust level of the client object and the more stringent trust level will be used to run the server object. If SRPActivateAsActivatorChecks is not enabled, the server object will run with the trust level of the client object regardless of the trust level with which it was configured. By default, both SRPRunningObjectChecks and SRPActivateAsActivatorChecks are enabled.

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Configuring the Software Restriction Policy](configuring-the-software-restriction-policy.md)
</dt> <dt>

[Library Application Security](library-application-security.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> </dl>

 

 
