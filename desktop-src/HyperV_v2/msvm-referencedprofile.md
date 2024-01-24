---
description: Describes a profile that is referenced by another registered profile.
ms.assetid: 36FC0161-C57F-488A-9B4A-C86C6EB481D7
title: Msvm_ReferencedProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReferencedProfile
- Msvm_ReferencedProfile.Antecedent
- Msvm_ReferencedProfile.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ReferencedProfile class

Describes a profile that is referenced by another registered profile.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
class Msvm_ReferencedProfile : CIM_ReferencedProfile
{
  CIM_RegisteredProfile REF Antecedent;
  CIM_RegisteredProfile REF Dependent;
};
```

## Members

The **Msvm\_ReferencedProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReferencedProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The registered profile that is referenced by the **Dependent** profile.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A registered profile that references other profiles.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\interop<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

