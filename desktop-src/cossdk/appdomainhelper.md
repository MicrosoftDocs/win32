---
description: Binds a managed object to an application domain, which is an isolated environment where applications execute.
ms.assetid: 9357ea5d-6f86-4747-a923-16575ff13122
title: AppDomainHelper class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AppDomainHelper
api_type: 
- COM
---

# AppDomainHelper class

Binds a managed object to an application domain, which is an isolated environment where applications execute.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|-------------------------------------------------------|
| CLSID      | GUID\_AppDomainHelper                                 |
| ProgID     | L"System.EnterpriseServices.Internal.AppDomainHelper" |
| Interfaces | [**IAppDomainHelper**](/windows/desktop/api/ComSvcs/nn-comsvcs-iappdomainhelper)          |



 

## When to use

Use this class to access the methods of [**IAppDomainHelper**](/windows/desktop/api/ComSvcs/nn-comsvcs-iappdomainhelper).

## Remarks

To create this object, call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. An AppDomainHelper object can be declared using "COMSVCSLib.AppDomainHelper" as the class name.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



## See also

<dl> <dt>

[**IAppDomainHelper**](/windows/desktop/api/ComSvcs/nn-comsvcs-iappdomainhelper)
</dt> </dl>

 

