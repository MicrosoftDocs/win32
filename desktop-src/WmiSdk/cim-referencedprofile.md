---
description: Used to associate an instance CIM\_RegisteredProfile with an instance of CIM\_RegisteredProfile of another profile that references the dependent profile as a related profile.
ms.assetid: 631003de-477b-4447-9633-1601a7f8eadb
ms.tgt_platform: multiple
title: CIM_ReferencedProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ReferencedProfile
- CIM_ReferencedProfile.Antecedent
- CIM_ReferencedProfile.Dependent
api_type: 
- Schema
api_location: 
- Root\interop
---

# CIM\_ReferencedProfile class

Used to associate an instance [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) with an instance of **CIM\_RegisteredProfile** of another profile that references the dependent profile as a related profile.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Association, Version("2.8.0"), UMLPackagePath("CIM::Interop"), AMENDMENT]
class CIM_ReferencedProfile : CIM_Dependency
{
  CIM_RegisteredProfile REF Antecedent;
  CIM_RegisteredProfile REF Dependent;
};
```

## Members

The **CIM\_ReferencedProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ReferencedProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) instance that is referenced by the **Dependent** profile.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) instance that references other profiles.

</dd> </dl>

## Remarks

The use of the **Dependent** and **Antecedent** properties in the **CIM\_ReferencedProfile** association is defined such that the profile being referenced is the antecedent and the profile doing the referencing is the dependent.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\interop<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Interop.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency)
</dt> </dl>

 

