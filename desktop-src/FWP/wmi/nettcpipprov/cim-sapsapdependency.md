---
description: CIM\_SAPSAPDependency is an association between one ServiceAccessPoint and another ServiceAccessPoint that indicates that the latter is required for the former to utilize or connect with its Service.
ms.assetid: 0b806e1e-2536-4c68-8a69-acedbb929023
title: CIM\_SAPSAPDependency class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SAPSAPDependency
- CIM_SAPSAPDependency.Antecedent
- CIM_SAPSAPDependency.Dependent
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_SAPSAPDependency class

CIM\_SAPSAPDependency is an association between one ServiceAccessPoint and another ServiceAccessPoint that indicates that the latter is required for the former to utilize or connect with its Service. For example, to print to a network printer, local Print Access Points must utilize underlying network-related SAPs, or ProtocolEndpoints, to send the print request.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Core::Service"), Version("2.10.0"), AMENDMENT]
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

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) containing the required service access point (SAP).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) that is dependent on an underlying SAP.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

