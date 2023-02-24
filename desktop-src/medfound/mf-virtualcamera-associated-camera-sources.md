---
description: Contains an IMFCollection object containing the IMFMediaSourceEx representing the physical cameras associated with a virtual camera.
title: MF_VIRTUALCAMERA_ASSOCIATED_CAMERA_SOURCES attribute (Mfvirtualcamera.h)
ms.topic: reference
ms.date: 05/09/2022
---

# MF\_VIRTUALCAMERA\_ASSOCIATED\_CAMERA\_SOURCES attribute

Contains an [IMFCollection](/windows/win32/api/mfobjects/nn-mfobjects-imfcollection) object containing the [IMFMediaSourceEx](/windows/win32/api/mfidl/nn-mfidl-imfmediasourceex) representing the physical cameras associated with a virtual camera. 


## Data type

**IMFCollection** stored as **IUnknown**.

## Remarks

Request for platform to populate this attribute by setting the [MF_VIRTUALCAMERA_PROVIDE_ASSOCIATED_CAMERA_SOURCES](mf-virtualcamera-provide-associated-camera-sources.md) attribute to a non-zero value.

The platform will set this attribute on the [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate) associated with the virtual camera prior to calling the [IMFActivate::ActivateObject](/windows/win32/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method.

The resulting **IMFCollection** can be empty if the associated cameras are no longer present. Virtual camera implementations should handle this scenario gracefully by providing feedback to the end user that the associated camera is not available such as displaying a fixed “video frame".



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

[**IMFAttributes::GetUnknown**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown)
</dt> 
</dl>
 




