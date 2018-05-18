---
title: Processing Groups and Callbacks
description: The following table summarizes a series of steps in an operational interaction between a routing protocol and the multicast group manager.
ms.assetid: '43c1dc12-70fd-4e02-a7b1-5818e6d7ddc6'
---

# Processing Groups and Callbacks

The following table summarizes a series of steps in an operational interaction between a routing protocol and the multicast group manager. The first column describes the actions that the routing protocol performs and the routing protocol's responses to the multicast group manager. The second column describes the multicast group manager's responses to the routing protocol and any actions the multicast group manager performs such as callbacks. The third column presents any additional information.

Each row of the table represents one step.

The tasks listed in this table do not occur in any specific order; rather, they occur based on the status of multicast group memberships. The table below shows an example order.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Routing protocol action</th>
<th>Multicast group manager action</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Manage group memberships based on protocol information received on those interfaces that the protocol owns. Management is performed using the following functions:
<ul>
<li>[<strong>MgmAddGroupMembershipEntry</strong>](mgmaddgroupmembershipentry.md)</li>
<li>[<strong>MgmDeleteGroupMembershipEntry</strong>](mgmdeletegroupmembershipentry.md)</li>
</ul></td>
<td>Add to and delete from the outgoing interface list for the specified (s, g), (*, g), and (*, *) entries. This list represents the set of interfaces on which data for this group is forwarded. The data for this group is from the specified source.</td>

</tr>
<tr class="even">

<td>Send alerts to routing protocols in the form of callbacks. The following events trigger the multicast group manager to invoke a callback:
<ul>
<li>Join or leave groups ( [<strong>PMGM_JOIN_ALERT_CALLBACK</strong>](pmgm-join-alert-callback.md), [<strong>PMGM_PRUNE_ALERT_CALLBACK</strong>](pmgm-prune-alert-callback.md)).</li>
<li>Group membership changed by IGMP ( [<strong>PMGM_LOCAL_JOIN_CALLBACK</strong>](pmgm-local-join-callback.md), [<strong>PMGM_LOCAL_LEAVE_CALLBACK</strong>](pmgm-local-leave-callback.md)).</li>
<li>Data received on wrong interface ( [<strong>PMGM_WRONG_IF_CALLBACK</strong>](pmgm-wrong-if-callback.md)).</li>
<li>Data received from new sources or to a new group ( [<strong>PMGM_CREATION_ALERT_CALLBACK</strong>](pmgm-creation-alert-callback.md) and [<strong>PMGM_RPF_CALLBACK</strong>](pmgm-rpf-callback.md)).</li>
</ul></td>
<td>Using these callbacks, the multicast group manager is able to coordinate packet forwarding when several multicast routing protocols are present on a router.</td>
</tr>
<tr class="odd">
<td>Enumerate the multicast forwarding entries (MFEs), using the [<strong>MgmGetFirstMfe</strong>](mgmgetfirstmfe.md), [<strong>MgmGetNextMfe</strong>](mgmgetnextmfe.md), and [<strong>MgmGetMfe</strong>](mgmgetmfe.md) functions. Make decisions about multicast data based on the results of the enumeration.</td>
<td>Return the requested MFEs. Return ERROR_NO_MORE ITEMS when there are no more MFEs to return.<br/></td>
<td>Use the [<strong>MgmGetFirstMfeStats</strong>](mgmgetfirstmfestats.md), [<strong>MgmGetNextMfeStats</strong>](mgmgetnextmfestats.md), [<strong>MgmGetMfeStats</strong>](mgmgetmfestats.md) functions to enumerate MFE statistics. See [Administrative Application Scenario](administrative-application-scenario.md) for a complete example of using these functions.<br/></td>
</tr>
<tr class="even">
<td>Modify the upstream neighbor in an MFE using the [<strong>MgmSetMfe</strong>](mgmsetmfe.md) function.</td>

<td>Clients use this function to modify the information regarding the incoming interface.</td>
</tr>
</tbody>
</table>



 

 

 





