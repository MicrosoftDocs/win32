---
Description: This section contains kernel mode network driver reference topics for the Fwptypes.h header.
ms.assetid: 8D441EE7-C902-4734-8C59-223CF9F764B4
title: Fwptypes.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fwptypes.h

This section contains kernel mode network driver reference topics for the Fwptypes.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Fwptypes.h header contains definitions for FWP APIs.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>FWP_BYTE_ARRAY16</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_BYTE_ARRAY16 structure defines an array of 16 bytes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_BYTE_BLOB</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_BYTE_BLOB structure defines a binary large object (BLOB).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_CONDITION_VALUE0</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The [<strong>FWP_CONDITION_VALUE0</strong>](/windows/desktop/api/fwptypes/) structure defines a condition value that is used by the filter engine when testing a data field against a filtering condition.<br/>
<blockquote>
[!Note]<br />
[<strong>FWP_CONDITION_VALUE0</strong>](/windows/desktop/api/fwptypes/) is a specific version of <strong>FWP_CONDITION_VALUE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_RANGE0</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The [<strong>FWP_RANGE0</strong>](/windows/desktop/api/fwptypes/) structure defines a range of values.<br/>
<blockquote>
[!Note]<br />
[<strong>FWP_RANGE0</strong>](/windows/desktop/api/fwptypes/) is a specific version of <strong>FWP_RANGE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_TOKEN_INFORMATION</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The [<strong>FWP_TOKEN_INFORMATION</strong>](/windows/desktop/api/fwptypes/) structure defines a set of security identifiers that are used for user-mode classification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_V4_ADDR_AND_MASK</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_V4_ADDR_AND_MASK structure defines the address and subnet mask for an IPv4 Internet address.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_V6_ADDR_AND_MASK</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_V6_ADDR_AND_MASK structure defines the address and subnet mask for an IPv6 Internet address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_VALUE0</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The [<strong>FWP_VALUE0</strong>](/windows/desktop/api/fwptypes/) structure defines a data value that can be one of a number of different data types.<br/>
<blockquote>
[!Note]<br />
[<strong>FWP_VALUE0</strong>](/windows/desktop/api/fwptypes/) is a specific version of <strong>FWP_VALUE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPM_DISPLAY_DATA0</strong>](/windows/desktop/api/Fwptypes/)<br/></td>
<td>The [<strong>FWPM_DISPLAY_DATA0</strong>](/windows/desktop/api/Fwptypes/) structure specifies a name and description for a layer, a filter, a provider, a provider context, a callout, or an open session.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPM_DISPLAY_DATA0</strong>](/windows/desktop/api/Fwptypes/) is a specific version of <strong>FWPM_DISPLAY_DATA</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>LUID</strong>](/windows-hardware/drivers/ddi/content/igpupvdev/)<br/></td>
<td>The locally unique identifier (LUID) is a 64-bit value guaranteed to be unique only on the system on which it was generated. The uniqueness of an LUID is guaranteed only until the system is restarted. <br/> An LUID is not for direct manipulation. Drivers must use support routines and structures to manipulate LUID values.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_CLASSIFY_OPTION_TYPE</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_CLASSIFY_OPTION_TYPE enumeration type specifies time-out options for unicast, multicast, and loose source mapping states and enables blocking or permission of state creation on outbound multicast and broadcast traffic.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_DATA_TYPE</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_DATA_TYPE enumeration type specifies a type of data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_DIRECTION</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_DIRECTION enumeration type specifies the direction of network traffic.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_FILTER_ENUM_TYPE</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_FILTER_ENUM_TYPE enumeration type specifies how the filter enumeration conditions should be interpreted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWP_IP_VERSION</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_IP_VERSION enumeration type specifies the Internet Protocol (IP) version.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWP_MATCH_TYPE</strong>](/windows/desktop/api/fwptypes/)<br/></td>
<td>The FWP_MATCH_TYPE enumeration type specifies the type of match that a filter should use to test for a particular condition.<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Fwptypes.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




