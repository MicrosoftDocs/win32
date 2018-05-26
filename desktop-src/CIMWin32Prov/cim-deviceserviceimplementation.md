---
Description: The CIM\_DeviceServiceImplementation class represents an association between a service and how it is implemented.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5e2e3975-8338-4bf4-8c73-5be4b93fa2c8
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_DeviceServiceImplementation class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_DeviceServiceImplementation class

The **CIM\_DeviceServiceImplementation** class represents an association between a service and how it is implemented. When multiple devices are associated with one service, the elements operate in conjunction to provide the service. If different implementations of a service exist, each implementation results in individual instantiations of the service object.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{290FC242-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_DeviceServiceImplementation : CIM_Dependency
{
  CIM_Service       REF Dependent;
  CIM_LogicalDevice REF Antecedent;
};
```

## Members

The **CIM\_DeviceServiceImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DeviceServiceImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_Service**](cim-service.md) that describes the service implemented using the logical device.

</dd> </dl>

## Remarks

WMI does not implement this class.

The **CIM\_DeviceServiceImplementation** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




