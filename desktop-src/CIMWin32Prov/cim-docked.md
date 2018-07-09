---
Description: The CIM\_Docked association represents the relationship between two chassis. For example, a laptop (a type of chassis) can be docked in a docking station (another type of chassis). This typical relationship is explicitly described.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72cb36bb-f79e-4d1a-a859-4024031e4ebc
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_Docked class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Docked
- CIM_Docked.Dependent
- CIM_Docked.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Docked class

The **CIM\_Docked** association represents the relationship between two chassis. For example, a laptop (a type of chassis) can be docked in a docking station (another type of chassis). This typical relationship is explicitly described.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, MappingStrings("MIF.DMTF|Dynamic States|001.2"), UUID("{FAF76B75-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_Docked : CIM_Dependency
{
  CIM_Chassis REF Dependent;
  CIM_Chassis REF Antecedent;
};
```

## Members

The **CIM\_Docked** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Docked** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Chassis**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**CIM\_Chassis**](cim-chassis.md) describing the docking station.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Chassis**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**CIM\_Chassis**](cim-chassis.md) describing the docked laptop.

</dd> </dl>

## Remarks

The **CIM\_Docked** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




