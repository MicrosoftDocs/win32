---
description: Retrieves information about an assembly when using managed code in the .NET Framework common language runtime.
ms.assetid: 45dcdc6a-74df-4763-ba8b-82f604db78d4
title: ClrAssemblyLocator class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ClrAssemblyLocator
api_type: 
- COM
---

# ClrAssemblyLocator class

Retrieves information about an assembly when using managed code in the .NET Framework common language runtime.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|-------------------------------------------------------|
| CLSID      | GUID\_AssemblyLocator                                 |
| ProgID     | L"System.EnterpriseServices.Internal.AssemblyLocator" |
| Interfaces | [**IAssemblyLocator**](/windows/desktop/api/ComSvcs/nn-comsvcs-iassemblylocator)          |



 

## When to use

Use this class to access the methods of [**IAssemblyLocator**](/windows/desktop/api/ComSvcs/nn-comsvcs-iassemblylocator).

## Remarks

To create this object, call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. A ClrAssemblyLocator object can be declared using "COMSVCSLib.ClrAssemblyLocator" as the class name.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



 

