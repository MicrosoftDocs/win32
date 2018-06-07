---
Description: The CIM\_AssociatedSensor class associates an installed sensor with a logical device. The sensor measures critical input and output properties, and can be included with the device or installed nearby.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ccaa37f-b95f-4582-a694-23bdc15b8c8b
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_AssociatedSensor class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_AssociatedSensor class

The **CIM\_AssociatedSensor** class associates an installed sensor with a logical device. The sensor measures critical input and output properties, and can be included with the device or installed nearby.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{956597A0-7D80-11D2-AAD3-006008C78BC7}"), AMENDMENT]
class CIM_AssociatedSensor : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_Sensor        REF Antecedent;
};
```

## Members

The **CIM\_AssociatedSensor** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AssociatedSensor** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Sensor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_Sensor**](cim-sensor.md) that describes the sensor.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the logical device for which information is measured by the sensor.

</dd> </dl>

## Remarks

The **CIM\_AssociatedSensor** class is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class. For more information about classes derived from **CIM\_AssociatedSensor**, see [Win32 Classes](win32-provider.md).

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

 

 




