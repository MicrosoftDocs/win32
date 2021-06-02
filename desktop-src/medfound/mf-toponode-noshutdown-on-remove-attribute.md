---
description: Specifies how the Media Session shuts down an object in the topology.
ms.assetid: 53b4faba-860f-4d6c-a145-09ea4ae63b8b
title: MF_TOPONODE_NOSHUTDOWN_ON_REMOVE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_NOSHUTDOWN\_ON\_REMOVE attribute

Specifies how the Media Session shuts down an object in the topology.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to the following types of toplogy node:

-   Output nodes
-   Any transform node that contains an *asynchronous* Media Foundation transform (MFT).

The attribute can have the following values:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TRUE</strong></td>
<td>When the Media Session switches to a new topology or clears the current topology, it does not shut down the object that belongs to this topology node.</td>
</tr>
<tr class="even">
<td><strong>FALSE</strong></td>
<td>When the Media Session switches to a new topology or clears the current topology, it shuts down the node object, as follows:
<ul>
<li>Output nodes: The session calls <a href="/windows/desktop/api/mfidl/nf-mfidl-imfmediasink-shutdown"><strong>IMFMediaSink::Shutdown</strong></a> on the media sink.</li>
<li>Transform nodes: The session calls <a href="/windows/desktop/api/mfidl/nf-mfidl-imfshutdown-shutdown"><strong>IMFShutdown::Shutdown</strong></a> on the MFT.</li>
</ul></td>
</tr>
</tbody>
</table>



 

The default value is **TRUE**.

If your application queues multiple topologies, it is a good idea to set this attribute to **FALSE**. Otherwise, objects in the topology might not be shut down correctly.

This attribute does not apply when the application shuts down the Media Session by calling [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown). When the Media Session shuts down, it always shuts down the media sinks and asynchronous MFTs in the current topology.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> </dl>

 

 




