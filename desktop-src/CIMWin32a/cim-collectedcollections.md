---
title: CIM\_CollectedCollections class
description: CIM\_CollectedCollections is an aggregation association representing that a CollectionOfMSEs may itself be contained in a collection of SMEs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fd157558-2272-4d60-bdd6-0c3ee5f7cb28'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_CollectedCollections class", "CIM_CollectedCollections class, described"]
topic_type:
- apiref
api_name:
- CIM_CollectedCollections
- CIM_CollectedCollections.Collection
- CIM_CollectedCollections.CollectionInCollection
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# CIM\_CollectedCollections class

**CIM\_CollectedCollections** is an aggregation association representing that a [**CollectionOfMSEs**](cim-collectionofmses.md) may itself be contained in a collection of SMEs.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Aggregation, AMENDMENT]
class CIM_CollectedCollections
{
  CIM_CollectionOfMSEs REF Collection;
  CIM_CollectionOfMSEs REF CollectionInCollection;
};
```

## Members

The **CIM\_CollectedCollections** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectedCollections** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

A reference to a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) containing the 'higher level' or parent element in the aggregation.

</dd> <dt>

**CollectionInCollection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

A reference to a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) containing the 'collected' collection.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



 

 





