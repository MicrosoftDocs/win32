---
Description: The CIM\_OperatingSystemSoftwareFeature class represents the software features that make up the operating system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ffc709c-213e-4252-9662-76f01e1685e5
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_OperatingSystemSoftwareFeature class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_OperatingSystemSoftwareFeature class

The **CIM\_OperatingSystemSoftwareFeature** class represents the software features that make up the operating system.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{96B4C734-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_OperatingSystemSoftwareFeature : CIM_Component
{
  CIM_SoftwareFeature REF PartComponent;
  CIM_OperatingSystem REF GroupComponent;
};
```

## Members

The **CIM\_OperatingSystemSoftwareFeature** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_OperatingSystemSoftwareFeature** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_OperatingSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

A [**CIM\_OperatingSystem**](cim-operatingsystem.md) describing the operating system.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A [**CIM\_SoftwareFeature**](cim-softwarefeature.md) describing the software features that make up the operating system.

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

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 




