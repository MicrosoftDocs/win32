---
Description: When role-based security is being used, the security call context object can be used to access security information about the current call.
ms.assetid: 9fc0a9e5-934c-4510-8fbb-1fb2817aa0ea
title: Accessing Security Call Context Information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing Security Call Context Information

When role-based security is being used, the security call context object can be used to access security information about the current call.

The following collections of properties are available from the security call context object:

-   [SecurityCallContext Collection](#securitycallcontext-collection)
-   [SecurityCallers Collection](#securitycallers-collection)
-   [SecurityIdentity Collection](#securityidentity-collection)
-   [Related topics](#related-topics)

## SecurityCallContext Collection



| Property                          | Description                                                                                                                            |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| NumCallers<br/>             | The number of callers in the chain of calls.<br/>                                                                                |
| MinAuthenticationLevel<br/> | The least secure authentication level of all callers in the chain.<br/>                                                          |
| Callers<br/>                | Information about the identity of upstream callers, in the form of a [**SecurityCallers**](/windows/win32/ComSvcs/?branch=master) collection.<br/> |
| DirectCaller<br/>           | The caller that called the object directly (with no intervening callers). <br/>                                                  |
| OriginalCaller<br/>         | The caller that originated the chain of calls to the object. <br/>                                                               |



 

For more information about how to use this collection, Microsoft Visual Basic developers should see the [**SecurityCallContext**](/windows/win32/ComSvcs/?branch=master) class. C and C++ developers should refer to [**ISecurityCallContext**](/windows/win32/ComSvcs/nn-comsvcs-isecuritycallcontext?branch=master).

## SecurityCallers Collection

The [**SecurityCallers**](/windows/win32/ComSvcs/?branch=master) collection represents callers that can be retrieved by using an index between 0 and 1 less than NumCallers, inclusive. Each caller is represented by a [**SecurityIdentity**](/windows/win32/ComSvcs/?branch=master) object.

For more information about this collection, Visual Basic developers should see the [**SecurityCallers**](/windows/win32/ComSvcs/?branch=master) class. C and C++ developers should refer to [**ISecurityCallersColl**](/windows/win32/ComSvcs/nn-comsvcs-isecuritycallerscoll?branch=master).

## SecurityIdentity Collection



| Property                         | Description                                                                                                                                                          |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SID<br/>                   | The security identifier for the caller.<br/>                                                                                                                   |
| AccountName<br/>           | The account name of the caller.<br/>                                                                                                                           |
| AuthenticationService<br/> | The authentication service used, such as NTLMSSP, Kerberos, or SSL.<br/>                                                                                       |
| AuthenticationLevel<br/>   | The authentication level used, which represents the amount of protection used when communicating with the object.<br/>                                         |
| ImpersonationLevel<br/>    | The level of impersonation set by the client, if impersonation was used. This level indicates the amount of authority given to the server by the client. <br/> |



 

For more information on this collection, Visual Basic developers should see the [**SecurityIdentity**](/windows/win32/ComSvcs/?branch=master) class. C and C++ developers should refer to [**ISecurityIdentityColl**](/windows/win32/ComSvcs/nn-comsvcs-isecurityidentitycoll?branch=master).

## Related topics

<dl> <dt>

[Checking Role Membership](checking-role-membership.md)
</dt> <dt>

[Determining Whether Role-Based Security Is Enabled](determining-whether-role-based-security-is-enabled.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> </dl>

 

 




