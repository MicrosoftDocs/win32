---
Description: The CIM\_DeviceAccessedByFile association class specifies the logical device accessed by using the referenced CIM\_DeviceFile class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ba44f40-8b84-4f5c-b719-aded10877654
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_DeviceAccessedByFile class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_DeviceAccessedByFile class

The **CIM\_DeviceAccessedByFile** association class specifies the logical device accessed by using the referenced [**CIM\_DeviceFile**](cim-devicefile.md) class.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{05D1FFF2-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_DeviceAccessedByFile : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_DeviceFile    REF Antecedent;
};
```

## Members

The **CIM\_DeviceAccessedByFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DeviceAccessedByFile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DeviceFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_DeviceFile**](cim-devicefile.md) that describes the device file.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the device that is accessed using the device file.

</dd> </dl>

## Remarks

WMI does not implement this class.

The **CIM\_DeviceAccessedByFile** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




