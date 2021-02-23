---
description: Specifies whether the topology loader enables the Transcode Video Processor (XVP). for conversions, enabling hardware accelerated color conversion.
title: MF_TOPOLOGY_ENABLE_XVP_FOR_PLAYBACK attribute (Mfidl.h)
ms.topic: reference
ms.date: 02/22/2021
---

# MF\_TOPOLOGY\_ENABLE\_XVP\_FOR\_PLAYBACK attribute

Specifies whether the topology loader enables the Transcode Video Processor (XVP). for conversions, enabling hardware accelerated color conversion.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology)

## Remarks

If this attribute is set, the topology loader will pull in the video processor, if necessary, during non-transcode topology resolution. When you are using the topology to build your own [IMFTopology](/windows/win32/api/mfidl/nn-mfidl-imftopology) this attribute tells the loader to use XVP for conversions instead of the legacy color converter, thus enabling hardware accelerated color conversion; the legacy color converter is software-only.

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

[Direct3D Device Manager](direct3d-device-manager.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




