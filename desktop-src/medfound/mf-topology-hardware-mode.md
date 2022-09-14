---
description: Specifies whether to load hardware-based Microsoft Media Foundation transforms (MFTs) in the topology.
ms.assetid: f7ac3c9b-c163-412f-84c0-27bf551091d8
title: MF_TOPOLOGY_HARDWARE_MODE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPOLOGY\_HARDWARE\_MODE attribute

Specifies whether to load hardware-based Microsoft Media Foundation transforms (MFTs) in the topology.

## Data type

**[**MFTOPOLOGY\_HARDWARE\_MODE**](/windows/desktop/api/mfidl/ne-mfidl-mftopology_hardware_mode)** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology)

## Remarks

This attribute is optional. Set the attribute before resolving the topology.



| Value                                  | Description                                                                                                                                                                                                                                                                       |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MFTOPOLOGY\_HWMODE\_USE\_HARDWARE**  | The Topology Loader will load hardware-based MFTs, such as hardware decoders, when available.<br/> The Topology Loader automatically falls back to software decoding if no hardware decoder is found, or if a hardware decoder fails to connect for some reason.<br/> |
| **MFTOPOLOGY\_HWMODE\_SOFTWARE\_ONLY** | The Topology Loader will load only software MFTs, including software decoders.                                                                                                                                                                                                    |



 

The default value is **MFTOPOLOGY\_HWMODE\_SOFTWARE\_ONLY**, for compatibility with existing applications. The recommended value is **MFTOPOLOGY\_HWMODE\_USE\_HARDWARE**.

If the Topology Loader inserts a hardware MFT into the topology, it sets the [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md) attribute on the topology node. To check whether a hardware MFT is present, enumerate the nodes in the resolved topology and check whether this attribute is present.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




