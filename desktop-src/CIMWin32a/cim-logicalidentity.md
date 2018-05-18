---
title: CIM\_LogicalIdentity class
description: CIM\_LogicalIdentity is an abstract and generic association, indicating that two CIM\_LogicalElement objects represent different aspects of the same underlying entity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff10263f-6b60-47e1-a2ea-c505911f41a0'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_LogicalIdentity class", "CIM_LogicalIdentity class, described"]
topic_type:
- apiref
api_name:
- CIM_LogicalIdentity
- CIM_LogicalIdentity.SystemElement
- CIM_LogicalIdentity.SameElement
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# CIM\_LogicalIdentity class

**CIM\_LogicalIdentity** is an abstract and generic association, indicating that two [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) objects represent different aspects of the same underlying entity.

This relationship conveys what could be defined with multiple inheritance. It is restricted to the 'logical' aspects of a managed system element. In most scenarios, the Identity relationship is determined by the equivalence of Keys or some other identifying properties of the related elements. The association should only be used in well understood scenarios. This is why the association is abstract - allowing more concrete definition and clarification in subclasses. One of the scenarios where this relationship is reasonable is to represent that a Device is both a 'bus' entity and a 'functional' entity. For example, a Device could be both a USB (bus) and a Keyboard (functional) entity.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, AMENDMENT]
class CIM_LogicalIdentity
{
  CIM_LogicalElement REF SystemElement;
  CIM_LogicalElement REF SameElement;
};
```

## Members

The **CIM\_LogicalIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogicalIdentity** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) representing an alternate aspect of the system entity.

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) object containing one aspect of the logical element.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



 

 





