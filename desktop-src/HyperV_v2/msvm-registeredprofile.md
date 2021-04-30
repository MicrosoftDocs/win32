---
description: Describes a set of classes with required properties and methods, necessary to manage a real-world entity or to support a usage scenario, in an interoperable fashion.
ms.assetid: 75644856-3B47-43B8-835C-783A6BEE7251
title: Msvm_RegisteredProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_RegisteredProfile
- Msvm_RegisteredProfile.InstanceID
- Msvm_RegisteredProfile.Caption
- Msvm_RegisteredProfile.Description
- Msvm_RegisteredProfile.ElementName
- Msvm_RegisteredProfile.RegisteredOrganization
- Msvm_RegisteredProfile.OtherRegisteredOrganization
- Msvm_RegisteredProfile.RegisteredName
- Msvm_RegisteredProfile.RegisteredVersion
- Msvm_RegisteredProfile.AdvertiseTypes
- Msvm_RegisteredProfile.AdvertiseTypeDescriptions
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_RegisteredProfile class

Describes a set of classes with required properties and methods, necessary to manage a real-world entity or to support a usage scenario, in an interoperable fashion.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
class Msvm_RegisteredProfile : CIM_RegisteredProfile
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  uint16 RegisteredOrganization;
  string OtherRegisteredOrganization;
  string RegisteredName;
  string RegisteredVersion;
  uint16 AdvertiseTypes[];
  string AdvertiseTypeDescriptions[];
};
```

## Members

The **Msvm\_RegisteredProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_RegisteredProfile** class has these properties.

<dl> <dt>

**AdvertiseTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings that provides additional information related to the **AdvertiseType** property. A description must be provided when the **AdvertiseType** is 1 (Other). An entry in this array corresponds to the same index in the **AdvertiseTypes** array. This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

</dd> <dt>

**AdvertiseTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the advertisement for the profile information. It is used by the advertising services of the WBEM infrastructure to determine what should be advertised, through what mechanisms. The property is an array so that the profile can be advertised using several mechanisms. If this property is **Null**, this is equivalent to specifying the value 2 (Not Advertised). This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Not_Advertised"></span><span id="not_advertised"></span><span id="NOT_ADVERTISED"></span>**Not Advertised** (2)
</dt> <dt>

<span id="SLP_"></span><span id="slp_"></span>**SLP** (3 )
</dt> </dl>

</dd> <dt>

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

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

A string that uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**OtherRegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 256 )
</dt> </dl>

A string that provides a description of the organization when **RegisteredOrganization** contains 1 (Other). This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

</dd> <dt>

**RegisteredName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 256 )
</dt> </dl>

The name of this registered profile. Since multiple versions can exist for the same **RegisteredName**, the combination of **RegisteredName**, **RegisteredOrganization**, and **RegisteredVersion** must uniquely identify the registered profile within the scope of the organization. This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

</dd> <dt>

**RegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The organization that defines this profile. This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="DMTF"></span><span id="dmtf"></span>**DMTF** (2)
</dt> <dt>

<span id="CompTIA"></span><span id="comptia"></span><span id="COMPTIA"></span>**CompTIA** (3)
</dt> <dt>

<span id="Consortium_for_Service_Innovation"></span><span id="consortium_for_service_innovation"></span><span id="CONSORTIUM_FOR_SERVICE_INNOVATION"></span>**Consortium for Service Innovation** (4)
</dt> <dt>

<span id="FAST"></span><span id="fast"></span>**FAST** (5)
</dt> <dt>

<span id="GGF"></span><span id="ggf"></span>**GGF** (6)
</dt> <dt>

<span id="INTAP"></span><span id="intap"></span>**INTAP** (7)
</dt> <dt>

<span id="itSMF"></span><span id="itsmf"></span><span id="ITSMF"></span>**itSMF** (8)
</dt> <dt>

<span id="NAC"></span><span id="nac"></span>**NAC** (9)
</dt> <dt>

<span id="__10___________Northwest_Energy_Efficiency_Alliance"></span><span id="__10___________northwest_energy_efficiency_alliance"></span><span id="__10___________NORTHWEST_ENERGY_EFFICIENCY_ALLIANCE"></span>**//10 Northwest Energy Efficiency Alliance** (10)
</dt> <dt>

<span id="SNIA"></span><span id="snia"></span>**SNIA** (11)
</dt> <dt>

<span id="TM_Forum"></span><span id="tm_forum"></span><span id="TM_FORUM"></span>**TM Forum** (12)
</dt> <dt>

<span id="The_Open_Group"></span><span id="the_open_group"></span><span id="THE_OPEN_GROUP"></span>**The Open Group** (13)
</dt> <dt>

<span id="ANSI"></span><span id="ansi"></span>**ANSI** (14)
</dt> <dt>

<span id="IEEE"></span><span id="ieee"></span>**IEEE** (15)
</dt> <dt>

<span id="IETF"></span><span id="ietf"></span>**IETF** (16)
</dt> <dt>

<span id="INCITS"></span><span id="incits"></span>**INCITS** (17)
</dt> <dt>

<span id="ISO"></span><span id="iso"></span>**ISO** (18)
</dt> <dt>

<span id="W3C"></span><span id="w3c"></span>**W3C** (19)
</dt> <dt>

<span id="__20___________OGF"></span><span id="__20___________ogf"></span>**//20 OGF** (20)
</dt> <dt>

<span id="The_Green_Grid"></span><span id="the_green_grid"></span><span id="THE_GREEN_GRID"></span>**The Green Grid** (21)
</dt> <dt>

<span id="DMTF_Reserved_"></span><span id="dmtf_reserved_"></span><span id="DMTF_RESERVED_"></span>**DMTF Reserved** (.. )
</dt> </dl>

</dd> <dt>

**RegisteredVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of this profile. The string must be in the form: "*M*.*N*.*U*" Where:

-   *M* is the major version (in numeric form) describing the profile's creation or last modification.
-   *N* is the minor version (in numeric form) describing the profile's creation or last modification.
-   *U* is the update (in numeric form) describing the profile's creation or last modification.

This property is inherited from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\interop<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

