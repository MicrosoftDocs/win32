---
title: CIM\_Component class
description: A generic association to establish part of relationships between managed system elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b21a1ef-b058-48de-b82e-bd29000f90f2
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
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
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Component class

A generic association to establish 'part of' relationships between managed system elements.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, AMENDMENT]
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

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The parent element in the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The child element in the association.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





