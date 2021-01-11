---
description: Width and height of a video frame, in pixels.
ms.assetid: 9f10a972-406f-47ef-b71c-86ed771c9a9a
title: MF_MT_FRAME_SIZE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_FRAME\_SIZE attribute

Width and height of a video frame, in pixels.

## Data type

**UINT64**

## Remarks

The upper 32 bits contain the width and the lower 32 bits contain the height.

To set this attribute, use the [**MFSetAttributeSize**](/windows/desktop/api/mfapi/nf-mfapi-mfsetattributesize) function. To get this attribute, use the [**MFGetAttributeSize**](/windows/desktop/api/mfapi/nf-mfapi-mfgetattributesize) function.

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples


```
// Helper function to set the frame size on a video media type.
inline HRESULT SetFrameSize(IMFMediaType *pType, UINT32 width, UINT32 height)
{
    return MFSetAttributeSize(pType, MF_MT_FRAME_SIZE, width, height);
}

// Helper function to get the frame size from a video media type.
inline HRESULT GetFrameSize(IMFMediaType *pType, UINT32 *pWidth, UINT32 *pHeight)
{
    return MFGetAttributeSize(pType, MF_MT_FRAME_SIZE, pWidth, pHeight);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




