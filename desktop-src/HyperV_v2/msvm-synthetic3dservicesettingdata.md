---
description: Represents the settings for the synthetic 3-D service present on a single host system.
ms.assetid: ed5d9bba-faad-40a6-8f08-258a94272a11
title: Msvm_Synthetic3DServiceSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Synthetic3DServiceSettingData
- Msvm_Synthetic3DServiceSettingData.InstanceID
- Msvm_Synthetic3DServiceSettingData.Caption
- Msvm_Synthetic3DServiceSettingData.Description
- Msvm_Synthetic3DServiceSettingData.ElementName
- Msvm_Synthetic3DServiceSettingData.GPUOvercommitEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_Synthetic3DServiceSettingData class

Represents the settings for the synthetic 3-D service present on a single host system. The properties for this class cannot be modified directly. The client must call the [**Msvm\_Synthetic3DService.ModifyServiceSettings**](modifyservicesettings-msvm-synthetic3dservice.md) method to modify any of these properties.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_Synthetic3DServiceSettingData : CIM_SettingData
{
  string  InstanceID;
  string  Caption = "Synthetic3D Service Settings";
  string  Description = "Configuration Settings for Synthetic3D Service.";
  string  ElementName = "Synthetic3D Service Settings";
  boolean GPUOvercommitEnabled = FALSE;
};
```

## Members

The **Msvm\_Synthetic3DServiceSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_Synthetic3DServiceSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**GPUOvercommitEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Controls whether virtual machine assignment takes GPU memory limitations into account.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

