---
Description: The CIM\_AssociatedAlarm dependency associates an alarm with a logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed0ccc81-6d1b-45b0-abf0-7a2bd9a50193
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_AssociatedAlarm class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_AssociatedAlarm class

The **CIM\_AssociatedAlarm** dependency associates an alarm with a logical device.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, UUID("{2280CB02-DB35-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_AssociatedAlarm : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_AlarmDevice   REF Antecedent;
};
```

## Members

The **CIM\_AssociatedAlarm** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AssociatedAlarm** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_AlarmDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_AlarmDevice**](cim-alarmdevice.md) that contains the alarm device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that contains the logical device that is alarmed.

</dd> </dl>

## Remarks

The **CIM\_AssociatedAlarm** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




