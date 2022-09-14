---
title: Join Alert Callbacks
description: When the multicast group manager is notified that there are new receivers present for a group on an interface, the multicast group manager invokes the PMGM\_JOIN\_ALERT\_CALLBACK callback.
ms.assetid: b625f8ec-f59b-4151-aa38-48cf8f004966
ms.topic: article
ms.date: 05/31/2018
---

# Join Alert Callbacks

When the multicast group manager is notified that there are new receivers present for a group on an interface, the multicast group manager invokes the [**PMGM\_JOIN\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_join_alert_callback) callback. This callback notifies the routing protocols that new hosts have joined the specified groups . Therefore, the routing protocols must request multicast data for the groups specified by the callback.

The multicast group manager uses a predefined set of rules that are used to determine when this callback is invoked. This set of rules is based on both the type of join request sent by the client and the order the join requests were received in.

## Wildcard Join Requests

When a wildcard join for a group (\*, g) is received from the first client, the multicast group manager invokes the [**PMGM\_JOIN\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_join_alert_callback) callback to all other registered clients. When a wildcard join for a group is received from the second client, the multicast group manager invokes this callback to the first client to join the group.

## Source-Specific Join Requests

The multicast group manager does not invoke this callback for any subsequent joins to the group.

When a source-specific join for a group (s, g) is received, the multicast group manager invokes the [**PMGM\_JOIN\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_join_alert_callback) callback only for the client that owns the incoming interface towards the source s.

 

 




