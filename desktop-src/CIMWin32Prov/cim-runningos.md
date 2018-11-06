---
Description: The CIM\_RunningOS class represents the currently executing operating system. At most, one operating system can execute at any time on a computer system; the computer system may not be currently booted, or its operating system may be unknown.
ms.assetid: 93e3d425-d751-4252-aa81-7d6774c8f8c5
ms.tgt_platform: multiple
title: CIM_RunningOS class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RunningOS
- CIM_RunningOS.Dependent
- CIM_RunningOS.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_RunningOS class

The **CIM\_RunningOS** class represents the currently executing operating system. At most, one operating system can execute at any time on a computer system; the computer system may not be currently booted, or its operating system may be unknown.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{1F2EA300-DB37-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_RunningOS : CIM_Dependency
{
  CIM_ComputerSystem  REF Dependent;
  CIM_OperatingSystem REF Antecedent;
};
```

## Members

The **CIM\_RunningOS** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RunningOS** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_OperatingSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_OperatingSystem**](cim-operatingsystem.md) that describes the operating system currently running on the computer system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_ComputerSystem**](cim-computersystem.md) that describes the computer system.

</dd> </dl>

## Remarks

The **CIM\_RunningOS** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




