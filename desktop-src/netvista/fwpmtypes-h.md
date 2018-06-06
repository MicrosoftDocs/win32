---
Description: This section contains kernel mode network driver reference topics for the Fwpmtypes.h header.
ms.assetid: 3BC4BB93-964C-42C7-9E06-213CB18122F0
title: Fwpmtypes.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fwpmtypes.h

This section contains kernel mode network driver reference topics for the Fwpmtypes.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Fwpstypes.h header contains definitions for management portion of the FWP APIs.

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
<td>[<strong>FWPM_CALLOUT0</strong>](/windows/desktop/api/fwpmtypes/)<br/></td>
<td>The [<strong>FWPM_CALLOUT0</strong>](/windows/desktop/api/fwpmtypes/) structure defines the data that is required for a callout driver to add a callout to the filter engine.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPM_CALLOUT0</strong>](/windows/desktop/api/fwpmtypes/) is a specific version of <strong>FWPM_CALLOUT</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPM_SESSION0</strong>](/windows/desktop/api/fwpmtypes/)<br/></td>
<td>The [<strong>FWPM_SESSION0</strong>](/windows/desktop/api/fwpmtypes/) structure defines session-specific parameters for an open session to the filter engine.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPM_SESSION0</strong>](/windows/desktop/api/fwpmtypes/) is a specific version of <strong>FWPM_SESSION</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FWPM_CLASSIFY_OPTION0</strong>](/windows/desktop/api/fwpmtypes/)<br/></td>
<td>The [<strong>FWPM_CLASSIFY_OPTION0</strong>](/windows/desktop/api/fwpmtypes/) structure can be used to define unicast and multicast time-out options and data for a non-TCP state.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPM_CLASSIFY_OPTION0</strong>](/windows/desktop/api/fwpmtypes/) is a specific version of <strong>FWPM_CLASSIFY_OPTION</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>FWPM_CLASSIFY_OPTIONS0</strong>](/windows/desktop/api/fwpmtypes/)<br/></td>
<td>The [<strong>FWPM_CLASSIFY_OPTIONS0</strong>](/windows/desktop/api/fwpmtypes/) structure can be used to define multiple time-out options and data for use with the [<strong>FwpsClassifyOptionSet0</strong>](/windows-hardware/drivers/ddi/content/fwpsk/nf-fwpsk-fwpsclassifyoptionset0) function.<br/>
<blockquote>
[!Note]<br />
[<strong>FWPM_CLASSIFY_OPTIONS0</strong>](/windows/desktop/api/fwpmtypes/) is a specific version of <strong>FWPM_CLASSIFY_OPTIONS</strong>. See [WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670) for more information.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Fwpmtypes.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




