---
description: Specifies the name of the video renderer effect app service with which a communication channel should be opened.
title: MF_VIDEO_RENDERER_EFFECT_APP_SERVICE_NAME attribute (Mfapi.h)
ms.topic: reference
ms.date: 09/10/2025
---

# MF\_VIDEO\_RENDERER\_EFFECT\_APP\_SERVICE\_NAME attribute

Specifies the name of the video renderer effect app service with which a communication channel will be opened.

## Data type

**String**

## Remarks

A video renderer effect sets this attribute to the name of the app service to connect to. The app service name is defined in the AppX manifest of the package that contains the video renderer effect. When this property is set, the platform will asynchronously call the app service's implementation of [IMFVideoRendererEffectControl::OnAppServiceConnectionEstablished](/windows/win32/api/mfidl/nf-mfidl-imfvideorenderereffectcontrol-onappserviceconnectionestablished), passing an **IUnknown** representing the app service communication channel.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 version 1803                                |
| Minimum supported server<br/> | Windows Server version 1803                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
