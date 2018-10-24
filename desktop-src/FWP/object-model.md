---
title: Object Model
description: The following table lists the object types that can be manipulated through the various API sets supplied by the Windows Filtering Platform (WFP).
ms.assetid: 6931583f-785c-4e27-b5e4-d185d23a54ee
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Object Model

The following table lists the object types that can be manipulated through the various API sets supplied by the Windows Filtering Platform (WFP).



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Object Type</th>
<th>Description</th>
<th>Sample Properties</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Filter</td>
<td>A rule that governs classification. If the conditions are met, the action is invoked. <br/> This is the most complex object exposed by WFP since it ties together all the other object types. <br/></td>
<td><ul>
<li>Array of conditions</li>
<li>Action (Permit, Block, Callout)</li>
<li><a href="filter-weight-assignment">Weight</a></li>
<li>Context</li>
</ul></td>
<td>&quot;Block traffic with a TCP port greater than 1024.&quot; <br/> &quot;Callout to IDS for all traffic that is not secured.&quot;<br/></td>
</tr>
<tr class="even">
<td>Callout</td>
<td>A set of functions that participate in the classification process.<br/> It allows for custom packet processing to be done when certain conditions are met.<br/></td>
<td><ul>
<li>ID</li>
<li>Applicable layer</li>
</ul></td>
<td>The NAT driver<br/></td>
</tr>
<tr class="odd">
<td>Layer</td>
<td>A filter container in the filter engine. <br/> Represents a specific point in network traffic processing where the filter engine is invoked.<br/></td>
<td><ul>
<li>Schema for filters that can be added to the layer</li>
</ul></td>
<td>The Inbound Transport Layer<br/></td>
</tr>
<tr class="even">
<td>Sub-layer</td>
<td>A sub-component of a layer, used in <a href="filter-arbitration">filter arbitration</a>.<br/></td>
<td><ul>
<li>Weight</li>
</ul></td>
<td>The IPsec Tunnel sub-layer<br/></td>
</tr>
<tr class="odd">
<td>Provider</td>
<td>A policy provider that has built a solution on WFP.<br/> It is used solely for management; it does not affect run-time packet processing.<br/></td>
<td><ul>
<li>ID</li>
<li>Service name</li>
</ul></td>
<td>Windows Firewall with Advanced Security<br/> A 3rd-party URL filtering application<br/></td>
</tr>
<tr class="even">
<td>Provider Context</td>
<td>A data blob used by a policy provider to store arbitrary context information. <br/> It is used to pass custom configuration information to a callout.<br/> The most common way to use the context information is to have filters reference a provider context. <br/></td>
<td><ul>
<li>ID</li>
<li>Data blob</li>
</ul></td>
<td>IPsec stores authentication settings in the Base Filtering Engine ( BFE). The &quot;Context&quot; property of a filter indicates the authentication settings to use for the traffic that the filter describes.<br/> The SSL certification selection shim will store certification information in a provider context. <br/></td>
</tr>
</tbody>
</table>



 

The object types exposed by WFP API have consistent semantics. The actions of add, enumerate, subscribe, and so on are similar for all object types.

Each object type is represented by a data structure (for example, [**FWPM\_FILTER0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_filter0_)). In order to minimize the number of different data structures exposed by the WFP API, the same data structure is used for both adding new objects and retrieving existing ones. Thus, there may be fields in each data structure that are ignored when adding a new object since these fields are filled in by the Base Filtering Engine (BFE), and not by the caller. For example, an **FWPM\_FILTER0** data structure has a **filterId** field that contains the **LUID** of the corresponding **FWPS\_FILTER0**. This **LUID** is assigned by BFE, and thus, this field is ignored in the call to [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0).

## Related topics

<dl> <dt>

[Object Management](object-management.md)
</dt> </dl>

 

 





