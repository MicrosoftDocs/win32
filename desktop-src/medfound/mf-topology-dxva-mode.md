---
Description: 'Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology.'
ms.assetid: '03783ef3-f957-41e3-9734-94cb34ecc088'
title: 'MF\_TOPOLOGY\_DXVA\_MODE attribute'
---

# MF\_TOPOLOGY\_DXVA\_MODE attribute

Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology.

## Data type

**[**MFTOPOLOGY\_DXVA\_MODE**](mftopology-dxva-mode.md)** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Applies to

[**IMFTopology**](imftopology.md)

## Remarks

The value of this attribute is an [**MFTOPOLOGY\_DXVA\_MODE**](mftopology-dxva-mode.md) enumeration constant. The default value is **MFTOPOLOGY\_DXVA\_DEFAULT**.

This attribute controls which MFTs receive a pointer to the Direct3D device manager. To enable full video acceleration, set the value to **MFTOPOLOGY\_DXVA\_FULL**. The value **MFTOPOLOGY\_DXVA\_DEFAULT** is defined for backward compatibility; it matches the behavior of all earlier versions of Microsoft Media Foundation.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

 

 




