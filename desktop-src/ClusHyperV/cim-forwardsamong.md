---
title: CIM\_ForwardsAmong class
description: Represents an association in which protocol endpoints depend on a forwarding service to forward data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f8e5e70e-fb87-44a1-ac92-8c2b8a220c27
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ForwardsAmong class
- CIM_ForwardsAmong class, described
topic_type:
- apiref
api_name:
- CIM_ForwardsAmong
- CIM_ForwardsAmong.Antecedent
- CIM_ForwardsAmong.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ForwardsAmong class

Represents an association in which protocol endpoints depend on a forwarding service to forward data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Network::RoutingForwarding")]
class CIM_ForwardsAmong : CIM_ServiceSAPDependency
{
  CIM_ProtocolEndpoint  REF Antecedent;
  CIM_ForwardingService REF Dependent;
};
```

## Members

The **CIM\_ForwardsAmong** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ForwardsAmong** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The protocol endpoints send and receive the forwarded data.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ForwardingService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The forwarding service that forwards the data.

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

[**CIM\_ServiceSAPDependency**](cim-servicesapdependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





