---
title: Prune Alert Callbacks
description: When the multicast group manager is notified that receivers are leaving a group on an interface, the multicast group manager invokes the PMGM\_PRUNE\_ALERT\_CALLBACK callback.
ms.assetid: 34eb6941-9488-481f-93ca-821789acc140
ms.topic: article
ms.date: 05/31/2018
---

# Prune Alert Callbacks

When the multicast group manager is notified that receivers are leaving a group on an interface, the multicast group manager invokes the [**PMGM\_PRUNE\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_prune_alert_callback) callback. This callback notifies the routing protocols that clients no longer belong to the specified group. Therefore, the routing protocols must stop requesting multicast data for the specified groups.

The multicast group manager has a predefined set of rules that are used to determine when this callback is invoked. These rules are based on both the type of prune request sent by the client and the order the prune requests were received in.

## Wildcard Prune Requests

When a wildcard prune for a group (\*, g) is received and the final interface is being removed for the second-to-last client (that is, when interfaces for only a single client remain), the multicast group manager invokes the [**PMGM\_PRUNE\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_prune_alert_callback) callback to that remaining client. After the final interface is removed for the last client (that is, when no other interfaces remain), then this callback is invoked for all the other clients that are registered with the multicast group manager.

## Source-Specific Prune Requests

When a source-specific prune for a group (s, g) is received, the multicast group manager invokes the [**PMGM\_PRUNE\_ALERT\_CALLBACK**](/windows/desktop/api/Mgm/nc-mgm-pmgm_prune_alert_callback) callback only for the client that owns the incoming interface towards the source s.

 

 




