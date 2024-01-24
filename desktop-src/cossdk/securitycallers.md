---
description: Provides access to information about individual callers in a collection of callers. The collection represents the chain of calls ending with the current call, and each caller in the collection represents the identity of one caller.
ms.assetid: 164fe12d-eeb3-402f-8aa3-e3545904d9c4
title: SecurityCallers class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SecurityCallers
api_type: 
- COM
---

# SecurityCallers class

Provides access to information about individual callers in a collection of callers. The collection represents the chain of calls ending with the current call, and each caller in the collection represents the identity of one caller. Only callers who cross a boundary where security is checked are included in the chain of callers. (In the COM+ environment, security is checked at application boundaries.) Access to information about a particular caller's identity is provided through the [**SecurityIdentity**](securityidentity.md) class, an identity collection.

Only COM+ applications that use role-based security can access the **SecurityCallers** class. For more information on roles, see [Role-Based Security Administration](role-based-security-administration.md).

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|------------------------------------------------------|
| Interfaces | [**ISecurityCallersColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallerscoll) |



 

## When to use

Use this class to access the methods of [**ISecurityCallersColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallerscoll).

## Remarks

You cannot directly create a **SecurityCallers** object. To use the methods of [**ISecurityCallersColl**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallerscoll), you must obtain a reference to its implementation by calling [**CoGetCallContext**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetcallcontext), supplying IID\_ISecurityCallContext for the *riid* parameter. Next, call [**ISecurityCallContext::get\_Item**](/windows/desktop/api/ComSvcs/nf-comsvcs-isecuritycallcontext-get_item) requesting a security call context item that is a security identity collection (such as "DirectCaller" or "OriginalCaller").

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. You cannot directly create a SecurityCallers object. To use its properties, you must obtain a refernece to its implementation using [**GetSecurityCallContext**](/windows/desktop/api/ComSvcs/nf-comsvcs-igetsecuritycallcontext-getsecuritycallcontext). Next, get the Item property of the object, requesting a security call context item that is a security identity collection (such as "DirectCaller" or "OriginalCaller").

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

[**SecurityIdentity**](securityidentity.md)
</dt> </dl>

 

