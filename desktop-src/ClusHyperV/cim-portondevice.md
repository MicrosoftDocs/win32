---
title: CIM\_PortOnDevice class
description: Represents an association between a port or connection point and a device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7e8ab5c9-e002-4814-8db0-ac67e04798df
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_PortOnDevice class
- CIM_PortOnDevice class, described
topic_type:
- apiref
api_name:
- CIM_PortOnDevice
- CIM_PortOnDevice.Antecedent
- CIM_PortOnDevice.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_PortOnDevice class

Represents an association between a port or connection point and a device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Device::Ports")]
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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





