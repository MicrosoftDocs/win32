---
title: Msvm\_ResourcePoolRegistration class
description: Registers a service that provides global resource pool-related objects.
ms.assetid: b6b26a65-b3cd-4305-96ce-e21721d8fc8c
keywords:
- Msvm_ResourcePoolRegistration class Hyper-V
- Msvm_ResourcePoolRegistration class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ResourcePoolRegistration
- Msvm_ResourcePoolRegistration.ResourceType
- Msvm_ResourcePoolRegistration.Component
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_ResourcePoolRegistration class

Registers a service that provides global resource pool-related objects.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Local(1033), AMENDMENT]
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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Component")
</dt> </dl>

A reference to an instance that describes the COM object that implements this class.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ResourceTypeDefinition**](msvm-resourcetypedefinition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to an instance that describes a resource type supported by the service.

This property is inherited from [**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ResourcePoolRegistration** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md)
</dt> <dt>

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





