---
description: When you use role-based security in the COM+ application that contains your component, you have access to programmatic security functionality from within your component.
ms.assetid: 6117970c-5dbd-485e-978e-3aa96e42b359
title: Programmatic Component Security
ms.topic: article
ms.date: 05/31/2018
---

# Programmatic Component Security

When you use role-based security in the COM+ application that contains your component, you have access to programmatic security functionality from within your component. You can check role membership to determine whether particular sections of code are executed, you can access security information using the security call context object, and you can determine whether security is enabled for the current call. You can perform all of these tasks by using a reference to a [**SecurityCallContext**](securitycallcontext.md) object (for Microsoft Visual Basic applications) or a pointer to the [**ISecurityCallContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallcontext) interface (for C and Microsoft Visual C++ applications).

For more information regarding programmatic role-based security, see the following topics in this section:

-   [Checking Role Membership](checking-role-membership.md)
-   [Determining Whether Role-Based Security Is Enabled](determining-whether-role-based-security-is-enabled.md)
-   [Accessing Security Call Context Information](accessing-security-call-context-information.md)

## Impersonation and COM Security Features

If your component is used in a COM+ application that does not use role-based security, programmatic role checking and security call context information are not available. However, you can use the programmatic security functionality provided by COM. For more information, see [Security in COM](/windows/desktop/com/security-in-com).

Although you can use most of the security functionality provided by COM, you cannot call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) from a component that is part of a COM+ application because **CoInitializeSecurity** is called by the surrogate that the COM+ application runs in. However, you can call other security functions, such as [**CoQueryClientBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryclientblanket), which retrieves information about the client.

In particular, when you need to use the client's identity to access some resource—for example, accessing a file protected by a security descriptor, or propagating the client's identity through to a database—you can perform impersonation programmatically. For more detail about when and how to do this, see [Client Impersonation and Delegation](client-impersonation-and-delegation.md).

## Testing Security Functionality

If you use COM+ programmatic security in your component, you must integrate the component into a COM+ application when you are ready to test the component's security functionality. If a component using COM+ programmatic security is run without being integrated into a COM+ application, exceptions will be thrown. Therefore, if you want to ensure that such a component is also capable of being successfully integrated into an application that is not part of the COM+ environment, you must ensure that these exceptions are handled appropriately.

## Documenting Security Requirements

If you are writing a stand-alone component for COM+ applications that use role-based security, you need to document the component so that security can be configured appropriately when the component is integrated into a COM+ application. For example, you should identify the roles that must be added and explain which methods and interfaces each role should be assigned to. In addition, if a method such as IsCallerInRole("Teller") is called, you should describe the functionality that only Tellers have access to. You should also specify whether a role is required to help protect access to the entire component.

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

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 
