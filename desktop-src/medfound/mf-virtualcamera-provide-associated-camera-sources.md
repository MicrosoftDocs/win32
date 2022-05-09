---
description: Specifies that the pipeline should provide the list of physical camera sources associated with a virtual camera.
title: MF_VIRTUALCAMERA_PROVIDE_ASSOCIATED_CAMERA_SOURCES attribute (Mfvirtualcamera.h)
ms.topic: reference
ms.date: 05/24/2021
---

# MF\_VIRTUALCAMERA\_PROVIDE\_ASSOCIATED\_CAMERA\_SOURCES attribute

Specifies that the pipeline should provide the list of physical camera sources associated with a virtual camera.


## Data type

**UINT32**

## Remarks

Setting this attribute to a non-zero value to requests that the platform provide a list of physical camera sources associated with a virtual camera. The platform will set the [MF_VIRTUALCAMERA_ASSOCIATED_CAMERA_SOURCES](mf-virtualcamera-associated-camera-sources.md) attribute on the [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate) associated with the virtual camera prior to calling the [IMFActivate::ActivateObject](/windows/win32/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method.

If this value is zero or not set, the **MF_VIRTUALCAMERA_ASSOCIATED_CAMERA_SOURCES** will not be set.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                          |
| Minimum supported server<br/> | Windows 11<br/>                      |
| Header<br/>                   | <dl> <dt>Mfvirtualcamera.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> 
</dl>
 




