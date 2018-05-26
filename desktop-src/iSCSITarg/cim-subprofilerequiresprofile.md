---
title: CIM\_SubProfileRequiresProfile class
description: A subprofile requires another RegisteredProfile for context. This association mandates the scoping relationship between a subprofile and its scoping profile.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 923628aa-cbb7-48eb-9bad-10ce4892036d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SubProfileRequiresProfile class iSCSI Software Target API
- CIM_SubProfileRequiresProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_SubProfileRequiresProfile
- CIM_SubProfileRequiresProfile.Antecedent
- CIM_SubProfileRequiresProfile.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SubProfileRequiresProfile class

A subprofile requires another RegisteredProfile for context. This association mandates the scoping relationship between a subprofile and its scoping profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.8.0"), UMLPackagePath("CIM::Interop")]
class CIM_SubProfileRequiresProfile : CIM_ReferencedProfile
{
  CIM_RegisteredProfile    REF Antecedent;
  CIM_RegisteredSubProfile REF Dependent;
};
```

## Members

The **CIM\_SubProfileRequiresProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SubProfileRequiresProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The RegisteredProfile that is referenced/required by the subprofile.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredSubProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A RegisteredSubProfile that requires a scoping profile, for context.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





