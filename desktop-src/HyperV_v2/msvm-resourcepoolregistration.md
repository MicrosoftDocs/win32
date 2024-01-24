---
description: Registers a service that provides global resource pool-related objects.
ms.assetid: B602F6E1-2889-43CF-AAF1-40F339231DB4
title: Msvm_ResourcePoolRegistration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ResourcePoolRegistration
- Msvm_ResourcePoolRegistration.ResourceType
- Msvm_ResourcePoolRegistration.Component
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ResourcePoolRegistration class

Registers a service that provides global resource pool-related objects.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
class Msvm_ResourcePoolRegistration : Msvm_VirtualizationComponentRegistration
{
  Msvm_ResourceTypeDefinition REF ResourceType;
  Msvm_ResourcePoolComponent  REF Component;
};
```

## Members

The **Msvm\_ResourcePoolRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ResourcePoolRegistration** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ResourcePoolComponent**](msvm-resourcepoolcomponent.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance that describes the COM object that implements this class.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ResourceTypeDefinition**](msvm-resourcetypedefinition.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance that describes a resource type supported by the service. This property is inherited from [**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ResourcePoolRegistration** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| End of client support<br/>    | Windows 8.1<br/>                                                                                  |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualizationComponentRegistration**](/windows/desktop/HyperV_v2/msvm-virtualizationcomponentregistration)
</dt> <dt>

[**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md)
</dt> </dl>

 

