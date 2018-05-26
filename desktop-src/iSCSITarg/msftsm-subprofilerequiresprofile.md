---
title: MSFTSM\_SubProfileRequiresProfile class
description: Associates a MSFTSM\_RegisteredSubProfile instance with a MSFTSM\_RegisteredProfile instance that provides context for the subprofile.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: be2677c4-e65e-4ba6-a9a4-f75051d4f61b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_SubProfileRequiresProfile class iSCSI Software Target API
- MSFTSM_SubProfileRequiresProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_SubProfileRequiresProfile
- MSFTSM_SubProfileRequiresProfile.Antecedent
- MSFTSM_SubProfileRequiresProfile.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFTSM\_SubProfileRequiresProfile class

Associates a [**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md) instance with a [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) instance that provides context for the subprofile. This association is mandatory for [**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md) instances.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("2.8.0"), provider("MSiSCSITargetProv")]
class MSFTSM_SubProfileRequiresProfile : CIM_SubProfileRequiresProfile
{
  CIM_RegisteredProfile    REF Antecedent;
  CIM_RegisteredSubProfile REF Dependent;
};
```

## Members

The **MSFTSM\_SubProfileRequiresProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_SubProfileRequiresProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The RegisteredProfile that is referenced/required by the subprofile.

This property is inherited from [**CIM\_SubProfileRequiresProfile**](cim-subprofilerequiresprofile.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredSubProfile**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A RegisteredSubProfile that requires a scoping profile, for context.

This property is inherited from [**CIM\_SubProfileRequiresProfile**](cim-subprofilerequiresprofile.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\Interop<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





