---
description: Specifies whether the Source Reader enables DirectX Video Acceleration (DXVA) on the video decoder.
ms.assetid: ec539038-3fd3-41b7-a0e6-e75e3f2828a7
title: MF_SOURCE_READER_DISABLE_DXVA attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SOURCE\_READER\_DISABLE\_DXVA attribute

Specifies whether the [Source Reader](source-reader.md) enables DirectX Video Acceleration (DXVA) on the video decoder.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute applies if the following conditions are true:

-   The source reader decodes a video stream.
-   The video decoder supports DXVA decoding.
-   The application uses the [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) attribute to set the [Direct3D Device Manager](direct3d-device-manager.md) on the source reader.

This attribute enables the application to disable DXVA while still decoding to Direct3D surfaces.

By default, the source reader uses the [Direct3D Device Manager](direct3d-device-manager.md) for two purposes:

-   To enable DXVA decoding in the video decoder.
-   To allocate Direct3D surfaces for the video samples.

If the value of the MF\_SOURCE\_READER\_DISABLE\_DXVA attribute is **TRUE**, the source reader does disables DXVA decoding, although it still uses the [Direct3D Device Manager](direct3d-device-manager.md) to allocate Direct3D surfaces.

If the [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) attribute is not set, the MF\_SOURCE\_READER\_DISABLE\_DXVA attribute is ignored.

The default value of this attribute is **FALSE**, meaning that DXVA decoding is enabled when available.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




