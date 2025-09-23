---
title: CIM\_Component class
description: CIM\_Component is a generic association used to establish \\'part of\\' relationships between Managed Elements. For example, it could be used to define the components or parts of a System.
ms.assetid: 44b82c0d-acf8-471c-91c4-4180a7705ac3
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
- NetEventPacketCapture.dll
api_type:
- DllExport


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# CIM\_Component class

CIM\_Component is a generic association used to establish \\'part of\\' relationships between Managed Elements. For example, it could be used to define the components or parts of a System.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, UMLPackagePath("CIM::Core::CoreElements"), Version("2.7.0"), AMENDMENT]
class CIM_Component
{
  CIM_ManagedElement REF GroupComponent;
  CIM_ManagedElement REF PartComponent;
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

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Aggregate**](/windows/win32/wmisdk/standard-qualifiers)
</dt> </dl>

The parent element in the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

The child element in the association.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                                       |
| MOF<br/>                      | <dl> <dt>NetEventPacketCapture.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetEventPacketCapture.dll</dt> </dl> |



 

