---
Description: The CIM\_ProductParentChild association defines a parent-child hierarchy among products. For example, a product can come bundled with other products.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 244576fd-8dae-4554-b80b-0cac58c93037
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ProductParentChild class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ProductParentChild class

The **CIM\_ProductParentChild** association defines a parent-child hierarchy among products. For example, a product can come bundled with other products.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{3E24D5A6-DB2B-11d2-85FC-0000F8102E5F}"), Aggregation, Association, AMENDMENT]
class CIM_ProductParentChild
{
  CIM_Product REF Child;
  CIM_Product REF Parent;
};
```

## Members

The **CIM\_ProductParentChild** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProductParentChild** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the child product in the association.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the parent product in the association.

</dd> </dl>

## Remarks

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



 

 




