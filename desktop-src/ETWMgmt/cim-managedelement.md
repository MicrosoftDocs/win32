---
title: CIM\_ManagedElement class
description: The CIM\_ManagedElement class is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51f4f819-4dd4-4d4b-82f4-5c7f43a6d696
ms.prod: windows-server-dev
ms.technology:
- event-tracing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ManagedElement class
- CIM_ManagedElement class, described
topic_type:
- apiref
api_name:
- CIM_ManagedElement
- CIM_ManagedElement.InstanceID
- CIM_ManagedElement.Caption
- CIM_ManagedElement.Description
- CIM_ManagedElement.ElementName
api_location:
- EventTracingManagement.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_ManagedElement class

The **CIM\_ManagedElement** class is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, UMLPackagePath("CIM::Core::CoreElements"), Version("2.19.0"), AMENDMENT]
class CIM_ManagedElement
{
  string InstanceID;
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

A short one-line description of the object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace.

The value of this property must be unique within the NameSpace.

</dd> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\EventTracingManagement<br/>                                           |
| MOF<br/>                      | <dl> <dt>EventTracingManagement.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>EventTracingManagement.dll</dt> </dl> |



 

 





