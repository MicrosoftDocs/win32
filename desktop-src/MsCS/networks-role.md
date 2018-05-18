---
title: Role
description: Provides the Role of the network in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ab1382e-15ca-4438-afec-28bc5071c811'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Role Failover Cluster ,for networks", "Role Failover Cluster"]
topic_type:
- apiref
api_name:
- Role
api_type:
- NA
---

# Role

Provides the **Role** of the [network](networks.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **Role** property.



| Attribute            | Value                                                  |
|----------------------|--------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                   |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>     |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/>   |
| Minimum<br/>   | **ClusterNetworkRoleNone** (0)<br/>              |
| Maximum<br/>   | **ClusterNetworkRoleInternalAndClient** (3)<br/> |
| Default<br/>   | **ClusterNetworkRoleInternalAndClient**<br/>     |



 

## Remarks

The data value for the **Role** property can be set to one of the following values of the [**CLUSTER\_NETWORK\_ROLE**](cluster-network-role.md) enumeration.



| Name                                               | Value        | Description                                                                                           |
|----------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------|
| **ClusterNetworkRoleNone**<br/>              | 0<br/> | The network is not used by the cluster.<br/>                                                    |
| **ClusterNetworkRoleInternalUse**<br/>       | 1<br/> | The network is used to carry internal cluster communication.<br/>                               |
| **ClusterNetworkRoleClientAccess**<br/>      | 2<br/> | Not supported.<br/>                                                                             |
| **ClusterNetworkRoleInternalAndClient**<br/> | 3<br/> | The network is used to connect client systems and to carry internal cluster communication.<br/> |



 

There are some restrictions to the data value. If any [IP Address](ip-address.md) resources reference this network, the **Role** property may not be changed to **ClusterNetworkRoleNone** or **ClusterNetworkRoleInternalUse**. If this network is the only one used for internal cluster communication, the **Role** property may not be changed to **ClusterNetworkRoleNone** or **ClusterNetworkRoleClientAccess**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Role** can be set with the following example code:


```C++
DWORD          RoleData = ClusterNetworkRoleClientAccess;
CLUSPROP_DWORD RoleValue;

RoleValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RoleValue.cbLength  = sizeof(DWORD);
RoleValue.dw        = RoleData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Network Common Properties](common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**CLUSTER\_NETWORK\_ROLE**](cluster-network-role.md)
</dt> </dl>

 

 





