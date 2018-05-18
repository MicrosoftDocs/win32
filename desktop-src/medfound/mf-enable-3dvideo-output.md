---
Description: 'Specifies how a Media Foundation transform (MFT) should output a 3D stereoscopic video stream.'
ms.assetid: 'AA75A2FB-DEAC-44E9-93E9-4AC2D9F03B39'
title: 'MF\_ENABLE\_3DVIDEO\_OUTPUT attribute'
---

# MF\_ENABLE\_3DVIDEO\_OUTPUT attribute

Specifies how a Media Foundation transform (MFT) should output a 3D stereoscopic video stream.

## Data type

**UINT32**

## Remarks

The value of the attribute is a member of the [**MF3DVideoOutputType**](mf3dvideooutputtype.md) enumeration.

This attribute applies only if the MFT returns **TRUE** for the [MFT\_SUPPORT\_3DVIDEO](mft-support-3dvideo.md) attribute.

To get or set this attribute call [**IMFTransform::GetAttributes**](imftransform-getattributes.md) to get the global attribute store of the MFT.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




