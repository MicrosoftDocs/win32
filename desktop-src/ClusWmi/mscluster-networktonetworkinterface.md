---
title: MSCluster\_NetworkToNetworkInterface class
description: A dynamic association WMI class that represents the network interfaces connected to a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 98e725a5-8ac7-4de7-bce2-b6ef946dc816
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_NetworkToNetworkInterface class
- MSCluster_NetworkToNetworkInterface class, described
topic_type:
- apiref
api_name:
- MSCluster_NetworkToNetworkInterface
- MSCluster_NetworkToNetworkInterface.GroupComponent
- MSCluster_NetworkToNetworkInterface.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_NetworkToNetworkInterface class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the network interfaces connected to a network.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{099B1BE4-D4BD-4b56-9815-AA90234B03C6}"), AMENDMENT]
class MSCluster_NetworkToNetworkInterface : CIM_Component
{
  MSCluster_Network          REF GroupComponent;
  MSCluster_NetworkInterface REF PartComponent;
};
```

## Members

The **MSCluster\_NetworkToNetworkInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_NetworkToNetworkInterface** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Network**](mscluster-network.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The network.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The networks interfaces.

</dd> </dl>

## Remarks

The **MSCluster\_NetworkToNetworkInterface** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





