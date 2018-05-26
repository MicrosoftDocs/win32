---
title: Msvm\_VirtualizationComponentRegistration class
description: Represents the registration of a service in the Microsoft Hyper-V platform.
ms.assetid: e7907d9c-96df-4ea3-9983-2496a1f575c9
keywords:
- Msvm_VirtualizationComponentRegistration class Hyper-V
- Msvm_VirtualizationComponentRegistration class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualizationComponentRegistration
- Msvm_VirtualizationComponentRegistration.Component
- Msvm_VirtualizationComponentRegistration.ResourceType
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_VirtualizationComponentRegistration class

Represents the registration of a service in the Microsoft Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code.

## Syntax

``` syntax
[Abstract, Association, AMENDMENT]
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
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
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

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualizationComponentRegistration** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





