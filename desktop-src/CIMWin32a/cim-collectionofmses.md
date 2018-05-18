---
title: CIM\_CollectionOfMSEs class
description: CollectionOfMSEs allows the grouping of CIM\_ManagedSystemElement objects for the purposes of associating settings and configurations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b9b9dafb-4718-4bee-8dc2-bb28d0f0e708'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_CollectionOfMSEs class", "CIM_CollectionOfMSEs class, described"]
topic_type:
- apiref
api_name:
- CIM_CollectionOfMSEs
- CIM_CollectionOfMSEs.CollectionID
- CIM_CollectionOfMSEs.Caption
- CIM_CollectionOfMSEs.Description
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# CIM\_CollectionOfMSEs class

**CollectionOfMSEs** allows the grouping of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) objects for the purposes of associating settings and configurations.

It is abstract to require further definition and semantic refinement in subclasses. The **CollectionOfMSEs** object does not carry any state or status information, but only represents a grouping or 'bag' of Elements. For this reason, it is incorrect to subclass groups that have state/status from CollectionOfMSEs - an example is CIM\_RedundancyGroup (which is correctly subclassed from LogicalElement).

Collections typically aggregate 'like' objects, and represent an optimization. Without Collections, one is forced to define individual ElementSetting and ElementConfiguration associations, to tie Settings and Configuration objects to individual ManagedSystemElements. There may be much duplication in assigning the same Setting to multiple objects. In addition, using the Collection object allows the determination that the Setting and Configuration associations are indeed the same for the Collection's members. This information would otherwise be obtained by defining the Collection in a proprietary manner, and then querying the ElementSetting and ElementConfiguration associations to determine if the Collection set is completely covered.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class CIM_CollectionOfMSEs
{
  string CollectionID;
  string Caption;
  string Description;
};
```

## Members

The **CIM\_CollectionOfMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionOfMSEs** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the current instance.

</dd> <dt>

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The identification of the collection object. When subclassed, **CollectionID** can be overridden to be a Key property.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the current instance.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



 

 





