---
title: CIM\_SystemComponent class
description: CIM\_SystemComponent is a specialization of the CIM\_Component association that establishes part of relationships between a System and the Managed System Elements of which it is composed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 98609ad2-fee9-4b37-aaf8-502c9c4c24ab
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SystemComponent class
- CIM_SystemComponent class, described
topic_type:
- apiref
api_name:
- CIM_SystemComponent
- CIM_SystemComponent.GroupComponent
- CIM_SystemComponent.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SystemComponent class

CIM\_SystemComponent is a specialization of the CIM\_Component association that establishes 'part of' relationships between a System and the Managed System Elements of which it is composed.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, UUID("{D4DF8D45-2057-4f5f-AAF0-BC4452F48F1F}"), AMENDMENT]
class CIM_SystemComponent : CIM_Component
{
  CIM_System               REF GroupComponent;
  CIM_ManagedSystemElement REF PartComponent;
};
```

## Members

The **CIM\_SystemComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The parent System in the Association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The child element that is a component of a System.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





