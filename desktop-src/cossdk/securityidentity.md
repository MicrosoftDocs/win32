---
description: "Provides access to a collection of security information representing a caller's identity. Using this class, you can find out about a particular caller in a chain of callers that is part of the security call context."
ms.assetid: 'c6b28695-1b08-490a-8d56-eb55d82f3e7a'
title: 'SecurityIdentity class (ComSvcs.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SecurityIdentity
api_type: 
- COM
---

# SecurityIdentity class

Provides access to a collection of security information representing a caller's identity. Using this class, you can find out about a particular caller in a chain of callers that is part of the security call context. For more information about how security call context information is accessed, see Programmatic Component Security.

Only COM+ applications that use role-based security can access the **SecurityIdentity** class. For more information on roles, see [Role-Based Security Administration](role-based-security-administration.md).

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|--------------------------------------------------------|
| Interfaces | [**ISecurityIdentityColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecurityidentitycoll) |



 

## When to use

Use this class to access the methods of [**ISecurityIdentityColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecurityidentitycoll).

## Remarks

You cannot directly create a **SecurityIdentity** object. To use the methods of [**ISecurityIdentityColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecurityidentitycoll), you must obtain a reference to its implementation by calling [**CoGetCallContext**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetcallcontext), supplying IID\_ISecurityCallContext for the *riid* parameter. Next, call [**ISecurityCallContext::get\_Item**](/windows/desktop/api/ComSvcs/nf-comsvcs-isecuritycallcontext-get_item) requesting a security call context item that is a security identity collection (such as "DirectCaller" or "OriginalCaller"). Then call [**ISecurityIdentityColl::get\_Item**](/windows/desktop/api/ComSvcs/nf-comsvcs-isecurityidentitycoll-get_item) to retrieve a security identity item (such as "Name" or "AuthenticationService").

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. You cannot directly create a SecurityIdentity object. To use its properties, you must obtain a refernece to its implementation using [**GetSecurityCallContext**](/windows/desktop/api/ComSvcs/nf-comsvcs-igetsecuritycallcontext-getsecuritycallcontext). Next, get the Item property of the object, requesting a security call context item that is a security identity collection (such as "DirectCaller" or "OriginalCaller"). Then, use the Item property of the SecurityIdentity object to retrieve a security identity item (such as "Name" or "AuthenticationService").

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



## See also

<dl> <dt>

[**GetSecurityCallContext**](/windows/desktop/api/ComSvcs/nf-comsvcs-igetsecuritycallcontext-getsecuritycallcontext)
</dt> <dt>

[**ISecurityCallersColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallerscoll)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[**SecurityCallContext**](securitycallcontext.md)
</dt> <dt>

[**SecurityCallers**](securitycallers.md)
</dt> </dl>

 

