---
Description: Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology.
ms.assetid: 03783ef3-f957-41e3-9734-94cb34ecc088
title: MF\_TOPOLOGY\_DXVA\_MODE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_DXVA\_MODE attribute

Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology.

## Data type

**[**MFTOPOLOGY\_DXVA\_MODE**](/windows/win32/mfidl/ne-mfidl-mftopology_dxva_mode?branch=master)** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)

## Remarks

The value of this attribute is an [**MFTOPOLOGY\_DXVA\_MODE**](/windows/win32/mfidl/ne-mfidl-mftopology_dxva_mode?branch=master) enumeration constant. The default value is **MFTOPOLOGY\_DXVA\_DEFAULT**.

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

 

 




