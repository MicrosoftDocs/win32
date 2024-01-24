---
title: IPv6-Aware and Legacy WPAD helper functions
description: Differences Between IPv6-Aware WPAD Helper Functions and Legacy WPAD Helper Functions
ms.assetid: ea4b1c0d-ce02-477b-85c8-44e1beef90c1
ms.topic: article
ms.date: 05/31/2018
---

# IPv6-Aware and Legacy WPAD helper functions

The following tables explain the differences between the new WPAD helper functions and the legacy WPAD helper functions. The new functions are marked with an asterisk.



<table>
<thead>
<tr class="header">
<th>Functions</th>
<th>Input</th>
<th>Output</th>
<th>Reason for Change</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>dnsResolve</td>
<td>Host</td>
<td>IPv4 address</td>
<td rowspan="2">Ex function will return a list of IPv6/IPv4. Necessary since IPv6 or IPv4 addresses can have multiple unicast addresses for a single interface.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>dnsResolveEx*</td>
<td>Host</td>
<td>List of IPv6/IPv4 addresses</td>

</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>Functions</th>
<th>Input</th>
<th>Output</th>
<th>Reason for Change</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>isResolveable</td>
<td>IPv4 host</td>
<td>TRUE / FALSE</td>
<td rowspan="2">The Ex function will return TRUE if a host can resolve to an IPv6 or IPv4 address. The legacy function only returns TRUE if the host resolves to an IPv4 address.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>isResolveableEx*</td>
<td>IPv6/IPv4 host</td>
<td>TRUE / FALSE</td>

</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>Functions</th>
<th>Input</th>
<th>Output</th>
<th>Reason for Change</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>myIPAddress</td>
<td>none</td>
<td>IPv4 address</td>
<td rowspan="2">Ex function will return a list of IPv6/IPv4. Necessary since IPv6 or IPv4 addresses can have multiple unicast addresses for a single interface ${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>myIPAddressEx*</td>
<td>none</td>
<td>List of IPv6/IPv4 addresses</td>

</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>Functions</th>
<th>Input</th>
<th>Output</th>
<th>Reason for Change</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>isInNet</td>
<td>Host, Dot separated IP address pattern, IP address Mask</td>
<td>TRUE / FALSE</td>
<td rowspan="2">Provide an IP version agnostic way to find if an IP address is in a given subnet. Also, the mask notation in IPv4 is deprecated.${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>isInNetEx*</td>
<td>IP Address IP Prefix</td>
<td>TRUE / FALSE</td>

</tr>
</tbody>
</table>



 



| Functions           | Input                       | Output                             | Reason for Change                                                                                                                           |
|---------------------|-----------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| sortIPAddressList\* | List of IPv6/IPv4 addresses | Sorted List of IPv6/IPv4 addresses | There is no counterpart legacy function because legacy functions only returned a single IPv4 address, therefore there was no need to sort . |



 



| Functions          | Input | Output                     | Reason for Change                                                                                                                                                                                                           |
|--------------------|-------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| getClientVersion\* | none  | WPAD engine version number | Currently this function returns version 1.0. We added this function to allow IT administrators to update their WPAD to work with different versions of the WPAD engine without causing breaks to their existent deployment. |



 

> [!Note]  
> This functionality requires Windows Internet Explorer 7 or greater.

 

 

 



