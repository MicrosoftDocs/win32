---
title: CIM\_SAPSAPDependency class
description: CIM\_SAPSAPDependency is an association between one ServiceAccessPoint and another ServiceAccessPoint that indicates that the latter is required for the former to utilize or connect with its Service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 85c3bf1e-3df7-4e2b-a207-61a00156f338
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SAPSAPDependency class iSCSI Software Target API
- CIM_SAPSAPDependency class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_SAPSAPDependency
- CIM_SAPSAPDependency.Antecedent
- CIM_SAPSAPDependency.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SAPSAPDependency class

CIM\_SAPSAPDependency is an association between one ServiceAccessPoint and another ServiceAccessPoint that indicates that the latter is required for the former to utilize or connect with its Service. For example, to print to a network printer, local Print Access Points must utilize underlying network-related SAPs, or ProtocolEndpoints, to send the print request.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service")]
class CIM_SAPSAPDependency : CIM_Dependency
{
  CIM_ServiceAccessPoint REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_SAPSAPDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SAPSAPDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The required ServiceAccessPoint.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The ServiceAccessPoint that is dependent on an underlying SAP.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





