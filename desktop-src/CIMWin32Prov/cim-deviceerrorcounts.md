---
Description: The CIM\_DeviceErrorCounts class is a statistical class that contains error-related counters for a logical device. The types of errors are defined by CCITT (Rec X.733) and ISO (IEC 10164-4).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d65cbc78-40f2-4846-bd47-76e04b2f588b
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_DeviceErrorCounts class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DeviceErrorCounts
- CIM_DeviceErrorCounts.Caption
- CIM_DeviceErrorCounts.Description
- CIM_DeviceErrorCounts.CriticalErrorCount
- CIM_DeviceErrorCounts.DeviceCreationClassName
- CIM_DeviceErrorCounts.DeviceID
- CIM_DeviceErrorCounts.Name
- CIM_DeviceErrorCounts.IndeterminateErrorCount
- CIM_DeviceErrorCounts.MajorErrorCount
- CIM_DeviceErrorCounts.MinorErrorCount
- CIM_DeviceErrorCounts.SystemCreationClassName
- CIM_DeviceErrorCounts.SystemName
- CIM_DeviceErrorCounts.WarningCount
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_DeviceErrorCounts class

The **CIM\_DeviceErrorCounts** class is a statistical class that contains error-related counters for a logical device. The types of errors are defined by CCITT (Rec X.733) and ISO (IEC 10164-4).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{117FDB8C-D025-11d2-85F5-0000F8102E5F}"), AMENDMENT]
class CIM_DeviceErrorCounts : CIM_StatisticalInformation
{
  string Caption;
  string Description;
  uint64 CriticalErrorCount;
  string DeviceCreationClassName;
  string DeviceID;
  string Name;
  uint64 IndeterminateErrorCount;
  uint64 MajorErrorCount;
  uint64 MinorErrorCount;
  string SystemCreationClassName;
  string SystemName;
  uint64 WarningCount;
};
```

## Members

The **CIM\_DeviceErrorCounts** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_DeviceErrorCounts** class has these methods.



| Method                                                                     | Description                                                               |
|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**ResetCounter**](resetcounter-method-in-class-cim-deviceerrorcounts.md) | Resets the error and warning counters. Not implemented by WMI.<br/> |



 

### Properties

The **CIM\_DeviceErrorCounts** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description for the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

</dd> <dt>

**CriticalErrorCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|003.7")
</dt> </dl>

Count of the critical errors.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

</dd> <dt>

**DeviceCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**CreationClassName**"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping device's **CreationClassName** property.

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**DeviceID**"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The scoping device's identifier.

</dd> <dt>

**IndeterminateErrorCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Count of the indeterminate errors.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**MajorErrorCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|003.8")
</dt> </dl>

Count of the major errors.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**MinorErrorCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Count of the minor errors.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The inherited Name property serves as part of the key for the **CIM\_DeviceErrorCounts** instance. The object is scoped by the logical device to which the statistics apply.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**SystemCreationClassName**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Scoping system's **CreationClassName**.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**SystemName**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Scoping system's **Name** property.

</dd> <dt>

**WarningCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|003.9")
</dt> </dl>

Count of the warnings.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

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



## See also

<dl> <dt>

[**CIM\_StatisticalInformation**](cim-statisticalinformation.md)
</dt> </dl>

 

 




