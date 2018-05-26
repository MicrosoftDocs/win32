---
Description: Specifies the element that contains this source node.
ms.assetid: f5fa5c10-8f30-43bd-8054-a39996f807a3
title: MF\_TOPONODE\_SEQUENCE\_ELEMENTID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_SEQUENCE\_ELEMENTID attribute

Specifies the element that contains this source node.

## Data type

**UINT32**

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**).

The media pipeline uses this attribute to discover when media sources are part of the same element. The pipeline treats all source nodes that are part of the same element as having the same clock.

When the pipeline queues up a new topology that contains source nodes that are part of an element that is present in the previous topology, the pipeline treats these source nodes as having the same clock as the source nodes from that element in the previous topology.

> [!Note]  
> The media pipeline does not correct time stamps for source nodes with different clock rates.

 

A media source that can provide topologies should implement the [**IMFMediaSourceTopologyProvider**](/windows/win32/mfidl/nn-mfidl-imfmediasourcetopologyprovider?branch=master) interface or the [**IMFSequencerSource**](/windows/win32/mfidl/nn-mfidl-imfsequencersource?branch=master) interface. A media source that provides topologies should set the **MF\_TOPONODE\_SEQUENCE\_ELEMENTID** attribute on every source node that it creates.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaSourceTopologyProvider**](/windows/win32/mfidl/nn-mfidl-imfmediasourcetopologyprovider?branch=master)
</dt> <dt>

[**IMFSequencerSource**](/windows/win32/mfidl/nn-mfidl-imfsequencersource?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 




