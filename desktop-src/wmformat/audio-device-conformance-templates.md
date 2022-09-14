---
title: Audio Device Conformance Templates
description: Audio Device Conformance Templates
ms.assetid: dad3dd2c-595e-45ce-bd84-2a20bc656cfb
keywords:
- Windows Media Format SDK,device conformance templates
- Advanced Systems Format (ASF),device conformance templates
- ASF (Advanced Systems Format),device conformance templates
- Windows Media Format SDK,audio device conformance templates
- Advanced Systems Format (ASF),audio device conformance templates
- ASF (Advanced Systems Format),audio device conformance templates
- Windows Media Audio 9 codec,audio device conformance templates
- codecs,Windows Media Audio 9 codec
- device conformance templates,video
- audio device conformance templates
- templates,audio device conformance templates
ms.topic: article
ms.date: 05/31/2018
---

# Audio Device Conformance Templates

The following table lists the device conformance templates and associated parameters for the Windows Media Audio 9 codec, or later.



| Template string | Bit rate range     | Notes                                                                                                                                                                                                                                |
|-----------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "L1"            | 64 Kbps   160 Kbps | This template is intended for constrained audio-only devices.                                                                                                                                                                        |
| "L2"            | <= 160 Kbps     | This template corresponds to Class 4 in the Windows Media Audio porting kit, which supports the entire Windows Media Audio decoder implementation.                                                                                   |
| "L3"            | <= 384 Kbps     | This template corresponds to Class 4 in the Windows Media Audio porting kit, which supports the entire Windows Media Audio decoder implementation.The bit rate range is the only difference between this template and L2.<br/> |
| "L"             | All bit rates      | This template is for use with personal computers only, and is usually used to showcase the full capabilities of the codec.                                                                                                           |



 

The following table lists the device conformance templates and associated parameters for the Windows Media Audio 9 Voice codec.



| Template string | Bit rate range | Notes                                                                                                                      |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------|
| "S1"            | <= 20 Kbps  | This template is intended for very low-complexity devices only.This template is speech only.<br/>                    |
| "S2"            | <= 20 Kbps  | This is the recommended template for most applications.This template supports combinations of speech and music.<br/> |



 

The following table lists the device conformance templates and associated parameters for the Windows Media Audio 9 Professional codec, or later.



| Template string | Properties                                                                                   | Notes                                                                                                                                                                                                                                           |
|-----------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "M1"            | Bit rate <= 384 KbpsSampling rate <= 48 kHz<br/> Channels <= 5.1<br/>   | This template is recommended for standard movies with surround sound.                                                                                                                                                                           |
| "M2"            | Bit rate <= 768 KbpsSampling rate <= 96 kHz<br/> Channels <= 5.1<br/>   | This template is recommended for high-definition movies with surround sound.                                                                                                                                                                    |
| "M3"            | Bit rate <= 1,500 KbpsSampling rate <= 96 kHz<br/> Channels <= 7.1<br/> | This template is recommended for high-definition movies with 8-channel surround sound, such as content encoded for presentation in theaters.                                                                                                    |
| "M"             | All bit ratesAll sampling rates<br/> All channels<br/>                           | This template is for use with personal computers only, and is usually used to showcase the full capabilities of the codec.This is also the template designation for all audio encoded with the Windows Media Audio 9 Lossless codec.<br/> |



 

## Related topics

<dl> <dt>

[**Device Conformance Template Parameters**](device-conformance-template-parameters.md)
</dt> <dt>

[**Recommended Device Conformance Template Combinations**](recommended-device-conformance-template-combinations.md)
</dt> <dt>

[**Video Device Conformance Templates**](video-device-conformance-templates.md)
</dt> </dl>

 

 





