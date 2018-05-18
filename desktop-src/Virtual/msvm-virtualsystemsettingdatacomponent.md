---
title: Msvm\_VirtualSystemSettingDataComponent class
description: A generic association used to establish 'part of' relationships between one instance of CIM\_VirtualSystemSettingData and one or more instances of CIM\_ResourceAllocationSettingData.
ms.assetid: '8e13bfb2-d0a6-4d4c-a19c-9a9645f7e098'
keywords: ["Msvm_VirtualSystemSettingDataComponent class Hyper-V", "Msvm_VirtualSystemSettingDataComponent class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSettingDataComponent
- Msvm_VirtualSystemSettingDataComponent.GroupComponent
- Msvm_VirtualSystemSettingDataComponent.PartComponent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VirtualSystemSettingDataComponent class

A generic association used to establish 'part of' relationships between one instance of [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and one or more instances of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemSettingDataComponent : CIM_VirtualSystemSettingDataComponent
{
  CIM_VirtualSystemSettingData      REF GroupComponent;
  CIM_ResourceAllocationSettingData REF PartComponent;
};
```

## Members

The **Msvm\_VirtualSystemSettingDataComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemSettingDataComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent element in the association. This property is inherited from [**CIM\_VirtualSystemSettingDataComponent**](https://msdn.microsoft.com/library/mt146366).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The child element in the association. This property is inherited from [**CIM\_VirtualSystemSettingDataComponent**](https://msdn.microsoft.com/library/mt146366).

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemSettingDataComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_VirtualSystemSettingDataComponent**](cim-virtualsystemsettingdatacomponent.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingDataComponent**](https://msdn.microsoft.com/library/mt146366)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





