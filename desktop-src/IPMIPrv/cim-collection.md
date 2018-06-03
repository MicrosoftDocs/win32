---
title: CIM\_Collection class
description: The common superclass for data elements that represent collections of ManagedElements and its subclasses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77c9cb9e-7efc-47d4-a2eb-7bafe94a7b13
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Collection class
- CIM_Collection class, described
topic_type:
- apiref
api_name:
- CIM_Collection
- CIM_Collection.Caption
- CIM_Collection.Description
- CIM_Collection.ElementName
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_Collection class

The common superclass for data elements that represent collections of ManagedElements and its subclasses.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), UUID("{07136e6c-c254-436d-a200-1404e98881b6}"), AMENDMENT]
class CIM_Collection : CIM_ManagedElement
{
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **CIM\_Collection** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Collection** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





