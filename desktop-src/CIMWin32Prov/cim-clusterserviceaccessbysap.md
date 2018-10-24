---
Description: The CIM\_ClusterServiceAccessBySAP class represents the relationship between a clustering service and its access points.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1e03ef1-909c-4836-a75f-c8d88a4d0087
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM_ClusterServiceAccessBySAP class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ClusterServiceAccessBySAP
- CIM_ClusterServiceAccessBySAP.Dependent
- CIM_ClusterServiceAccessBySAP.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ClusterServiceAccessBySAP class

The **CIM\_ClusterServiceAccessBySAP** class represents the relationship between a clustering service and its access points.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{88F073D8-DB35-11d2-85FC-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_ClusterServiceAccessBySAP : CIM_ServiceAccessBySAP
{
  CIM_ClusteringSAP     REF Dependent;
  CIM_ClusteringService REF Antecedent;
};
```

## Members

The **CIM\_ClusterServiceAccessBySAP** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ClusterServiceAccessBySAP** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ClusteringService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**CIM\_ClusteringService**](cim-clusteringservice.md) that describes the clustering service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ClusteringSAP**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_ClusteringSAP**](cim-clusteringsap.md) that describes an access point for the clustering service.

</dd> </dl>

## Remarks

The **CIM\_ClusterServiceAccessBySAP** class is derived from [**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md).

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

[**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md)
</dt> </dl>

 

 




