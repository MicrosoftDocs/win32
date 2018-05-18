---
title: CIM\_HostedService class
description: CIM\_HostedService is an association between a service and the system on which the functionality resides.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c7462487-bc15-4a87-98d4-2362a2a9e382'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedService class", "CIM_HostedService class, described"]
topic_type:
- apiref
api_name:
- CIM_HostedService
- CIM_HostedService.Antecedent
- CIM_HostedService.Dependent
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_HostedService class

CIM\_HostedService is an association between a service and the system on which the functionality resides. The cardinality of this association is 1-to-many. A system may host many services. services are weak with respect to their hosting system. Heuristic: A service is hosted on the system where the logical devices or software features that implement the service are located. The model does not represent services hosted across multiple systems. This is modeled as an application system that acts as an aggregation point for services, that are each located on a single host.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class CIM_HostedService : CIM_Dependency
{
  CIM_System  REF Antecedent;
  CIM_Service REF Dependent;
};
```

## Members

The **CIM\_HostedService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The hosting system

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The service hosted on the system

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





