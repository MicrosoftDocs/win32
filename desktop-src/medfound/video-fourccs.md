---
description: Video FOURCCs
ms.assetid: bea4835d-fd7f-4ac3-8466-7f4e0d799a12
title: Video FOURCCs
ms.topic: article
ms.date: 05/31/2018
---

# Video FOURCCs

Many video formats have FOURCC codes assigned to them. A FOURCC code is a 32-bit unsigned integer that is created by concatenating four ASCII characters. For example, the FOURCC code for YUY2 video is 'YUY2'.

Various C/C++ macros are defined for declaring FOURCC values in source code. The **MAKEFOURCC** macro is defined in Mmsystem.h, and the **FCC** macro is defined in Aviriff.h and various other header files. You can also declare a FOURCC code directly as a string literal simply by reversing the order of the characters. Thus, the following statements are equivalent:

``` syntax
DWORD fccYUY2 = MAKEFOURCC('Y','U','Y','2');
DWORD fccYUY2 = FCC('YUY2');
DWORD fccYUY2 = '2YUY';  // Declares the FOURCC 'YUY2'.
```

(In the last example, reversing the byte order is necessary because Windows uses a little-endian architecture. 'Y' = 0x59, 'U' = 0x55, and '2' = 0x32, so '2YUY' is 0x32595559.)

Some of the [DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md) APIs use a **D3DFORMAT** value to describe a video format. A FOURCC code can be used in this context as well:

``` syntax
D3DFORMAT fmt = (D3DFORMAT)MAKEFOURCC('Y','U','Y','2');
D3DFORMAT fmt = (D3DFORMAT)FCC('YUY2');
D3DFORMAT fmt = D3DFORMAT('2YUY'); // Coerce to D3DFORMAT type.
```

### FOURCC Constants

The following table lists some common FOURCC codes.



| FOURCC value | Description                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| 'H264'       | H.264 video.                                                                                                          |
| 'I420'       | YUV video stored in planar 4:2:0 format.                                                                              |
| 'IYUV'       | YUV video stored in planar 4:2:0 format.                                                                              |
| 'M4S2'       | MPEG-4 part 2 video.                                                                                                  |
| 'MP4S'       | Microsoft MPEG 4 codec version 3. This codec is no longer supported.                                                  |
| 'MP4V'       | MPEG-4 part 2 video.                                                                                                  |
| 'MPG1'       | MPEG-1 video.                                                                                                         |
| 'MSS1'       | Content encoded with the Windows Media Video 7 screen codec.                                                          |
| 'MSS2'       | Content encoded with the Windows Media Video 9 screen codec.                                                          |
| 'UYVY'       | YUV video stored in packed 4:2:2 format. Similar to YUY2 but with different ordering of data.                         |
| 'WMV1'       | Content encoded with the Windows Media Video 7 codec.                                                                 |
| 'WMV2'       | Content encoded with the Windows Media Video 8 codec.                                                                 |
| 'WMV3'       | Content encoded with the Windows Media Video 9 codec.                                                                 |
| 'WMVA'       | Content encoded with the older, obsolete version of the Windows Media Video 9 Advanced Profile codec.                 |
| 'WMVP'       | Content encoded with the Windows Media Video 9.1 Image codec.                                                         |
| 'WVC1'       | SMPTE 421M ("VC-1"). Content encoded with Windows Media Video 9 Advanced Profile.                                     |
| 'WVP2'       | Content encoded with the Windows Media Video 9.1 Image v2 codec.                                                      |
| 'YUY2'       | YUV video stored in packed 4:2:2 format.                                                                              |
| 'YV12'       | YUV video stored in planar 4:2:0 or 4:1:1 format. Identical to I420/IYUV except that the U and V planes are switched. |
| 'YVU9'       | YUV video stored in planar 16:1:1 format.                                                                             |
| 'YVYU'       | YUV video stored in packed 4:2:2 format. Similar to YUY2 but with different ordering of data.                         |



 

## Related topics

<dl> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[Video Subtype GUIDs](video-subtype-guids.md)
</dt> </dl>

 

 



