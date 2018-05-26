---
title: MSCluster\_NodeToNetworkInterface class
description: A dynamic association WMI class that represents the network interfaces connected to a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 971f6514-f7ac-488d-8e83-67530d525185
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_NodeToNetworkInterface class
- MSCluster_NodeToNetworkInterface class, described
topic_type:
- apiref
api_name:
- MSCluster_NodeToNetworkInterface
- MSCluster_NodeToNetworkInterface.GroupComponent
- MSCluster_NodeToNetworkInterface.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_NodeToNetworkInterface class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [network interfaces](https://msdn.microsoft.com/library/aa371519) connected to a [node](https://msdn.microsoft.com/library/aa371745).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{82459303-B1E9-4ddf-970F-25B17AD2A01B}"), AMENDMENT]
class MSCluster_NodeToNetworkInterface : CIM_SystemDevice
{
  MSCluster_Node             REF GroupComponent;
  MSCluster_NetworkInterface REF PartComponent;
};
```

## Members

The **MSCluster\_NodeToNetworkInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_NodeToNetworkInterface** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The node.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_NetworkInterface**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The group that is active on the node.

</dd> </dl>

## Remarks

The **MSCluster\_NodeToNetworkInterface** class is derived from the **CIM\_SystemDevice** class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





