---
title: RegisteredProfile class
description: Represents a registered profile, which manages use cases for a system or service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9D8852F1-FD0F-4507-A451-30F0D7D3090A'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RegisteredProfile class", "RegisteredProfile class, described"]
topic_type:
- apiref
api_name:
- RegisteredProfile
- RegisteredProfile.Caption
- RegisteredProfile.Description
- RegisteredProfile.ElementName
- RegisteredProfile.InstanceID
- RegisteredProfile.RegisteredOrganization
- RegisteredProfile.OtherRegisteredOrganization
- RegisteredProfile.RegisteredName
- RegisteredProfile.RegisteredVersion
- RegisteredProfile.AdvertiseTypes
- RegisteredProfile.AdvertiseTypeDescriptions
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# RegisteredProfile class

Represents a registered profile, which manages use cases for a system or service.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("IPMIPrv"), AMENDMENT]
class RegisteredProfile : CIM_RegisteredProfile
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  uint16 RegisteredOrganization;
  string OtherRegisteredOrganization;
  string RegisteredName;
  string RegisteredVersion;
  uint16 AdvertiseTypes[];
  string AdvertiseTypeDescriptions[];
};
```

## Members

The **RegisteredProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **RegisteredProfile** class has these properties.

<dl> <dt>

**AdvertiseTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.AdvertiseTypes")
</dt> </dl>

A free-form string providing additional information related to the AdvertiseType. A description MUST be provided when the AdvertiseType is 1, "Other". An entry in this array corresponds to the entry in the AdvertiseTypes array at the same index. It is not expected that additional descriptions are needed if the Type is set to "Not Advertised" or "SLP". However, as the SLP template expands, or as other advertisement mechanisms are defined, support for additional descriptions may be needed. This array is defined to support this.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

</dd> <dt>

**AdvertiseTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.AdvertiseTypeDescriptions")
</dt> </dl>

This property signifies the advertisement for the profile information. It is used by the advertising services of the WBEM infrastructure to determine what should be advertised, via what mechanisms. The property is an array so that the profile MAY be advertised using several mechanisms. Note: If this property is null/uninitialized, this is equivalent to specifying the value 2, "Not Advertised".

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Advertised"></span><span id="not_advertised"></span><span id="NOT_ADVERTISED"></span>

**Not Advertised** (2)


</dt> <dd></dd> <dt>

<span id="SLP"></span><span id="slp"></span>

**SLP** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name IN ADDITION TO its key properties/identity data, and description information.

Note that ManagedSystemElement's Name property is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information MAY be present in both the Name and ElementName properties.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the organizational entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace.

For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

</dd> <dt>

**OtherRegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.RegisteredOrganization")
</dt> </dl>

A free-form string providing a description of the organization when 1, "Other", is specified for the RegisteredOrganization.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

</dd> <dt>

**RegisteredName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of this registered profile. Since multiple versions can exist for the same RegisteredName, the combination of RegisteredName, RegisteredOrganization, and RegisteredVersion MUST uniquely identify the registered profile within the scope of the organization.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

</dd> <dt>

**RegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.OtherRegisteredOrganization")
</dt> </dl>

The organization that defines this profile.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="DMTF"></span><span id="dmtf"></span>

**DMTF** (2)


</dt> <dd></dd> <dt>

<span id="CompTIA"></span><span id="comptia"></span><span id="COMPTIA"></span>

**CompTIA** (3)


</dt> <dd></dd> <dt>

<span id="Consortium_for_Service_Innovation"></span><span id="consortium_for_service_innovation"></span><span id="CONSORTIUM_FOR_SERVICE_INNOVATION"></span>

**Consortium for Service Innovation** (4)


</dt> <dd></dd> <dt>

<span id="FAST"></span><span id="fast"></span>

**FAST** (5)


</dt> <dd></dd> <dt>

<span id="GGF"></span><span id="ggf"></span>

**GGF** (6)


</dt> <dd></dd> <dt>

<span id="INTAP"></span><span id="intap"></span>

**INTAP** (7)


</dt> <dd></dd> <dt>

<span id="itSMF"></span><span id="itsmf"></span><span id="ITSMF"></span>

**itSMF** (8)


</dt> <dd></dd> <dt>

<span id="NAC"></span><span id="nac"></span>

**NAC** (9)


</dt> <dd></dd> <dt>

<span id="Northwest_Energy_Efficiency_Alliance"></span><span id="northwest_energy_efficiency_alliance"></span><span id="NORTHWEST_ENERGY_EFFICIENCY_ALLIANCE"></span>

**Northwest Energy Efficiency Alliance** (10)


</dt> <dd></dd> <dt>

<span id="SNIA"></span><span id="snia"></span>

**SNIA** (11)


</dt> <dd></dd> <dt>

<span id="TM_Forum"></span><span id="tm_forum"></span><span id="TM_FORUM"></span>

**TM Forum** (12)


</dt> <dd></dd> <dt>

<span id="The_Open_Group"></span><span id="the_open_group"></span><span id="THE_OPEN_GROUP"></span>

**The Open Group** (13)


</dt> <dd></dd> <dt>

<span id="ANSI"></span><span id="ansi"></span>

**ANSI** (14)


</dt> <dd></dd> <dt>

<span id="IEEE"></span><span id="ieee"></span>

**IEEE** (15)


</dt> <dd></dd> <dt>

<span id="IETF"></span><span id="ietf"></span>

**IETF** (16)


</dt> <dd></dd> <dt>

<span id="INCITS"></span><span id="incits"></span>

**INCITS** (17)


</dt> <dd></dd> <dt>

<span id="ISO"></span><span id="iso"></span>

**ISO** (18)


</dt> <dd></dd> <dt>

<span id="W3C"></span><span id="w3c"></span>

**W3C** (19)


</dt> <dd></dd> </dl>

</dd> <dt>

**RegisteredVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The version of this profile. The string representing the version MUST be in the form:

M + "." + N + "." + U

Where:

M - The major version (in numeric form) describing the profile's creation or last modification.

N - The minor version (in numeric form) describing the profile's creation or last modification.

U - The update (e.g. errata, patch, ..., in numeric form) describing the profile's creation or last modification.

This property is inherited from [**CIM\_RegisteredProfile**](cim-registeredprofile.md).

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_RegisteredProfile**](cim-registeredprofile.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





