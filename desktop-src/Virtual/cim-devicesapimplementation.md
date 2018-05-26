---
title: CIM\_DeviceSAPImplementation class
description: Represents an association between a service access point (SAP) and a logical device that implements it.
ms.assetid: 9a451e38-cc5d-4375-ad6a-dd4b8e3405f4
keywords:
- CIM_DeviceSAPImplementation class Hyper-V
- CIM_DeviceSAPImplementation class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_DeviceSAPImplementation
- CIM_DeviceSAPImplementation.Antecedent
- CIM_DeviceSAPImplementation.Dependent
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

# CIM\_DeviceSAPImplementation class

Represents an association between a service access point (SAP) and a logical device that implements it.

Multiple logical devices can operate in conjunction to implement the same SAP. In addition, a logical device can implement more than one SAP.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), AMENDMENT]
class CIM_DeviceSAPImplementation : CIM_Dependency
{
  CIM_LogicalDevice      REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_DeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DeviceSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](cim-logicaldevice.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The SAP implemented by the logical device.

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

 

 





