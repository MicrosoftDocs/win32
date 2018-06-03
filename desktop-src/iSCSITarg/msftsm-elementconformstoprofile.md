---
title: MSFTSM\_ElementConformsToProfile class
description: This association indicates that the specified CIM\_ManagedElement instance, which includes all constituent elements, conforms to the specified MSFTSM\_RegisteredProfile instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cded0f44-c7f5-4131-9bb4-699b2d1d97e4
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_ElementConformsToProfile class iSCSI Software Target API
- MSFTSM_ElementConformsToProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_ElementConformsToProfile
- MSFTSM_ElementConformsToProfile.ConformantStandard
- MSFTSM_ElementConformsToProfile.ManagedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFTSM\_ElementConformsToProfile class

This association indicates that the specified [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) instance, which includes all constituent elements, conforms to the specified [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) instance. This association is typically applied to a higher-level instance, such as a **CIM\_System**, **CIM\_NameSpace**, or **CIM\_Service** instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), provider("MSiSCSITargetProv")]
class MSFTSM_ElementConformsToProfile : CIM_ElementConformsToProfile
{
  CIM_RegisteredProfile REF ConformantStandard;
  CIM_ManagedElement    REF ManagedElement;
};
```

## Members

The **MSFTSM\_ElementConformsToProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_ElementConformsToProfile** class has these properties.

<dl> <dt>

**ConformantStandard**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (ConformantStandard)
</dt> </dl>

Indicates the registered profile to which the managed element conforms.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (ManagedElement), **MSFT\_TargetNamespace** ("root\\\\cimv2\\\\storage\\\\iscsitarget")
</dt> </dl>

Indicates the managed element that conforms to the registered profile

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\Interop<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementConformsToProfile**](https://msdn.microsoft.com/library/mt446049)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





