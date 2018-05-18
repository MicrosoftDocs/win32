---
title: DefaultNetworkRole
description: Specifies the role that the cluster automatically assigns to any newly discovered or created network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '21ba6d5d-9a0f-4c60-9694-87a40dcb0c33'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DefaultNetworkRole Failover Cluster ,for clusters", "DefaultNetworkRole Failover Cluster"]
topic_type:
- apiref
api_name:
- DefaultNetworkRole
api_type:
- NA
---

# DefaultNetworkRole

Specifies the [**role**](networks-role.md) that the [*cluster*](c-gly.md#-wolf-cluster-gly) automatically assigns to any newly discovered or created [network](networks.md). The following table summarizes the attributes of the **DefaultNetworkRole** property.



| Attribute            | Value                                                  |
|----------------------|--------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                   |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>     |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/>   |
| Minimum<br/>   | **ClusterNetworkRoleNone** (0)<br/>              |
| Maximum<br/>   | **ClusterNetworkRoleInternalAndClient** (3)<br/> |
| Default<br/>   | **ClusterNetworkRoleInternalAndClient**<br/>     |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CLUS\_DEFAULT\_NETWORK\_ROLE**.

When the [Cluster service](cluster-service.md) detects a new network, it sets the network's [**Role**](networks-role.md) property to the value specified by **DefaultNetworkRole**. Thereafter, the network's role can be changed only by adjusting its **Role** property. Changing **DefaultNetworkRole** will not affect previously detected networks.

The **DefaultNetworkRole** property can be set to one of the following values of the [**CLUSTER\_NETWORK\_ROLE**](cluster-network-role.md) enumeration.



| Name                                               | Value        | Description                                                                                           |
|----------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------|
| **ClusterNetworkRoleNone**<br/>              | 0<br/> | The network is not used by the cluster.<br/>                                                    |
| **ClusterNetworkRoleInternalUse**<br/>       | 1<br/> | The network is used to carry internal cluster communication.<br/>                               |
| **ClusterNetworkRoleClientAccess**<br/>      | 2<br/> | Not supported.<br/>                                                                             |
| **ClusterNetworkRoleInternalAndClient**<br/> | 3<br/> | The network is used to connect client systems and to carry internal cluster communication.<br/> |



 

## Examples

The following example shows how to set the property value portion of a [property list](property-lists.md) entry for **DefaultNetworkRole**.


```C++
DWORD          DefaultNetworkRoleData = ClusterNetworkRoleInternalAndClient;
CLUSPROP_DWORD DefaultNetworkRoleValue;

DefaultNetworkRoleValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DefaultNetworkRoleValue.cbLength  = sizeof(DWORD);
DefaultNetworkRoleValue.dw        = DefaultNetworkRoleData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**CLUSTER\_NETWORK\_ROLE**](cluster-network-role.md)
</dt> </dl>

 

 





