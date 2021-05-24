---
description: Specifies the app package family name for a virtual camera configuration application.
title: MF_VIRTUALCAMERA_APP_PACKAGE_FAMILY_NAME attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/24/2021
---

# MF\_VIRTUALCAMERA\_APP\_PACKAGE\_FAMILY\_NAME attribute

Specifies the app package family name for a virtual camera configuration application. When provided, the pipeline will associate the configuration application with the virtual camera and provide a launch point within the Camera Settings page.

## Data type

[MF_ATTRIBUTE_STRING](/windows/win32/api/mfobjects/ne-mfobjects-mf_attribute_type)

## Remarks

This attribute may be exposed by the virtual camera custom media source from the media source attribute store [IMFMediaSourceEx::GetSourceAttributes](/windows/win32/api/mfvirtualcamera/nf-mfvirtualcamera-imfvirtualcamera-getmediasource).  

If the configuration application is not yet installed on the machine, the Store application will be launched and navigated to the application page specified by the package family name. Otherwise, the installed application will be launched for the user.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | TBD<br/>                          |
| Minimum supported server<br/> | TBD<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> 
</dl>
 




