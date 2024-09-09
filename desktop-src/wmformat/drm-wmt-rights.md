---
title: WMT_RIGHTS enumeration (Wmdrmsdk.h)
description: Defines the rights that may be specified in a DRM license.
ms.assetid: 9c034ca0-83e9-4a4c-8e98-96e2a95fd97c
keywords:
- WMT_RIGHTS enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- WMT_RIGHTS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMT\_RIGHTS enumeration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WMT\_RIGHTS** enumeration type defines the rights that may be specified in a DRM license.

## Syntax


```C++
typedef enum WMT_RIGHTS { 
  WMT_RIGHT_PLAYBACK                 = 0x00000001,
  WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE  = 0x00000002,
  WMT_RIGHT_COPY_TO_CD               = 0x00000008,
  WMT_RIGHT_COPY_TO_SDMI_DEVICE      = 0x00000010,
  WMT_RIGHT_ONE_TIME                 = 0x00000020,
  WMT_RIGHT_SAVE_STREAM_PROTECTED    = 0x00000040,
  WMT_RIGHT_COPY                     = 0x00000080,
  WMT_RIGHT_COLLABORATIVE_PLAY       = 0x00000100,
  WMT_RIGHT_SDMI_TRIGGER             = 0x00010000,
  WMT_RIGHT_SDMI_NOMORECOPIES        = 0x00020000
} ;
```



## Constants

<dl> <dt>

<span id="WMT_RIGHT_PLAYBACK"></span><span id="wmt_right_playback"></span>**WMT\_RIGHT\_PLAYBACK**
</dt> <dd>

Specifies the right to play content without restriction.

</dd> <dt>

<span id="WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE"></span><span id="wmt_right_copy_to_non_sdmi_device"></span>**WMT\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE**
</dt> <dd>

Specifies the right to copy content to a device not compliant with the Secure Digital Music Initiative (SDMI).

</dd> <dt>

<span id="WMT_RIGHT_COPY_TO_CD"></span><span id="wmt_right_copy_to_cd"></span>**WMT\_RIGHT\_COPY\_TO\_CD**
</dt> <dd>

Specifies the right to copy content to a CD.

</dd> <dt>

<span id="WMT_RIGHT_COPY_TO_SDMI_DEVICE"></span><span id="wmt_right_copy_to_sdmi_device"></span>**WMT\_RIGHT\_COPY\_TO\_SDMI\_DEVICE**
</dt> <dd>

Specifies the right to copy content to a device compliant with the SDMI.

</dd> <dt>

<span id="WMT_RIGHT_ONE_TIME"></span><span id="wmt_right_one_time"></span>**WMT\_RIGHT\_ONE\_TIME**
</dt> <dd>

Specifies the right to play content one time only.

</dd> <dt>

<span id="WMT_RIGHT_SAVE_STREAM_PROTECTED"></span><span id="wmt_right_save_stream_protected"></span>**WMT\_RIGHT\_SAVE\_STREAM\_PROTECTED**
</dt> <dd>

Specifies the right to save content from a server.

</dd> <dt>

<span id="WMT_RIGHT_COPY"></span><span id="wmt_right_copy"></span>**WMT\_RIGHT\_COPY**
</dt> <dd>

Specifies the right to copy content. Windows Media DRM 10 regulates the devices to which the content can be copied by using output protection levels (OPLs).

</dd> <dt>

<span id="WMT_RIGHT_COLLABORATIVE_PLAY"></span><span id="wmt_right_collaborative_play"></span>**WMT\_RIGHT\_COLLABORATIVE\_PLAY**
</dt> <dd>

Specifies the right to play content as part of an online scenario where multiple participants can contribute songs from their collection to a shared playlist.

</dd> <dt>

<span id="WMT_RIGHT_SDMI_TRIGGER"></span><span id="wmt_right_sdmi_trigger"></span>**WMT\_RIGHT\_SDMI\_TRIGGER**
</dt> <dd>

Reserved for future use. Do not use.

</dd> <dt>

<span id="WMT_RIGHT_SDMI_NOMORECOPIES"></span><span id="wmt_right_sdmi_nomorecopies"></span>**WMT\_RIGHT\_SDMI\_NOMORECOPIES**
</dt> <dd>

Reserved for future use. Do not use.

</dd> </dl>

## Remarks

These values are bit flags, so one or more can be set by combining them with the bitwise **OR** operator.

When using Windows Media DRM 10, **WMT\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE**, **WMT\_RIGHT\_COPY\_TO\_SDMI\_DEVICE**, and **WMT\_RIGHT\_COPY\_TO\_CD** are superseded by **WMT\_RIGHT\_COPY**. Limitations on the devices to which the content may be copied are specified by using output protection levels (OPLs).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> </dl>

 

 





