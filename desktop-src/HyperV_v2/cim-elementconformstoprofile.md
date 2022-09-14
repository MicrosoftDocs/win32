---
description: Represents an association in which a managed element conforms to the standard of a registered profile.
ms.assetid: 9d5704b6-c764-4f68-bce3-384d5a244e28
title: CIM_ElementConformsToProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ElementConformsToProfile
- CIM_ElementConformsToProfile.ConformantStandard
- CIM_ElementConformsToProfile.ManagedElement
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ElementConformsToProfile class

Represents an association in which a managed element conforms to the standard of a registered profile. This association usually applies to a higher level instance, such as a system, namespace, or service. When applied to a higher level instance, all constituent parts MUST behave appropriately in support of the ManagedElement's conformance to the named RegisteredProfile.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Interop")]
class CIM_ElementConformsToProfile
{
  CIM_RegisteredProfile REF ConformantStandard;
  CIM_ManagedElement    REF ManagedElement;
};
```

## Members

The **CIM\_ElementConformsToProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementConformsToProfile** class has these properties.

<dl> <dt>

**ConformantStandard**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The registered profile to which the managed element conforms.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The managed element that conforms to the registered profile.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

