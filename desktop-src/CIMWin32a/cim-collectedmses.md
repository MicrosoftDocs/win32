---
title: CIM\_CollectedMSEs class
description: CIM\_CollectedMSEs is a generic association used to establish the members of the grouping object, CIM\_CollectionOfMSEs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fda6707b-b4dd-4152-9e3f-578a9f6b8c9c'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_CollectedMSEs class", "CIM_CollectedMSEs class, described"]
topic_type:
- apiref
api_name:
- CIM_CollectedMSEs
- CIM_CollectedMSEs.Collection
- CIM_CollectedMSEs.Member
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# CIM\_CollectedMSEs class

**CIM\_CollectedMSEs** is a generic association used to establish the members of the grouping object, [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Aggregation, AMENDMENT]
class CIM_CollectedMSEs
{
  CIM_CollectionOfMSEs     REF Collection;
  CIM_ManagedSystemElement REF Member;
};
```

## Members

The **CIM\_CollectedMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectedMSEs** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) containing the grouping or 'bag' object that represents the collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) representing the members of the collection.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



 

 





