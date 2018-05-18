---
title: CIM\_CollectionSetting class
description: CollectionSetting represents the association between a CollectionOfMSEs class and the Setting class(es) defined for them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a45dd0f-7ffd-4ab2-be1a-f5f1ba9d0da8'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_CollectionSetting class", "CIM_CollectionSetting class, described"]
topic_type:
- apiref
api_name:
- CIM_CollectionSetting
- CIM_CollectionSetting.Collection
- CIM_CollectionSetting.Setting
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# CIM\_CollectionSetting class

**CollectionSetting** represents the association between a [**CollectionOfMSEs**](cim-collectionofmses.md) class and the Setting class(es) defined for them.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, AMENDMENT]
class CIM_CollectionSetting
{
  CIM_CollectionOfMSEs REF Collection;
  CIM_Setting          REF Setting;
};
```

## Members

The **CIM\_CollectionSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionSetting** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

A [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) referencing the collection of SMEs.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

A [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) containing the Setting object associated with the collection.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



 

 





