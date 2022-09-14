---
description: Represents the registration of a service in the Microsoft Hyper-V platform.
ms.assetid: 706557C2-49D6-453F-9DC0-2C655888EEBE
title: Msvm_VirtualizationComponentRegistration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualizationComponentRegistration
- Msvm_VirtualizationComponentRegistration.Component
- Msvm_VirtualizationComponentRegistration.ResourceType
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualizationComponentRegistration class

Represents the registration of a service in the Microsoft Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code.

## Syntax

``` syntax
class Msvm_VirtualizationComponentRegistration
{
  Msvm_VirtualizationComponent REF Component;
  Msvm_ResourceTypeDefinition  REF ResourceType;
};
```

## Members

The **Msvm\_VirtualizationComponentRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualizationComponentRegistration** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md)**
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

A reference to an instance that describes a resource type supported by the service.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualizationComponentRegistration** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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



 

