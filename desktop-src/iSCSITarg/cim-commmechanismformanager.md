---
title: CIM\_CommMechanismForManager class
description: An association between an ObjectManager and an ObjectManagerCommunicationMechanism class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '048c7988-6bc0-4993-8865-e01b3563d590'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_CommMechanismForManager class iSCSI Software Target API", "CIM_CommMechanismForManager class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_CommMechanismForManager
- CIM_CommMechanismForManager.Antecedent
- CIM_CommMechanismForManager.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_CommMechanismForManager class

An association between an ObjectManager and an ObjectManagerCommunicationMechanism class. The latter describes a possible encoding/protocol/ set of operations for accessing the referenced ObjectManager.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Interop")]
class CIM_CommMechanismForManager : CIM_ServiceAccessBySAP
{
  CIM_ObjectManager                       REF Antecedent;
  CIM_ObjectManagerCommunicationMechanism REF Dependent;
};
```

## Members

The **CIM\_CommMechanismForManager** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CommMechanismForManager** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManager**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The specific ObjectManager whose communication mechanism is described.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManagerCommunicationMechanism**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The encoding/protocol/set of operations that may be used to communicate with the referenced ObjectManager.

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

[**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md)
</dt> </dl>

 

 





