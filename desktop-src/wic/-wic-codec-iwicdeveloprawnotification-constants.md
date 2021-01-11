---
description: Flags used to by IWICDevelopRawNotificationCallback to indicate which members have changed.
ms.assetid: 4e94b4f4-abd9-4395-87ec-a08e49a2cf88
title: IWICDevelopRawNotificationCallback Constants (Wincodec.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IWICDevelopRawNotificationCallback Constants

Flags used to by [**IWICDevelopRawNotificationCallback**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdeveloprawnotificationcallback) to indicate which members have changed.



| Constant/value                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| <span id="WICRawChangeNotification_ExposureCompensation"></span><span id="wicrawchangenotification_exposurecompensation"></span><span id="WICRAWCHANGENOTIFICATION_EXPOSURECOMPENSATION"></span><dl> <dt>**WICRawChangeNotification\_ExposureCompensation**</dt> <dt>0x00000001</dt> </dl>             | Mask used to report a exposure compensation change.<br/>                                                       |
| <span id="WICRawChangeNotification_NamedWhitePoint"></span><span id="wicrawchangenotification_namedwhitepoint"></span><span id="WICRAWCHANGENOTIFICATION_NAMEDWHITEPOINT"></span><dl> <dt>**WICRawChangeNotification\_NamedWhitePoint**</dt> <dt>0x00000002</dt> </dl>                                 | Mask used to report a [**WICNamedWhitePoint**](/windows/desktop/api/Wincodec/ne-wincodec-wicnamedwhitepoint) change.<br/>                 |
| <span id="WICRawChangeNotification_KelvinWhitePoint"></span><span id="wicrawchangenotification_kelvinwhitepoint"></span><span id="WICRAWCHANGENOTIFICATION_KELVINWHITEPOINT"></span><dl> <dt>**WICRawChangeNotification\_KelvinWhitePoint**</dt> <dt>0x00000004</dt> </dl>                             | Mask used to report a kelvin white point change.<br/>                                                          |
| <span id="WICRawChangeNotification_RGBWhitePoint"></span><span id="wicrawchangenotification_rgbwhitepoint"></span><span id="WICRAWCHANGENOTIFICATION_RGBWHITEPOINT"></span><dl> <dt>**WICRawChangeNotification\_RGBWhitePoint**</dt> <dt>0x00000008</dt> </dl>                                         | Mask used to report a RGB white point change.<br/>                                                             |
| <span id="WICRawChangeNotification_Contrast"></span><span id="wicrawchangenotification_contrast"></span><span id="WICRAWCHANGENOTIFICATION_CONTRAST"></span><dl> <dt>**WICRawChangeNotification\_Contrast**</dt> <dt>0x00000010</dt> </dl>                                                             | Mask used to report a contrast change.<br/>                                                                    |
| <span id="WICRawChangeNotification_Gamma"></span><span id="wicrawchangenotification_gamma"></span><span id="WICRAWCHANGENOTIFICATION_GAMMA"></span><dl> <dt>**WICRawChangeNotification\_Gamma**</dt> <dt>0x00000020</dt> </dl>                                                                         | Mask used to report a gamma change.<br/>                                                                       |
| <span id="WICRawChangeNotification_Sharpness"></span><span id="wicrawchangenotification_sharpness"></span><span id="WICRAWCHANGENOTIFICATION_SHARPNESS"></span><dl> <dt>**WICRawChangeNotification\_Sharpness**</dt> <dt>0x00000040</dt> </dl>                                                         | Mask used to report a sharpness change.<br/>                                                                   |
| <span id="WICRawChangeNotification_Saturation"></span><span id="wicrawchangenotification_saturation"></span><span id="WICRAWCHANGENOTIFICATION_SATURATION"></span><dl> <dt>**WICRawChangeNotification\_Saturation**</dt> <dt>0x00000080</dt> </dl>                                                     | Mask used to report a saturation change.<br/>                                                                  |
| <span id="WICRawChangeNotification_Tint"></span><span id="wicrawchangenotification_tint"></span><span id="WICRAWCHANGENOTIFICATION_TINT"></span><dl> <dt>**WICRawChangeNotification\_Tint**</dt> <dt>0x00000100</dt> </dl>                                                                             | Mask used to report a tint change.<br/>                                                                        |
| <span id="WICRawChangeNotification_NoiseReduction"></span><span id="wicrawchangenotification_noisereduction"></span><span id="WICRAWCHANGENOTIFICATION_NOISEREDUCTION"></span><dl> <dt>**WICRawChangeNotification\_NoiseReduction**</dt> <dt>0x00000200</dt> </dl>                                     | Mask used to report a noise reduction change.<br/>                                                             |
| <span id="WICRawChangeNotification_DestinationColorContext"></span><span id="wicrawchangenotification_destinationcolorcontext"></span><span id="WICRAWCHANGENOTIFICATION_DESTINATIONCOLORCONTEXT"></span><dl> <dt>**WICRawChangeNotification\_DestinationColorContext**</dt> <dt>0x00000400</dt> </dl> | Mask used to report a destination color context change.<br/>                                                   |
| <span id="WICRawChangeNotification_ToneCurve"></span><span id="wicrawchangenotification_tonecurve"></span><span id="WICRAWCHANGENOTIFICATION_TONECURVE"></span><dl> <dt>**WICRawChangeNotification\_ToneCurve**</dt> <dt>0x00000800</dt> </dl>                                                         | Mask used to report a tone curve change.<br/>                                                                  |
| <span id="WICRawChangeNotification_Rotation"></span><span id="wicrawchangenotification_rotation"></span><span id="WICRAWCHANGENOTIFICATION_ROTATION"></span><dl> <dt>**WICRawChangeNotification\_Rotation**</dt> <dt>0x00001000</dt> </dl>                                                             | Mask used to report a [**WICRawRotationCapabilities**](/windows/desktop/api/Wincodec/ne-wincodec-wicrawrotationcapabilities) change.<br/> |
| <span id="WICRawChangeNotification_RenderMode"></span><span id="wicrawchangenotification_rendermode"></span><span id="WICRAWCHANGENOTIFICATION_RENDERMODE"></span><dl> <dt>**WICRawChangeNotification\_RenderMode**</dt> <dt>0x00002000</dt> </dl>                                                     | Mask used to report a [**WICRawRenderMode**](/windows/desktop/api/Wincodec/ne-wincodec-wicrawrendermode) change.<br/>                     |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincodec.h</dt> </dl> |



## See also

<dl> <dt>

[**IWICDevelopRawNotificationCallback**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdeveloprawnotificationcallback)
</dt> </dl>

 

 




