---
title: CIM\_ElementConformsToProfile class
description: Defines the RegisteredProfiles to which the referenced ManagedElement is conformant.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '748272ca-bfd2-490c-a7cd-77580a5db641'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ElementConformsToProfile class iSCSI Software Target API", "CIM_ElementConformsToProfile class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_ElementConformsToProfile
- CIM_ElementConformsToProfile.ConformantStandard
- CIM_ElementConformsToProfile.ManagedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_ElementConformsToProfile class

Defines the RegisteredProfiles to which the referenced ManagedElement is conformant.

This association may apply to any Managed Element. Typical usage will apply it to a higher level instance, such as a System, NameSpace, or Service. When applied to a higher level instance, all constituent parts MUST behave appropriately in support of the ManagedElement's conformance to the named RegisteredProfile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Interop")]
class CIM_ElementConformsToProfile
{
  CIM_RegisteredProfile REF ConformantStandard;
  CIM_ManagedElement    REF ManagedElement;
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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) to which the Managed Element conforms.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) that conforms to the Registered Profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





