---
title: CIM\_ServiceSAPDependency class
description: Represents an association between a service and a service access point (SAP) that provides the service with functionality.
ms.assetid: 04151228-4d21-422f-8e84-f4d05b23c54d
keywords:
- CIM_ServiceSAPDependency class Hyper-V
- CIM_ServiceSAPDependency class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_ServiceSAPDependency
- CIM_ServiceSAPDependency.Antecedent
- CIM_ServiceSAPDependency.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ServiceSAPDependency class

Represents an association between a service and a service access point (SAP) that provides the service with functionality.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.10.0")]
class CIM_ServiceSAPDependency : CIM_Dependency
{
  CIM_ServiceAccessPoint REF Antecedent;
  CIM_Service            REF Dependent;
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

The required service access point.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The service that is dependent on the SAP.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





