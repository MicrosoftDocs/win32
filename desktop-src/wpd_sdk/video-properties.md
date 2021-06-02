---
description: Windows Portable Devices supports the following video properties.
ms.assetid: e6df5b2d-ceb8-4de0-b60b-9102c77143fe
title: Video Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Video
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Video Properties

Windows Portable Devices supports the following video properties.



| Property                                         | VarType        | Description                                                                                                                                                                                                                                             |
|--------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_VIDEO\_AUTHOR**                           | **VT\_LPWSTR** | The author of the video file.                                                                                                                                                                                                                           |
| **WPD\_VIDEO\_BITRATE**                          | **VT\_UI4**    | The bit rate of the video file.                                                                                                                                                                                                                         |
| **WPD\_VIDEO\_BUFFER\_SIZE**                     | **VT\_UI4**    | A value that specifies the required video buffer size to render this file.                                                                                                                                                                              |
| **WPD\_VIDEO\_CREDITS**                          | **VT\_LPWSTR** | The credits listing the cast and crew for the video.                                                                                                                                                                                                    |
| **WPD\_VIDEO\_FOURCC\_CODE**                     | **VT\_DWORD**  | The registered FourCC code that indicates the codec that was used for the video file. For a listing of FourCC formats, see the article [Registered FOURCC Codes and WAVE Formats](https://msdn2.microsoft.com/library/ms867195.aspx) on the MSDN Web site. |
| **WPD\_VIDEO\_FRAMERATE**                        | **VT\_UI4**    | The frame rate of the video file, in frames/second x 1,000. For example, a frame rate of 29.97 is represented as 29970.                                                                                                                                 |
| **WPD\_VIDEO\_GENRE**                            | **VT\_LPWSTR** | The genre of this video file. There are no standard genre definitions.                                                                                                                                                                                  |
| **WPD\_VIDEO\_KEY\_FRAME\_DISTANCE**             | **VT\_UI4**    | The interval between key frames, in milliseconds.                                                                                                                                                                                                       |
| **WPD\_VIDEO\_QUALITY\_SETTING**                 | **VT\_UI4**    | The quality setting for the video file. This is codec-dependent.                                                                                                                                                                                        |
| **WPD\_VIDEO\_RECORDEDTV\_CHANNEL\_NUMBER**      | **VT\_UI4**    | The television channel number the video was recorded from.                                                                                                                                                                                              |
| **WPD\_VIDEO\_RECORDEDTV\_PROGRAM\_DESCRIPTION** | **VT\_LPWSTR** | A description of the recorded television program.                                                                                                                                                                                                       |
| **WPD\_VIDEO\_RECORDEDTV\_REPEAT**               | **VT\_BOOL**   | A Boolean value that specifies whether the television program was a repeat showing.                                                                                                                                                                     |
| **WPD\_VIDEO\_RECORDEDTV\_STATION\_NAME**        | **VT\_LPWSTR** | The television station that the video was recorded from.                                                                                                                                                                                                |
| **WPD\_VIDEO\_SCAN\_TYPE**                       | **VT\_UI4**    | A [**WPD\_VIDEO\_SCAN\_TYPES**](wpd-video-scan-types.md) enumerator that specifies the interlacing of the video file.                                                                                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




