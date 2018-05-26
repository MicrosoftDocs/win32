---
title: CIM\_PortOnDevice class
description: Represents an association between a port or connection point and a device.
ms.assetid: 86ff3616-1218-4d86-91ea-78e8e82b70bb
keywords:
- CIM_PortOnDevice class Hyper-V
- CIM_PortOnDevice class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_PortOnDevice
- CIM_PortOnDevice.Antecedent
- CIM_PortOnDevice.Dependent
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

# CIM\_PortOnDevice class

Represents an association between a port or connection point and a device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.8.0"), AMENDMENT]
class CIM_PortOnDevice : CIM_HostedDependency
{
  CIM_LogicalDevice REF Antecedent;
  CIM_LogicalPort   REF Dependent;
};
```

## Members

The **CIM\_PortOnDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PortOnDevice** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The device that includes the port.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The port on the device.

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> </dl>

 

 





