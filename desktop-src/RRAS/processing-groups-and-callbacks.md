---
title: Processing Groups and Callbacks
description: The following table summarizes a series of steps in an operational interaction between a routing protocol and the multicast group manager.
ms.assetid: 43c1dc12-70fd-4e02-a7b1-5818e6d7ddc6
ms.topic: article
ms.date: 05/31/2018
---

# Processing Groups and Callbacks

The following table summarizes a series of steps in an operational interaction between a routing protocol and the multicast group manager. The first column describes the actions that the routing protocol performs and the routing protocol's responses to the multicast group manager. The second column describes the multicast group manager's responses to the routing protocol and any actions the multicast group manager performs such as callbacks. The third column presents any additional information.

Each row of the table represents one step.

The tasks listed in this table do not occur in any specific order; rather, they occur based on the status of multicast group memberships. The table below shows an example order.




| Routing protocol action | Multicast group manager action | Notes | 
|-------------------------|--------------------------------|-------|
| Manage group memberships based on protocol information received on those interfaces that the protocol owns. Management is performed using the following functions:<ul><li><a href="/windows/desktop/api/Mgm/nf-mgm-mgmaddgroupmembershipentry"><strong>MgmAddGroupMembershipEntry</strong></a></li><li><a href="/windows/desktop/api/Mgm/nf-mgm-mgmdeletegroupmembershipentry"><strong>MgmDeleteGroupMembershipEntry</strong></a></li></ul> | Add to and delete from the outgoing interface list for the specified (s, g), (*, g), and (*, *) entries. This list represents the set of interfaces on which data for this group is forwarded. The data for this group is from the specified source. | 
| Send alerts to routing protocols in the form of callbacks. The following events trigger the multicast group manager to invoke a callback:<ul><li>Join or leave groups ( <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_join_alert_callback"><strong>PMGM_JOIN_ALERT_CALLBACK</strong></a>, <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_prune_alert_callback"><strong>PMGM_PRUNE_ALERT_CALLBACK</strong></a>).</li><li>Group membership changed by IGMP ( <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_local_join_callback"><strong>PMGM_LOCAL_JOIN_CALLBACK</strong></a>, <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_local_leave_callback"><strong>PMGM_LOCAL_LEAVE_CALLBACK</strong></a>).</li><li>Data received on wrong interface ( <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_wrong_if_callback"><strong>PMGM_WRONG_IF_CALLBACK</strong></a>).</li><li>Data received from new sources or to a new group ( <a href="/windows/desktop/api/mgm/nc-mgm-pmgm_creation_alert_callback"><strong>PMGM_CREATION_ALERT_CALLBACK</strong></a> and <a href="/windows/desktop/api/Mgm/nc-mgm-pmgm_rpf_callback"><strong>PMGM_RPF_CALLBACK</strong></a>).</li></ul> | Using these callbacks, the multicast group manager is able to coordinate packet forwarding when several multicast routing protocols are present on a router. | 
| Enumerate the multicast forwarding entries (MFEs), using the <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfe"><strong>MgmGetFirstMfe</strong></a>, <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetnextmfe"><strong>MgmGetNextMfe</strong></a>, and <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetmfe"><strong>MgmGetMfe</strong></a> functions. Make decisions about multicast data based on the results of the enumeration. | Return the requested MFEs. Return ERROR_NO_MORE ITEMS when there are no more MFEs to return.<br /> | Use the <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfestats"><strong>MgmGetFirstMfeStats</strong></a>, <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetnextmfestats"><strong>MgmGetNextMfeStats</strong></a>, <a href="/windows/desktop/api/Mgm/nf-mgm-mgmgetmfestats"><strong>MgmGetMfeStats</strong></a> functions to enumerate MFE statistics. See <a href="administrative-application-scenario.md">Administrative Application Scenario</a> for a complete example of using these functions.<br /> | 
| Modify the upstream neighbor in an MFE using the <a href="/windows/desktop/api/Mgm/nf-mgm-mgmsetmfe"><strong>MgmSetMfe</strong></a> function. | Clients use this function to modify the information regarding the incoming interface. | 




 

 

