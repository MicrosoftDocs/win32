---
description: This page describes the behavior of multicast socket options based on various socket option settings states.
ms.assetid: a411e831-7b28-4ab5-a09a-650db99a7cd5
title: Multicast Socket Option Behavior
ms.topic: article
ms.date: 05/31/2018
---

# Multicast Socket Option Behavior

This page describes the behavior of multicast socket options based on various socket option settings states.

For example, this page describes the behavior when the IP\_ADD\_SOURCE\_MEMBERSHIP socket option is set on a socket for which the IP\_ADD\_SOURCE\_MEMBERSHIP option has already been set with the specified group/source pair on the same network interface. It is permitted to call IP\_ADD\_SOURCE\_MEMBERSHIP on the same group on a different network interface.

This page assists in properly designing and troubleshooting Windows Sockets multicast applications. 

<table>
<thead>
<tr class="header">
<th>Initial socket option</th>
<th>Conflicting subsequent socket option</th>
<th>Error returned</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4">IP_ADD_MEMBERSHIP<br />
</td>
<td>IP_ADD_MEMBERSHIP</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Do not call IP_ADD_MEMBERSHIP with the same group more than once on the same network interface.</td>
</tr>
<tr class="even">
<td>IP_ADD_SOURCE_MEMBERSHIP</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Do not call IP_ADD_SOURCE_MEMBERSHIP with the same group previously called with IP_ADD_MEMBERSHIP on the same network interface.</td>

</tr>
<tr class="odd">
<td>IP_DROP_SOURCE_MEMBERSHIP</td>
<td>WSAEINVAL</td>
<td>Use IP_BLOCK_SOURCE instead.</td>

</tr>
<tr class="even">
<td>IP_UNBLOCK_SOURCE</td>
<td>WSAEINVAL</td>
<td>Returns an error when attempting to unblock a group/source pair that has not previously been blocked on the same network interface.</td>

</tr>
<tr class="odd">
<td>IP_DROP_MEMBERSHIP</td>
<td>Any subsequent call on the same group or group/source pair</td>
<td>WSAEINVAL</td>
<td>Making socket option calls on a group or group/source pair not currently in the inclusion list (due to dropping membership, or otherwise) results in an error.</td>
</tr>
<tr class="even">
<td rowspan="3">IP_ADD_SOURCE_MEMBERSHIP<br />
</td>
<td>IP_ADD_MEMBERSHIP</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Do not call IP_ADD_MEMBERSHIP with the same group previously called with IP_ADD_SOURCE_MEMBERSHIP on the same network interface.</td>
</tr>
<tr class="odd">
<td>IP_ADD_SOURCE_MEMBERSHIP</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Do not call IP_ADD_SOURCE_MEMBERSHIP with the same group/source pair previously called with IP_ADD_SOURCE_MEMBERSHIP on the same network interface.</td>

</tr>
<tr class="even">
<td>IP_UNBLOCK_SOURCE</td>
<td>WSAEINVAL</td>
<td>Returns an error when attempting to unblock a group/source pair that has not previously been blocked on the same network interface.</td>

</tr>
<tr class="odd">
<td rowspan="2">IP_DROP_SOURCE_MEMBERSHIP<br />
</td>
<td>IP_UNBLOCK_SOURCE</td>
<td>WSAEINVAL</td>
<td>Returns an error when attempting to unblock a group/source pair that has not previously been blocked on the same network interface.</td>
</tr>
<tr class="even">
<td>IP_DROP_SOURCE_MEMBERSHIP</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Returns an error when attempting to drop a group/source pair that is not in the inclusion list on the same network interface.</td>

</tr>
<tr class="odd">
<td rowspan="3">IP_BLOCK_SOURCE<br />
</td>
<td>IP_BLOCK_SOURCE</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Returns an error when attempting to block a group/source pair that is already blocked on the same network interface.</td>
</tr>
<tr class="even">
<td>IP_ADD_SOURCE_MEMBERSHIP</td>
<td>WSAEINVAL</td>
<td>Use IP_UNBLOCK_SOURCE instead.</td>

</tr>
<tr class="odd">
<td>IP_ADD_MEMBERSHIP</td>
<td>WSAEINVAL</td>
<td>Use IP_UNBLOCK_SOURCE instead.</td>

</tr>
<tr class="even">
<td>IP_UNBLOCK_SOURCE</td>
<td>IP_UNBLOCK_SOURCE</td>
<td>WSAEADDRNOTAVAIL</td>
<td>Returns an error when attempting to unblock a group/source pair that is not in the blocked list on the same network interface.</td>
</tr>
</tbody>
</table>



 

 

 



