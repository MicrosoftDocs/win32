---
title: FORMAT\_TYPE enumeration
description: The FORMAT\_TYPE enumeration describes the format of a buffer and how it should be treated.
ms.assetid: 4421d80f-17e8-4d3a-bccf-0ee90d987e21
keywords:
- FORMAT_TYPE enumeration Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- FORMAT_TYPE
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# FORMAT\_TYPE enumeration

The **FORMAT\_TYPE** enumeration describes the format of a buffer and how it should be treated.

## Syntax


```C++
typedef enum eFORMAT_TYPE { 
  FORMAT_VIDEO_TYPE_SYSTEMMEM            = 0x001,
  FORMAT_VIDEO_TYPE_VIDEOMEM             = 0x002,
  FORMAT_VIDEO_TYPE_SYSTEM_OR_VIDEO_MEM  = 0x004,
  FORMAT_VIDEO_TYPE_ALPHA                = 0x010,
  FORMAT_VIDEO_TYPE_NONALPHA             = 0x020,
  FORMAT_VIDEO_FLAG_FORCELETTERBOX       = 0x100,
  FORMAT_VIDEO_FLAG_CANLETTERBOX         = 0x200,
  FORMAT_AUDIO_TYPE_BUFFER               = 0x001,
  FORMAT_FLAG_READONLY                   = 0x010000,
  FORMAT_FLAG_INPLACE_RENDER             = 0x020000,
  FORMAT_FLAG_PREROLL                    = 0x100000,
  FORMAT_FLAG_MASK                       = 0xFFFF0000,
  FORMAT_VIDEO_LOCATION_TYPE_MASK        = 0x0F,
  FORMAT_VIDEO_COLOR_TYPE_MASK           = 0xF0,
  FORMAT_MEDIA_TYPE_MASK                 = 0xFFFF
} FORMAT_TYPE;
```



## Constants

<dl> <dt>

<span id="FORMAT_VIDEO_TYPE_SYSTEMMEM"></span><span id="format_video_type_systemmem"></span>**FORMAT\_VIDEO\_TYPE\_SYSTEMMEM**
</dt> <dd>

The buffer uses system memory. Specifying this can reduce performance.

</dd> <dt>

<span id="FORMAT_VIDEO_TYPE_VIDEOMEM"></span><span id="format_video_type_videomem"></span>**FORMAT\_VIDEO\_TYPE\_VIDEOMEM**
</dt> <dd>

The buffer uses video memory. Specifying this can improve performance.

</dd> <dt>

<span id="FORMAT_VIDEO_TYPE_SYSTEM_OR_VIDEO_MEM"></span><span id="format_video_type_system_or_video_mem"></span>**FORMAT\_VIDEO\_TYPE\_SYSTEM\_OR\_VIDEO\_MEM**
</dt> <dd>

The buffer can use system or video memory.

</dd> <dt>

<span id="FORMAT_VIDEO_TYPE_ALPHA"></span><span id="format_video_type_alpha"></span>**FORMAT\_VIDEO\_TYPE\_ALPHA**
</dt> <dd>

The buffer contains alpha blending data.

</dd> <dt>

<span id="FORMAT_VIDEO_TYPE_NONALPHA"></span><span id="format_video_type_nonalpha"></span>**FORMAT\_VIDEO\_TYPE\_NONALPHA**
</dt> <dd>

The buffer does not contain alpha blending data.

</dd> <dt>

<span id="FORMAT_VIDEO_FLAG_FORCELETTERBOX"></span><span id="format_video_flag_forceletterbox"></span>**FORMAT\_VIDEO\_FLAG\_FORCELETTERBOX**
</dt> <dd>

The video information is in letterbox format only.

</dd> <dt>

<span id="FORMAT_VIDEO_FLAG_CANLETTERBOX"></span><span id="format_video_flag_canletterbox"></span>**FORMAT\_VIDEO\_FLAG\_CANLETTERBOX**
</dt> <dd>

The video information can be displayed in letterbox format.

</dd> <dt>

<span id="FORMAT_AUDIO_TYPE_BUFFER"></span><span id="format_audio_type_buffer"></span>**FORMAT\_AUDIO\_TYPE\_BUFFER**
</dt> <dd>

This is an audio buffer. The value is the same as **FORMAT\_VIDEO\_TYPE\_SYSTEMMEM** because all audio uses system memory.

</dd> <dt>

<span id="FORMAT_FLAG_READONLY"></span><span id="format_flag_readonly"></span>**FORMAT\_FLAG\_READONLY**
</dt> <dd>

The data should not be modified inside this buffer; you should create a new buffer to hold modified data. Contrast with **FORMAT\_FLAG\_INPLACE\_RENDER**.

</dd> <dt>

<span id="FORMAT_FLAG_INPLACE_RENDER"></span><span id="format_flag_inplace_render"></span>**FORMAT\_FLAG\_INPLACE\_RENDER**
</dt> <dd>

The data should be modified in place, in the buffer. Contrast with **FORMAT\_FLAG\_READONLY**.

</dd> <dt>

<span id="FORMAT_FLAG_PREROLL"></span><span id="format_flag_preroll"></span>**FORMAT\_FLAG\_PREROLL**
</dt> <dd>

This buffer should be prerolled.

</dd> <dt>

<span id="FORMAT_FLAG_MASK"></span><span id="format_flag_mask"></span>**FORMAT\_FLAG\_MASK**
</dt> <dd>

A mask to determine the upper two bytes of the enumeration value.

</dd> <dt>

<span id="FORMAT_VIDEO_LOCATION_TYPE_MASK"></span><span id="format_video_location_type_mask"></span>**FORMAT\_VIDEO\_LOCATION\_TYPE\_MASK**
</dt> <dd>

A mask to determine what kind of memory this buffer uses system memory (**FORMAT\_VIDEO\_TYPE\_SYSTEMMEM**) or video memory (**FORMAT\_VIDEO\_TYPE\_VIDEOMEM**).

</dd> <dt>

<span id="FORMAT_VIDEO_COLOR_TYPE_MASK"></span><span id="format_video_color_type_mask"></span>**FORMAT\_VIDEO\_COLOR\_TYPE\_MASK**
</dt> <dd>

A mask to determine whether the enumeration value contains alpha blending data. See **FORMAT\_VIDEO\_TYPE\_ALPHA** and **FORMAT\_VIDEO\_TYPE\_NONALPHA**.

</dd> <dt>

<span id="FORMAT_MEDIA_TYPE_MASK"></span><span id="format_media_type_mask"></span>**FORMAT\_MEDIA\_TYPE\_MASK**
</dt> <dd>

A mask to determine the lower two bytes of the enumeration value. (This includes the basic media type of the buffer.)

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





