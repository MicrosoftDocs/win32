---
title: Msvm\_ResourcePoolComponent class
description: Represents a resource pool element of the Microsoft Windows Hyper-V platform.
ms.assetid: a1245059-6202-4024-a35a-fb8c7586200b
keywords:
- Msvm_ResourcePoolComponent class Hyper-V
- Msvm_ResourcePoolComponent class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ResourcePoolComponent
- Msvm_ResourcePoolComponent.Name
- Msvm_ResourcePoolComponent.CLSID
- Msvm_ResourcePoolComponent.Context
- Msvm_ResourcePoolComponent.Enabled
- Msvm_ResourcePoolComponent.ResourcePoolClassName
- Msvm_ResourcePoolComponent.AllocationCapabilitiesClassName
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

# Msvm\_ResourcePoolComponent class

Represents a resource pool element of the Microsoft Windows Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_ResourcePoolComponent : Msvm_VirtualizationComponent
{
  string  Name;
  string  CLSID;
  uint32  Context = 1;
  boolean Enabled = True;
  string  ResourcePoolClassName;
  string  AllocationCapabilitiesClassName;
};
```

## Members

The **Msvm\_ResourcePoolComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ResourcePoolComponent** class has these properties.

<dl> <dt>

**AllocationCapabilitiesClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the class derived from [**CIM\_AllocationCapabilities**](https://msdn.microsoft.com/library/cc136804) that describes the allocation capabilities of this resource pool.

</dd> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A **GUID** that represents the class identifier of the service's COM object. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md).

</dd> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The context in which the newly created object will run. This value is passed in the *dwClsContext* parameter to **CoCreateInstance**. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md) and it is always set to 1.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this instance is enabled and can be used to complete client requests. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md) and it is always set to true.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A language-neutral string that uniquely identifies the element. The following format is suggested to prevent naming conflicts: "vendor\|component\|version". For example, this name represents version 1.0 of the Microsoft Emulated Network Port Component: "Microsoft\|EmulatedNetworkPortComponent\|V1.0". This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md).

</dd> <dt>

**ResourcePoolClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the class derived from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) that implements the resource pool.

</dd> </dl>

## Remarks

Access to the **Msvm\_ResourcePoolComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md)
</dt> <dt>

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





