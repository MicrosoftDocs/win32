---
description: COM+ provides several security features that you can use to help protect your COM+ applications, ranging from services you configure administratively to APIs you can call within code.
ms.assetid: 686fb391-d337-41b4-bb51-b70f27a0c300
title: COM+ Security Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Security Concepts

COM+ provides several security features that you can use to help protect your COM+ applications, ranging from services you configure administratively to APIs you can call within code.

Whenever possible, for COM+ applications, it is better to use automatic security, such as declarative role-based security and authentication, rather than configuring security within components. Using automatic security makes it easier to write and maintain components, easier to design security across an entire application, and, because it is configured administratively, easier to modify an application's security policy. These automatic security services make it possible for you to leave all security-related functionality out of your components. When you can turn on the services and configure them appropriately, COM+ will handle the details of enforcing the security policy you specify.

However, when the automatic security services in COM+ don't do precisely what you need them to do, you can extend them, building on the automatic security platform provided by COM+. In cases where you choose not to use automatic security or where you want to use it but need to build on it to suit your application's security requirements, you have the following options for configuring security programmatically:

-   Programmatic role-based security—for example, role checking, which is available when role-based security is enabled for your application.
-   Impersonation—for when you want to use a client's identity to access a protected resource.
-   Auditing features based on security call context information—also available when role-based security is enabled.

Which mechanisms you use to help protect a given application will depend on the particular requirements of that application. Some security choices can affect how you write components, and some can significantly affect the application's design. Before you make any decisions about how to implement a security strategy for an application, you should consider its security requirements in the context of its overall design—performance requirements, data access, physical design—and choose the most suitable combination of security features. For more information about implementing programmatic security, see [Programmatic Component Security](programmatic-component-security.md).

Brief descriptions of COM+ security categories, features, and issues are provided here, with links to topics in this section that provide a detailed discussion of each of the important areas.

> [!Note]  
> Although not discussed in this section, queued components also have particular issues relating to what security features are available to them. For details, see [Queued Components Security](queued-components-security.md) and [Developing Queued Components](developing-queued-components.md).

 

## Role-Based Security

Role-based security is the central feature of COM+ application security. Using roles, you can administratively construct an authorization policy for an application, choosing (down to the method level, if necessary) which users can access which resources. Additionally, roles provide a framework for enforcing security-checking within code if your application requires finer-grained access control.

Role-based security is built on a general mechanism that enables you to retrieve security information regarding all upstream callers in the chain of calls to your component. This facility is useful particularly if you wish to do detailed auditing and logging. For a description of the auditing features provided by COM+, see [Accessing Security Call Context Information](accessing-security-call-context-information.md).

For a description of role-based security and administration issues that you should consider when using it, see [Role-Based Security Administration](role-based-security-administration.md).

## Client Authentication

Before you can authorize clients to be able to access resources, you must be confident that they are who they say they are. To enable this identity verification, COM+ provides authentication services. While these services are actually provided at a more fundamental level by COM and Microsoft Windows, a COM+ application lets you simply turn on the authentication service administratively so that it works under the covers, transparent to the application. For a description of authentication services, see [Client Authentication](client-authentication.md).

## Client Impersonation and Delegation

In some cases, your application needs to do work on behalf of a client using the client's identity—for example, when accessing a database that is going to authenticate the original client. This requires your application to impersonate the client. COM+ provides facilities to enable various levels of impersonation. Impersonation is configured administratively, but you also must provide support for impersonation with the code of your application's components. For a description of impersonation and issues concerning its use, see [Client Impersonation and Delegation](client-impersonation-and-delegation.md).

## Using the Software Restriction Policy in COM+

A software restriction policy provides a way to run untrusted, and therefore potentially harmful, code in a constrained environment so that it cannot misuse the privileges of the user. It does this by assigning trust levels to files that the user can run. For example, certain system files can be fully trusted and given unrestricted access to the privileges of the user, while a file that was downloaded from the Internet might be completely untrusted and therefore allowed to run only in a restricted environment where it is disallowed from using any security-sensitive user privileges.

The systemwide software restriction policy is controlled through the Local Security Policy administrative tool, which enables administrators to configure trust levels for individual files. However, all COM+ server applications run in the dllhost.exe file. Therefore COM+ provides a way to specify the software restriction policy for each server application so that they do not need to depend on the restriction policy of the dllhost.exe file. For a discussion concerning how to use the software restriction policy in COM+, see [Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md).

## Library Application Security

Library applications have special security considerations. Because these applications run in the client's process, they are affected by the security enforced by the hosting process while unable to control process-level security. For a description of factors to consider for library applications, see [Library Application Security](library-application-security.md).

## Multi-Tier Application Security

COM+ applications are typically middle-tier applications; that is, they move information between clients and back-end resources such as databases. Difficult choices can be involved in determining where security should be enforced and to what degree. Security inherently involves performance trade-offs. Some of the most severe of these occur when you must enforce security checking at both the data tier and the middle-tier. For a discussion of issues to consider, see [Multi-Tier Application Security](multi-tier-application-security.md).

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[COM+ Security Tasks](com--security-tasks.md)
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

 

 



