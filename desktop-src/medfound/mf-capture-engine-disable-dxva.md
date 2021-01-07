---
description: Specifies whether the capture engine uses DirectX Video Acceleration (DXVA) for video decoding.
ms.assetid: 9F677E6E-0DCD-456F-8A00-1C11011BAA13
title: MF_CAPTURE_ENGINE_DISABLE_DXVA attribute (Mfcaptureengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_CAPTURE\_ENGINE\_DISABLE\_DXVA attribute

Specifies whether the capture engine uses DirectX Video Acceleration (DXVA) for video decoding.

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute applies if the following conditions are true:

-   The capture engine decodes a compressed video stream from the capture device (for example, if the capture device outputs H.264 video).
-   The video decoder supports hardware-accelerated decoding using DXVA.
-   The application uses the [MF\_CAPTURE\_ENGINE\_D3D\_MANAGER](mf-capture-engine-d3d-manager.md) attribute to set the DXGI Device Manager on the capture engine.

Otherwise, this attribute is ignored.

This attribute enables the application to disable DXVA while still decoding to Direct3D surfaces.

The default value of this attribute is **FALSE**, meaning that DXVA decoding is enabled when available.

## Requirements



| Requirement | Value |
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

[**IMFCaptureEngine::Initialize**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize)
</dt> </dl>

 

 




