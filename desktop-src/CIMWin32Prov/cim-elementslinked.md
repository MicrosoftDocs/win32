---
Description: The CIM\_ElementsLinked association represents physical elements that are cabled together by a physical link.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b9e1d11e-6f89-4d7a-9b5c-01161e7c1bdf
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ElementsLinked class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ElementsLinked class

The **CIM\_ElementsLinked** association represents physical elements that are cabled together by a physical link.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B83-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ElementsLinked : CIM_Dependency
{
  CIM_PhysicalElement REF Dependent;
  CIM_PhysicalLink    REF Antecedent;
};
```

## Members

The **CIM\_ElementsLinked** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementsLinked** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalLink**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_PhysicalLink**](cim-physicallink.md) that describes the physical link.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_PhysicalElement**](cim-physicalelement.md) that describes the physical element that is linked.

</dd> </dl>

## Remarks

The **CIM\_ElementsLinked** class is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




