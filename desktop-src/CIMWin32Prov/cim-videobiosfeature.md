---
description: The CIM\_VideoBIOSFeature class represents the capabilities of the low-level software used to configure and access a computer system's video controller and display.
ms.assetid: a12ca387-5b12-487f-84fd-381afe266338
ms.tgt_platform: multiple
title: CIM_VideoBIOSFeature class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VideoBIOSFeature
- CIM_VideoBIOSFeature.Caption
- CIM_VideoBIOSFeature.CharacteristicDescriptions
- CIM_VideoBIOSFeature.Characteristics
- CIM_VideoBIOSFeature.Description
- CIM_VideoBIOSFeature.IdentifyingNumber
- CIM_VideoBIOSFeature.InstallDate
- CIM_VideoBIOSFeature.Name
- CIM_VideoBIOSFeature.ProductName
- CIM_VideoBIOSFeature.Status
- CIM_VideoBIOSFeature.Vendor
- CIM_VideoBIOSFeature.Version
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_VideoBIOSFeature class

The **CIM\_VideoBIOSFeature** class represents the capabilities of the low-level software used to configure and access a computer system's video controller and display.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{BAE20634-E3D4-11d2-8601-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_VideoBIOSFeature : CIM_SoftwareFeature
{
  string   Caption;
  string   CharacteristicDescriptions[];
  uint16   Characteristics[];
  string   Description;
  string   IdentifyingNumber;
  datetime InstallDate;
  string   Name;
  string   ProductName;
  string   Status;
  string   Vendor;
  string   Version;
};
```

## Members

The **CIM\_VideoBIOSFeature** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VideoBIOSFeature** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CharacteristicDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Video BIOS Characteristic\|001.4"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VideoBIOSFeature**.**Characteristics**")
</dt> </dl>

Free-form strings that provide detailed descriptions for the video BIOS features indicated in the **Characteristics** array.

> [!Note]  
> Each entry of this array is related to the entry in the **Characteristics** array that is located at the same index.

 

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Video BIOS Characteristic\|001.3"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VideoBIOSFeature**.**CharacteristicDescriptions**")
</dt> </dl>

Features supported by the video BIOS. For example, support for VESA power management or video BIOS shadowing could be indicated. The value 3 ("Unknown") is not valid in the CIM schema since it represents that no BIOS features are supported in DMI. In which case, the object should not be instantiated.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (3)


</dt> <dd></dd> <dt>

<span id="Standard_Video_BIOS"></span><span id="standard_video_bios"></span><span id="STANDARD_VIDEO_BIOS"></span>

**Standard Video BIOS** (4)


</dt> <dd></dd> <dt>

<span id="VESA_BIOS_Extensions_Supported"></span><span id="vesa_bios_extensions_supported"></span><span id="VESA_BIOS_EXTENSIONS_SUPPORTED"></span>

**VESA BIOS Extensions Supported** (5)


</dt> <dd></dd> <dt>

<span id="VESA_Power_Management_Supported"></span><span id="vesa_power_management_supported"></span><span id="VESA_POWER_MANAGEMENT_SUPPORTED"></span>

**VESA Power Management Supported** (6)


</dt> <dd></dd> <dt>

<span id="VESA_Display_Data_Channel_Supported"></span><span id="vesa_display_data_channel_supported"></span><span id="VESA_DISPLAY_DATA_CHANNEL_SUPPORTED"></span>

**VESA Display Data Channel Supported** (7)


</dt> <dd></dd> <dt>

<span id="Video_BIOS_Shadowing_Allowed"></span><span id="video_bios_shadowing_allowed"></span><span id="VIDEO_BIOS_SHADOWING_ALLOWED"></span>

**Video BIOS Shadowing Allowed** (8)


</dt> <dd></dd> <dt>

<span id="Video_BIOS_Upgradeable"></span><span id="video_bios_upgradeable"></span><span id="VIDEO_BIOS_UPGRADEABLE"></span>

**Video BIOS Upgradeable** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IdentifyingNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Product**](cim-product.md).**IdentifyingNumber**"), [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("DMTF\|ComponentID\|001.4")
</dt> </dl>

Product identification, such as a serial number on software or a die number on a hardware chip. This property is inherited from [**CIM\_SoftwareFeature**](cim-softwarefeature.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Label by which the object is known outside of the data processing system. This label is a name that uniquely identifies the element in the context of the element's namespace.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Product**](cim-product.md).**Name**"), [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("DMTF\|ComponentID\|001.2")
</dt> </dl>

Commonly used product name.

This property is inherited from [**CIM\_SoftwareFeature**](cim-softwarefeature.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**Vendor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Product**](cim-product.md).**Vendor**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("DMTF\|ComponentID\|001.1")
</dt> </dl>

Name of the product's supplier, which corresponds to the **Vendor** property in the product object of the DMTF Solution Exchange Standard (SES).

This property is inherited from [**CIM\_SoftwareFeature**](cim-softwarefeature.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Product**](cim-product.md).**Version**"), [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("DMTF\|ComponentID\|001.3")
</dt> </dl>

Product version information, which corresponds to the **Version** property in the product object of the DMTF SES.

This property is inherited from [**CIM\_SoftwareFeature**](cim-softwarefeature.md).

</dd> </dl>

## Remarks

The **CIM\_VideoBIOSFeature** class is derived from [**CIM\_SoftwareFeature**](cim-softwarefeature.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SoftwareFeature**](cim-softwarefeature.md)
</dt> </dl>

 

