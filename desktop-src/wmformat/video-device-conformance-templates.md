---
title: Video Device Conformance Templates
description: Video Device Conformance Templates
ms.assetid: 0a91167c-8799-4ce8-a377-c4e613567d0f
keywords:
- Windows Media Format SDK,device conformance templates
- Advanced Systems Format (ASF),device conformance templates
- ASF (Advanced Systems Format),device conformance templates
- Windows Media Format SDK,video device conformance templates
- Advanced Systems Format (ASF),video device conformance templates
- ASF (Advanced Systems Format),video device conformance templates
- Windows Media Video 9 codec,video device conformance templates
- codecs,Windows Media Video 9 codec
- device conformance templates,video
- video device conformance templates
- templates,video device conformance templates
ms.topic: article
ms.date: 05/31/2018
---

# Video Device Conformance Templates

The following tables list the device conformance templates and associated parameters for the Windows Media Video 9 codec.

## Simple Profile, Low Level



| Parameter                                | Value                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------|
| Template string                          | "SP@LL"                                                                               |
| Appropriate devices                      | Wireless handsets (Microsoft Windows-Powered SmartPhone Solution and similar devices) |
| Maximum resolution                       | 176 x 144                                                                             |
| Maximum frame rate                       | 15 fps                                                                                |
| Maximum bit rate                         | 96 Kbps                                                                               |
| Maximum buffer size (in 16384-bit units) | 20 (about 3.4 seconds at maximum bit rate)                                            |
| Interlaced Encoding                      | No                                                                                    |



 

## Simple Profile, Medium Level



| Parameter                                | Value                                                                                |
|------------------------------------------|--------------------------------------------------------------------------------------|
| Template string                          | "SP@ML"                                                                              |
| Appropriate devices                      | Handheld computers and Personal data assistantsHigh-end wireless handsets<br/> |
| Maximum resolution                       | 352 x 288                                                                            |
| Maximum frame rate                       | 15 fps @ 352 x 28824 fps @ 320 x 240<br/>                                      |
| Maximum bit rate                         | 384 Kbps                                                                             |
| Maximum buffer size (in 16384-bit units) | 77 (about 3.3 seconds at maximum bit rate)                                           |
| Interlaced Encoding                      | No                                                                                   |



 

## Generic Simple Profile

A stream that complies with the algorithmic limitations of the simple profile, but does not fit into one of the level specifications, will be assigned "SP" as its device conformance template string.

## Main Profile, Low Level



| Parameter                                | Value                                       |
|------------------------------------------|---------------------------------------------|
| Template string                          | "MP@LL"                                     |
| Appropriate devices                      | Set-top boxes                               |
| Maximum resolution                       | 352 x 288                                   |
| Maximum frame rate                       | 30 fps                                      |
| Maximum bit rate                         | 2 Mbps                                      |
| Maximum buffer size (in 16384-bit units) | 306 (about 2.5 seconds at maximum bit rate) |
| Interlaced Encoding                      | No                                          |



 

## Main Profile, Medium Level



| Parameter                                | Value                                                                                                                  |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Template string                          | "MP@ML"                                                                                                                |
| Appropriate devices                      | Set-top boxesSlower computers using DirectX Video Acceleration<br/> Windows Media enabled DVD players<br/> |
| Maximum resolution                       | 720 x 576                                                                                                              |
| Maximum frame rate                       | 30 fps @ 720 x 48025 fps @ 720 x 576<br/>                                                                        |
| Maximum bit rate                         | 10 Mbps                                                                                                                |
| Maximum buffer size (in 16384-bit units) | 611 (about 1 second at maximum bit rate)                                                                               |
| Interlaced Encoding                      | Yes                                                                                                                    |



 

## Main Profile, High Level



| Parameter                                | Value                                                                                                                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template string                          | "MP@HL"                                                                                                                                                               |
| Appropriate devices                      | Computers using DirectX Video AccelerationHigh-Definition Windows Media enabled DVD players<br/> Digital cinema<br/> high-definition streaming<br/> |
| Maximum resolution                       | 1920 x 1080                                                                                                                                                           |
| Maximum frame rate                       | 30 fps @ 1920 x 108060 fps @ 1280 x 720<br/>                                                                                                                    |
| Maximum bit rate                         | 20 Mbps                                                                                                                                                               |
| Maximum buffer size (in 16384-bit units) | 2442 (about 2.66 seconds at maximum bit rate)                                                                                                                         |
| Interlaced Encoding                      | Yes                                                                                                                                                                   |



 

## Generic Main Profile

A stream that complies with the algorithmic limitations of the main profile, but does not fit into one of the level specifications, will be assigned "MP" as its device conformance template string.

## Complex Profile



| Parameter       | Value                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Template string | "CP"                                                                                                                                   |
| Remarks         | The complex profile has no explicit limitations. It is used to enable all of the codec algorithms, usually for demonstration purposes. |



 

The following tables list the parameters of the device conformance templates for the Windows Media Video 9 Image codec.

## Video Image Level 1



| Parameter                                | Value                                       |
|------------------------------------------|---------------------------------------------|
| Template string                          | "I1"                                        |
| Maximum resolution                       | 352 x 288                                   |
| Maximum frame rate                       | 30 fps                                      |
| Maximum bit rate                         | 192 Kbps                                    |
| Maximum buffer size (in 16384-bit units) | 39 (about 3.26 seconds at maximum bit rate) |
| Interlaced Encoding                      | No                                          |



 

## Video Image Level 2



| Parameter                                | Value                                       |
|------------------------------------------|---------------------------------------------|
| Template string                          | "I2"                                        |
| Maximum resolution                       | 1024 x 768                                  |
| Maximum frame rate                       | 30 fps                                      |
| Maximum bit rate                         | 384 Kbps                                    |
| Maximum buffer size (in 16384-bit units) | 77 (about 3.26 seconds at maximum bit rate) |
| Interlaced Encoding                      | No                                          |



 

## Generic Video Image

A Video Image stream that does not fit into one of the level specifications will be assigned "I" as its device conformance template string.

## Related topics

<dl> <dt>

[**Audio Device Conformance Templates**](audio-device-conformance-templates.md)
</dt> <dt>

[**Device Conformance Template Parameters**](device-conformance-template-parameters.md)
</dt> <dt>

[**Recommended Device Conformance Template Combinations**](recommended-device-conformance-template-combinations.md)
</dt> </dl>

 

 





