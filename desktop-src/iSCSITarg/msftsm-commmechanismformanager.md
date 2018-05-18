---
title: MSFTSM\_CommMechanismForManager class
description: Associates an MSFTSM\_ObjectManager instance with an CIM\_ObjectManagerCommunicationMechanism instance, which describes a protocol and encoding that can be used to communicate with the object manager.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7aca9e9b-6213-4452-a07e-d4132d615e1c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_CommMechanismForManager class iSCSI Software Target API", "MSFTSM_CommMechanismForManager class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_CommMechanismForManager
- MSFTSM_CommMechanismForManager.Antecedent
- MSFTSM_CommMechanismForManager.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_CommMechanismForManager class

Associates an [**MSFTSM\_ObjectManager**](msftsm-objectmanager.md) instance with an **CIM\_ObjectManagerCommunicationMechanism** instance, which describes a protocol and encoding that can be used to communicate with the object manager.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), provider("MSiSCSITargetProv")]
class MSFTSM_CommMechanismForManager : CIM_CommMechanismForManager
{
  CIM_ObjectManager                       REF Antecedent;
  CIM_ObjectManagerCommunicationMechanism REF Dependent;
};
```

## Members

The **MSFTSM\_CommMechanismForManager** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_CommMechanismForManager** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManager**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The specific ObjectManager whose communication mechanism is described.

This property is inherited from [**CIM\_CommMechanismForManager**](cim-commmechanismformanager.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManagerCommunicationMechanism**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The encoding/protocol/set of operations that may be used to communicate with the referenced ObjectManager.

This property is inherited from [**CIM\_CommMechanismForManager**](cim-commmechanismformanager.md).

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

[**CIM\_CommMechanismForManager**](cim-commmechanismformanager.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





