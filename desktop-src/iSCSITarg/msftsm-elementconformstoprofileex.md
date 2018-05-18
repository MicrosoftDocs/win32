---
title: MSFTSM\_ElementConformsToProfileEx class
description: This association indicates that the specified CIM\_ManagedElement instance, which includes all constituent elements, conforms to the specified MSFTSM\_RegisteredProfile instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '73cb783b-b77a-44f8-9e35-359b6d9e0fbe'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_ElementConformsToProfileEx class iSCSI Software Target API", "MSFTSM_ElementConformsToProfileEx class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_ElementConformsToProfileEx
- MSFTSM_ElementConformsToProfileEx.ConformantStandard
- MSFTSM_ElementConformsToProfileEx.ManagedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_ElementConformsToProfileEx class

This association indicates that the specified [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) instance, which includes all constituent elements, conforms to the specified [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) instance. This association is typically applied to a higher-level instance, such as a **CIM\_System**, **CIM\_NameSpace**, or **CIM\_Service** instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), provider("MSiSCSITargetProv")]
class MSFTSM_ElementConformsToProfileEx : CIM_ElementConformsToProfile
{
  CIM_RegisteredProfile REF ConformantStandard;
  CIM_ManagedElement    REF ManagedElement;
};
```

## Members

The **MSFTSM\_ElementConformsToProfileEx** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_ElementConformsToProfileEx** class has these properties.

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

This property is inherited from [**CIM\_ElementConformsToProfile**](cim-elementconformstoprofile.md).

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

This property is inherited from [**CIM\_ElementConformsToProfile**](cim-elementconformstoprofile.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementConformsToProfile**](https://msdn.microsoft.com/library/mt446049)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





