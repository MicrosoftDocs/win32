---
Description: 'Sets a pointer to the DXGI Device Manager on the capture engine.'
ms.assetid: '1DFDE7AB-7DFF-4C39-9460-E42E37649AAC'
title: 'MF\_CAPTURE\_ENGINE\_D3D\_MANAGER attribute'
---

# MF\_CAPTURE\_ENGINE\_D3D\_MANAGER attribute

Sets a pointer to the DXGI Device Manager on the capture engine.

## Data type

**IUnknown\***

## Remarks

The value of this attribute is a pointer to the [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) interface. This attribute enables the capture engine to allocate video frames using DXGI surfaces, and to use hardware acceleration for decoding and video processing.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Capture Engine Attributes](capture-engine-attributes.md)
</dt> <dt>

[**IMFCaptureEngine::Initialize**](imfcaptureengine-initialize.md)
</dt> </dl>

 

 




