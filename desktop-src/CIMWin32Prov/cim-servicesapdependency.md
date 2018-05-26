---
Description: The CIM\_ServiceSAPDependency class represents an association between a service and a service access point (SAP), which indicates that the referenced SAP is used by the service to provide its functionality.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf5a8b9b-a38e-4173-861c-e417fbea6016
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ServiceSAPDependency class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ServiceSAPDependency class

The **CIM\_ServiceSAPDependency** class represents an association between a service and a service access point (SAP), which indicates that the referenced SAP is used by the service to provide its functionality. For example, boot services can invoke BIOS disk services (interrupts) to function.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{652E2D58-DB37-11d2-85FC-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_ServiceSAPDependency : CIM_Dependency
{
  CIM_Service            REF Dependent;
  CIM_ServiceAccessPoint REF Antecedent;
};
```

## Members

The **CIM\_ServiceSAPDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ServiceSAPDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) that describes the required service access point.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_Service**](cim-service.md) that describes the service that is dependent on an underlying SAP.

</dd> </dl>

## Remarks

WMI does not implement this class.

The **CIM\_ServiceSAPDependency** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

 




