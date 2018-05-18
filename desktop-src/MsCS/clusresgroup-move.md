---
title: ClusResGroup.Move method
description: Moves a group and all of its resources from one node to another.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8f923a22-31b2-4a41-b88d-8eb7bac9725e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Move method Failover Cluster", "Move method Failover Cluster , ClusResGroup object", "ClusResGroup object Failover Cluster , Move method"]
topic_type:
- apiref
api_name:
- ClusResGroup.Move
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroup.Move method

\[The **Move** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Moves a [group](groups.md) and all of its [resources](resources.md) from one [node](nodes.md) to another.

## Syntax


```VB
ClusResGroup.Move( _
  ByVal varTimeout, _
  [ ByVal objNode ] _
)
```



## Parameters

<dl> <dt>

*varTimeout* 
</dt> <dd>

A **Variant** that specifies how long (in seconds) the method should wait for the move to complete before setting *varPending* to **TRUE** and returning.

</dd> <dt>

*objNode* \[optional\]
</dt> <dd>

Optional. A [**ClusNode**](clusnode-object.md) object that represents the node to which the group should be moved. If no node is specified, the **Move** method moves the group to the best available node.

</dd> </dl>

## Return value

A **Variant** that is set to **TRUE** if the request is still pending.

## Remarks

Unless a node is specified, **Move** automatically selects the destination node on the basis of the following data:

-   The set of currently active nodes.
-   The group's prioritized list of [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly) nodes (see [**ClusResGroup.PreferredOwnerNodes**](clusresgroup-preferredownernodes.md)).
-   The set of nodes listed as possible owners by all resources in the group. To access the possible owners list for a resource, use the [**ClusResource.PossibleOwnerNodes**](clusresource-possibleownernodes.md) property.

**Move** selects the most preferred node from the set of possible active nodes. If no active nodes are listed as possible owners by all resources in the group, **Move** fails.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





