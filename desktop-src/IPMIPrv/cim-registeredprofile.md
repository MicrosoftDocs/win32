---
title: CIM\_RegisteredProfile class
description: Describes a set of CIM Schema classes with required properties and/or methods, necessary to manage a real-world entity or to support a usage scenario, in an interoperable fashion.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2bec874d-eb36-4f21-a19a-74eec2b19ea1
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_RegisteredProfile class
- CIM_RegisteredProfile class, described
topic_type:
- apiref
api_name:
- CIM_RegisteredProfile
- CIM_RegisteredProfile.Caption
- CIM_RegisteredProfile.Description
- CIM_RegisteredProfile.ElementName
- CIM_RegisteredProfile.InstanceID
- CIM_RegisteredProfile.RegisteredOrganization
- CIM_RegisteredProfile.OtherRegisteredOrganization
- CIM_RegisteredProfile.RegisteredName
- CIM_RegisteredProfile.RegisteredVersion
- CIM_RegisteredProfile.AdvertiseTypes
- CIM_RegisteredProfile.AdvertiseTypeDescriptions
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_RegisteredProfile class

Describes a set of CIM Schema classes with required properties and/or methods, necessary to manage a real-world entity or to support a usage scenario, in an interoperable fashion.

Registered profiles can be defined by the DMTF or other standards organizations. A registered profile is a named 'standard' for CIM-based management of a particular System, subsystem, Service or other entity.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), AMENDMENT]
class CIM_RegisteredProfile : CIM_ManagedElement
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

The **CIM\_RegisteredProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RegisteredProfile** class has these properties.

<dl> <dt>

**AdvertiseTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.AdvertiseTypes")
</dt> </dl>

Additional information related to the **AdvertiseTypes** property. An entry in this array corresponds to the entry in the **AdvertiseTypes** array at the same index.

A description must be provided when the **AdvertiseTypes** entry is **Other** (1). Additional descriptions are probably not needed if the entry is set to **Not Advertised** or **SLP**, but may be appropriate in the future.

</dd> <dt>

**AdvertiseTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.AdvertiseTypeDescriptions")
</dt> </dl>

The advertisement for the profile information. It is used by the advertising services of the WBEM infrastructure to determine what should be advertised, via what mechanisms. The profile may be advertised using several mechanisms.

If this property is NULL or uninitialized, it is equivalent to **Not Advertised** (2).

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

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

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

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following format:

&lt;*OrgID*&gt;:&lt;*LocalID*&gt;

&lt;*OrgID*&gt; must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating the **InstanceID**, or is a registered ID that is assigned to the business entity by a recognized global authority. &lt;OrgID&gt; must not contain a colon (":"). The first colon to appear in **InstanceID** must be between &lt;*OrgID*&gt; and &lt;*LocalID*&gt;.

&lt;*LocalID*&gt; is chosen by the business entity and should not be re-used to identify different underlying elements.

If the above format is not used, the defining entity must assure that the resultant **InstanceID** is not re-used by this or other providers for this instance's NameSpace.

For DMTF defined instances, the format must have &lt;*OrgID*&gt; set to "CIM".

</dd> <dt>

**OtherRegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.RegisteredOrganization")
</dt> </dl>

When **RegisteredOrganization** is **Other** (1), a description of the organization.

</dd> <dt>

**RegisteredName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of this registered profile. The combination of **RegisteredName**, **RegisteredOrganization**, and **RegisteredVersion** must uniquely identify the registered profile within the scope of the organization.

</dd> <dt>

**RegisteredOrganization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RegisteredProfile.OtherRegisteredOrganization")
</dt> </dl>

The organization that defines this profile

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

The version of this profile. The version must be in the form, &lt;*major version number*&gt;.&lt;*minor version number*&gt;.&lt;*update*&gt;.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





