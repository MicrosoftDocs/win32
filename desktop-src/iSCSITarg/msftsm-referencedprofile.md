---
title: MSFTSM\_ReferencedProfile class
description: Associates two instances of MSFTSM\_RegisteredProfile where one of the registered profiles references the other.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 336adfd9-57cd-40a0-b04c-7f18dc4a1f28
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_ReferencedProfile class iSCSI Software Target API
- MSFTSM_ReferencedProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_ReferencedProfile
- MSFTSM_ReferencedProfile.Antecedent
- MSFTSM_ReferencedProfile.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFTSM\_ReferencedProfile class

Associates two instances of [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) where one of the registered profiles references the other.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), provider("MSiSCSITargetProv")]
class MSFTSM_ReferencedProfile : CIM_ReferencedProfile
{
  CIM_RegisteredProfile REF Antecedent;
  CIM_RegisteredProfile REF Dependent;
};
```

## Members

The **MSFTSM\_ReferencedProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_ReferencedProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) instance that is referenced by the **Dependent** profile.

This property is inherited from [**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) instance that references other profiles.

This property is inherited from [**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374).

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

[**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





