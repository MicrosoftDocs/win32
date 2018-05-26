---
title: CIM\_ManagedElement class
description: ManagedElement is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bd711f5d-1d07-48d5-bc73-d1642887cff9
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ManagedElement class
- CIM_ManagedElement class, described
topic_type:
- apiref
api_name:
- CIM_ManagedElement
- CIM_ManagedElement.Caption
- CIM_ManagedElement.Description
- CIM_ManagedElement.ElementName
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ManagedElement class

ManagedElement is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.7.0"), UUID("{d62c5793-c0eb-400e-a97b-2db5df757b8c}"), AMENDMENT]
class CIM_ManagedElement
{
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **CIM\_ManagedElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ManagedElement** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name IN ADDITION TO its key properties/identity data, and description information.

Note that ManagedSystemElement's Name property is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information MAY be present in both the Name and ElementName properties.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



 

 





