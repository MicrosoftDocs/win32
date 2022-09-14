---
description: Represents the parameters to set the boot source of a virtual machine.
ms.assetid: 21CD4B71-3D05-469E-89BB-DC2C65F5AB10
title: Msvm_BootSourceSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_BootSourceSettingData
- Msvm_BootSourceSettingData.Description
- Msvm_BootSourceSettingData.Caption
- Msvm_BootSourceSettingData.InstanceID
- Msvm_BootSourceSettingData.ElementName
- Msvm_BootSourceSettingData.BootSourceType
- Msvm_BootSourceSettingData.OtherLocation
- Msvm_BootSourceSettingData.FirmwareDevicePath
- Msvm_BootSourceSettingData.BootSourceDescription
- Msvm_BootSourceSettingData.OptionalData
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_BootSourceSettingData class

Represents the parameters to set the boot source of a virtual machine. This class derives from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_BootSourceSettingData : CIM_SettingData
{
  string Description;
  string Caption;
  string InstanceID;
  string ElementName;
  uint32 BootSourceType;
  string OtherLocation;
  string FirmwareDevicePath;
  string BootSourceDescription;
  uint8  OptionalData[];
};
```

## Members

The **Msvm\_BootSourceSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_BootSourceSettingData** class has these properties.

<dl> <dt>

**BootSourceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the boot source provided by the firmware.

</dd> <dt>

**BootSourceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration value that specifies the type of the boot source.

These are valid values:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Drive"></span><span id="drive"></span><span id="DRIVE"></span>

**Drive** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> <dt>

<span id="File"></span><span id="file"></span><span id="FILE"></span>

**File** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

A short textual description of the object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The display name for this instance of SettingData. In addition, the display name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

</dd> <dt>

**FirmwareDevicePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The native path that the firmware uses to describe the device.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

</dd> <dt>

**OptionalData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **OctetString**, [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

Optional data provided by the firmware.

> [!Note]  
> Property added in Windows 10.

 

</dd> <dt>

**OtherLocation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The other location info, if any, that the firmware uses to further uniquely identify the boot source.

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85))
</dt> </dl>

 

