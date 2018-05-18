---
title: Msvm\_VirtualSystemResourceRegistration class
description: Registers a service that provides virtual system-specific resource-related objects.
ms.assetid: '864d3db2-b711-4550-9e8f-d77a675b23ce'
keywords: ["Msvm_VirtualSystemResourceRegistration class Hyper-V", "Msvm_VirtualSystemResourceRegistration class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemResourceRegistration
- Msvm_VirtualSystemResourceRegistration.ResourceType
- Msvm_VirtualSystemResourceRegistration.Component
- Msvm_VirtualSystemResourceRegistration.IsRootDevice
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VirtualSystemResourceRegistration class

Registers a service that provides virtual system-specific resource-related objects.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class Msvm_VirtualSystemResourceRegistration : Msvm_VirtualizationComponentRegistration
{
  Msvm_ResourceTypeDefinition         REF ResourceType;
  Msvm_VirtualSystemResourceComponent REF Component;
  boolean                                 IsRootDevice = False;
};
```

## Members

The **Msvm\_VirtualSystemResourceRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemResourceRegistration** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemResourceComponent**](msvm-virtualsystemresourcecomponent.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Component")
</dt> </dl>

A reference to an instance that describes the COM object that implements this class.

</dd> <dt>

**IsRootDevice**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, this registration indicates whether the specified resource type is the root (or parent-less) device for this service. Only one registration may exist with **IsRootDevice** to set true. Otherwise, this registration represents a mapping to a sub-device. This property is always set to **False**.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ResourceTypeDefinition**](msvm-resourcetypedefinition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to an instance that describes a resource type supported by the service. This property is inherited from [**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemResourceRegistration** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md)
</dt> <dt>

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





