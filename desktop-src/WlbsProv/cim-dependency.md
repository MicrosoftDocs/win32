---
title: CIM\_Dependency class
description: A generic association to establish dependency relationships between objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ad3aa6fe-f25a-4531-b300-53fbcc23d8be'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_Dependency class", "CIM_Dependency class, described"]
topic_type:
- apiref
api_name:
- CIM_Dependency
- CIM_Dependency.Antecedent
- CIM_Dependency.Dependent
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_Dependency class

A generic association to establish dependency relationships between objects

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, AMENDMENT]
class CIM_Dependency
{
  CIM_ManagedSystemElement REF Antecedent;
  CIM_ManagedSystemElement REF Dependent;
};
```

## Members

The **CIM\_Dependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Dependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antecedent represents the independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Dependent represents the object dependent on the Antecedent.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





