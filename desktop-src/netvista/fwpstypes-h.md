---
Description: This section contains kernel mode network driver reference topics for the Fwpstypes.h header.
ms.assetid: 765B7BBB-A7D6-4B94-98FA-4E352BE5B238
title: Fwpstypes.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fwpstypes.h

This section contains kernel mode network driver reference topics for the Fwpstypes.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Fwpstypes.h header contains definitions for system portion of the FWP APIs.

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
<td>[<strong>FWPS_ACTION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_action0_)<br/></td>
<td>The [<strong>FWPS_ACTION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_action0_) structure specifies the run-time action that the filter engine takes if all of the filter's filtering conditions are true.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_ACTION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_action0_) is a specific version of <strong>FWPS_ACTION</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_ALE_ENDPOINT_ENUM_TEMPLATE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_enum_template0_)<br/></td>
<td>The [<strong>FWPS_ALE_ENDPOINT_ENUM_TEMPLATE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_enum_template0_) structure specifies a template for application layer enforcement (ALE) endpoints to be enumerated.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_ALE_ENDPOINT_ENUM_TEMPLATE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_enum_template0_) is a specific version of <strong>FWPS_ALE_ENDPOINT_ENUM_TEMPLATE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_ALE_ENDPOINT_PROPERTIES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_properties0_)<br/></td>
<td>The [<strong>FWPS_ALE_ENDPOINT_PROPERTIES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_properties0_) structure specifies the properties of an application layer enforcement (ALE) endpoint.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_ALE_ENDPOINT_PROPERTIES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_ale_endpoint_properties0_) is a specific version of <strong>FWPS_ALE_ENDPOINT_PROPERTIES</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_FILTER0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter0_)<br/></td>
<td>The [<strong>FWPS_FILTER0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter0_) structure defines a run-time filter in the filter engine.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_FILTER0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter0_) is the specific version of <strong>FWPS_FILTER</strong> used in Windows Vista and later. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information. For Windows 8, [<strong>FWPS_FILTER2</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter2_) is available. For Windows 7, [<strong>FWPS_FILTER1</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_) is available.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_FILTER1</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_)<br/></td>
<td>The [<strong>FWPS_FILTER1</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_) structure defines a run-time filter in the filter engine.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_FILTER1</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_) is the specific version of <strong>FWPS_FILTER</strong> used in Windows 7 and later. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information. For Windows 8, [<strong>FWPS_FILTER2</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter2_) is available. For Windows Vista, [<strong>FWPS_FILTER0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter0_) is available.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_FILTER2</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter2_)<br/></td>
<td>The [<strong>FWPS_FILTER2</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter2_) structure defines a run-time filter in the filter engine.
<blockquote>
[!Note]<br />
[<strong>FWPS_FILTER2</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter2_) is the specific version of <strong>FWPS_FILTER</strong> used in Windows 8 and later. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information. For Windows 7, [<strong>FWPS_FILTER1</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter1_) is available. For Windows Vista, [<strong>FWPS_FILTER0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter0_) is available.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_FILTER_CONDITION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter_condition0_)<br/></td>
<td>The [<strong>FWPS_FILTER_CONDITION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter_condition0_) structure defines a run-time filtering condition for a filter.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_FILTER_CONDITION0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_filter_condition0_) is a specific version of <strong>FWPS_FILTER_CONDITION</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_DISCARD_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_discard_metadata0_)<br/></td>
<td>The [<strong>FWPS_DISCARD_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_discard_metadata0_) structure describes the data that was discarded by the filter engine, a network layer, or a transport layer.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_DISCARD_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_discard_metadata0_) is a specific version of <strong>FWPS_DISCARD_METADATA</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_INBOUND_FRAGMENT_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_inbound_fragment_metadata0_)<br/></td>
<td>The [<strong>FWPS_INBOUND_FRAGMENT_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_inbound_fragment_metadata0_) structure describes the fragment data for a received packet fragment.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_INBOUND_FRAGMENT_METADATA0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_inbound_fragment_metadata0_) is a specific version of <strong>FWPS_INBOUND_FRAGMENT_METADATA</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_INCOMING_VALUE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_value0_)<br/></td>
<td>The [<strong>FWPS_INCOMING_VALUE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_value0_) structure defines an individual data value.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_INCOMING_VALUE0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_value0_) is a specific version of <strong>FWPS_INCOMING_VALUE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_INCOMING_VALUES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_values0_)<br/></td>
<td>The [<strong>FWPS_INCOMING_VALUES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_values0_) structure defines data values that are passed by the filter engine to a callout's [<em>classifyFn</em>](/windows-hardware/drivers/ddi/content/Fwpsk/nc-fwpsk-fwps_callout_classify_fn0) callout function.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_INCOMING_VALUES0</strong>](/windows/desktop/api/fwpstypes/ns-fwpstypes-fwps_incoming_values0_) is a specific version of <strong>FWPS_INCOMING_VALUES</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPS_DISCARD_MODULE0</strong>](/windows/desktop/api/fwpstypes/ne-fwpstypes-fwps_discard_module0_)<br/></td>
<td>The [<strong>FWPS_DISCARD_MODULE0</strong>](/windows/desktop/api/fwpstypes/ne-fwpstypes-fwps_discard_module0_) enumeration type specifies the type of module that discarded the data.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_DISCARD_MODULE0</strong>](/windows/desktop/api/fwpstypes/ne-fwpstypes-fwps_discard_module0_) is a specific version of <strong>FWPS_DISCARD_MODULE</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPS_CLASSIFY_OUT0</strong>](/windows/desktop/api/Fwpstypes/ns-fwpstypes-fwps_classify_out0_)<br/></td>
<td>The [<strong>FWPS_CLASSIFY_OUT0</strong>](/windows/desktop/api/Fwpstypes/ns-fwpstypes-fwps_classify_out0_) structure defines the data that is returned to the caller of a callout's [classifyFn](https://www.bing.com/search?q=classifyFn) callout function.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPS_CLASSIFY_OUT0</strong>](/windows/desktop/api/Fwpstypes/ns-fwpstypes-fwps_classify_out0_) is a specific version of <strong>FWPS_CLASSIFY_OUT</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Fwpstypes.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




