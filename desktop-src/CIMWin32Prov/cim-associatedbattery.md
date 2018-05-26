---
Description: The CIM\_AssociatedBattery dependency associates a battery with a logical device. Use this association to model individual batteries that make up an uninterruptible power supply (UPS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f8d8b3d3-edc5-438a-8be6-3ea4d765085b
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_AssociatedBattery class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_AssociatedBattery class

The **CIM\_AssociatedBattery** dependency associates a battery with a logical device. Use this association to model individual batteries that make up an uninterruptible power supply (UPS).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8502C578-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class CIM_AssociatedBattery : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_Battery       REF Antecedent;
};
```

## Members

The **CIM\_AssociatedBattery** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AssociatedBattery** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Battery**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_Battery**](cim-battery.md) that describes the battery.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that contains the logical device needing or associated with the battery.

</dd> </dl>

## Remarks

The **CIM\_AssociatedBattery** class is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class. For more information about classes derived from **CIM\_AssociatedBattery**, see [Win32 Classes](win32-provider.md).

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

 

 




