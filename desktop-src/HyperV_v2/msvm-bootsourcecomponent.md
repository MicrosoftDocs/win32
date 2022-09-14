---
description: Associates the Msvm\_BootSourceSettingData to the overall Msvm\_VirtualSystemSettingData.
ms.assetid: DB2E66F1-CC2C-49FC-96CE-D9DE441AA809
title: Msvm_BootSourceComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_BootSourceComponent
- Msvm_BootSourceComponent.GroupComponent
- Msvm_BootSourceComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_BootSourceComponent class

Associates the [**Msvm\_BootSourceSettingData**](msvm-bootsourcesettingdata.md) to the overall [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md). This class derives from [**CIM\_Component**](/windows/desktop/CIMWin32Prov/cim-component).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_BootSourceComponent : CIM_Component
{
  CIM_ManagedSystemElement REF GroupComponent;
  CIM_ManagedSystemElement REF PartComponent;
};
```

## Members

The **Msvm\_BootSourceComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_BootSourceComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the parent element in the association. This property is inherited from [**CIM\_Component**](cim-component.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the child element in the association. This property is inherited from [**CIM\_Component**](cim-component.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[**CIM\_Component**](/windows/desktop/CIMWin32Prov/cim-component)
</dt> <dt>

[**Msvm\_BootSourceSettingData**](msvm-bootsourcesettingdata.md)
</dt> <dt>

[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)
</dt> </dl>

 

