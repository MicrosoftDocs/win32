---
Description: The CIM\_ServiceAccessBySAP association class represents the access points for a service. For example, a printer can be accessed by NetWare, Macintosh, or Windows service access points (SAPs), which are potentially hosted on different systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 68311a56-b034-4a30-a885-74a745a738d8
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ServiceAccessBySAP class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ServiceAccessBySAP
- CIM_ServiceAccessBySAP.Dependent
- CIM_ServiceAccessBySAP.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ServiceAccessBySAP class

The **CIM\_ServiceAccessBySAP** association class represents the access points for a service. For example, a printer can be accessed by NetWare, Macintosh, or Windows service access points (SAPs), which are potentially hosted on different systems.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{714C00BA-DB37-11d2-85FC-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_ServiceAccessBySAP : CIM_Dependency
{
  CIM_ServiceAccessPoint REF Dependent;
  CIM_Service            REF Antecedent;
};
```

## Members

The **CIM\_ServiceAccessBySAP** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ServiceAccessBySAP** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_Service**](cim-service.md) that describes the service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) that describes an access point for a service. Access points are dependent in this relationship since they have no function without a corresponding service.

</dd> </dl>

## Remarks

The **CIM\_ServiceAccessBySAP** class is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class. For WMI classes that are derived from **CIM\_ServiceAccessBySAP**, see [Win32 Classes](win32-provider.md).

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

 

 




