---
description: The Win32\_MethodParameterClass abstract, base WMI class derives any class defined as a container of parameter values that will be passed to a method.
ms.assetid: 293fa378-432d-4e97-a8ab-8dc4917d5476
ms.tgt_platform: multiple
title: Win32_MethodParameterClass class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_MethodParameterClass
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_MethodParameterClass class

The **Win32\_MethodParameterClass** abstract, base [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) derives any class defined as a container of parameter values that will be passed to a method. Having no properties of its own, this class serves as a classification node. A similar example is [**CIM\_PhysicalElement**](cim-physicalelement.md). Derivation from **CIM\_PhysicalElement** indicates that the class describes a physical rather than logical entity. In the case of **Win32\_MethodParameterClass**, classes derived from it are created specifically to pass parameters to a method.

## Syntax

## Members

The **Win32\_MethodParameterClass** class does not define any members.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[WMI Service Management Classes](/windows/desktop/CIMWin32Prov/wmi-service-management-classes)
</dt> </dl>

 

