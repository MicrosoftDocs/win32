---
description: You use role-based security to establish an authorization policy, determining which client or clients to let in and with what authority. You are deciding who should be able to perform which actions and access which resources.
ms.assetid: 8fc27fe1-e50a-44ba-a595-70b1fe463e24
title: Using Roles for Client Authorization
ms.topic: article
ms.date: 05/31/2018
---

# Using Roles for Client Authorization

You use role-based security to establish an authorization policy, determining which client or clients to let in and with what authority. You are deciding who should be able to perform which actions and access which resources.

Roles facilitate this by acting as an access control mechanism invoked whenever a user attempts to access any application resource. A role is basically a list of users—more precisely, a symbolic category of users that share the same security privilege. When you assign a role to an application resource, you are granting access permission for that resource to whoever is a member of that role.

Therefore, you can define a very particular security privilege by declaring it as a role and then assigning the role to specific resources. When the application is deployed, the system administrator can populate the role with actual users and user groups. When the application runs, COM+ will enforce the policy by carrying out role checks.

Fundamentally, roles help protect your code—that is, the methods that can be called by clients of a COM+ application. Role membership is checked whenever a client attempts to call a method exposed by a component in an application. If the caller is in a role assigned to the called method, or resource, the call succeeds; otherwise, it fails.

## Declarative Role-Based Security

With declarative role-based security, you administratively declare roles—using either the Component Services administrative tool or the Administrative functions—and administratively assign them to application resources. Where and how you set declarative security will determine where security boundaries are drawn for your application. For more detail, see [Security Boundaries](security-boundaries.md).

You can assign a given role to the entire application, to a particular component, to a particular interface in a component, or to a particular method on an interface. Role assignments are inherited down the natural chain of inclusion—that is, if you assign a role to a component, it is implicitly assigned to every interface and method exposed by that component.

With the availability of method-level role assignments, you can effectively help protect components and interfaces that have not been designed with security in mind. However, if the methods themselves are not securable with declarative role assignments, you might need to do programmatic role checking. It is generally a good idea to keep security in mind when deciding how to factor business functionality through methods; otherwise, you could find yourself adding in security-related code at the last minute.

For detailed procedures for setting role-based security, see [Configuring Role-Based Security](configuring-role-based-security.md).

## Programmatic Security

In some circumstances you may want to put security logic into components while still using role-based security. It might be that you're not able to—or choose not to—factor all access decisions through methods. For example, you might have a private application resource, perhaps a particular database, that you want to allow only some callers of a method to access while excluding others. Or you might have a single TransferMoney method and want to restrict some callers by limiting the amount they can transfer.

In such circumstances, you can do role checking in code. A simple API is provided, enabling you to check whether security is turned on and whether a caller or a particular user is in a given role. This functionality is available only when role-based security is enabled. This means that you can still take advantage of declarative role-based security where it suffices, and then you can programmatically extend it to a finer level of granularity when necessary.

Additionally, when you use role-based security, you have programmatic access to information regarding all upstream callers in the chain of calls to your component. This is especially useful when you want to keep a detailed audit trail.

For descriptions of how to do role checking in code and how to access security call context information, see [Programmatic Component Security](programmatic-component-security.md).

## Authorization and Authentication

Meaningful authorization presupposes that you are confident that clients are actually who they say they are. The verification of client identity is handled separately by an authentication service. Without authentication, you are basically letting callers in on the honor system. For descriptions of authentication as it impacts COM+ applications, see [Client Authentication](client-authentication.md).

## Related topics

<dl> <dt>

[Designing Roles Effectively](designing-roles-effectively.md)
</dt> <dt>

[Security Boundaries](security-boundaries.md)
</dt> <dt>

[Security Call Context Information](security-call-context-information.md)
</dt> <dt>

[Security Context Property](security-context-property.md)
</dt> </dl>

 

 



