---
title: CIM\_Component class
description: A generic association used to establish part of relationships between Managed System Elements. For example, the SystemComponent association defines parts of a System.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8bd8639-fa1c-4f54-85e0-13fea984a0d0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Component class
- CIM_Component class, described
topic_type:
- apiref
api_name:
- CIM_Component
- CIM_Component.GroupComponent
- CIM_Component.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Component class

A generic association used to establish 'part of' relationships between Managed System Elements. For example, the SystemComponent association defines parts of a System.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, UUID("{7C6B02AF-B639-4ca5-9A92-E5710AB090AC}"), AMENDMENT]
class CIM_Component
{
  CIM_ManagedSystemElement REF GroupComponent;
  CIM_ManagedSystemElement REF PartComponent;
};
```

## Members

The **CIM\_Component** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Component** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The parent element in the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The child element in the association.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





