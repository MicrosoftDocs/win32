---
title: MEDIA\_FORMAT\_TYPE enumeration
description: The MEDIA\_FORMAT\_TYPE enumeration describes the media type handled by a transform.
ms.assetid: c417e1e8-a539-4021-b9ae-b9764686d3cc
keywords:
- MEDIA_FORMAT_TYPE enumeration Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- MEDIA_FORMAT_TYPE
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEDIA\_FORMAT\_TYPE enumeration

The **MEDIA\_FORMAT\_TYPE** enumeration describes the media type handled by a transform.

## Syntax


```C++
typedef enum eMEDIA_FORMAT_TYPE { 
  MEDIA_TYPE_VIDEO,
  MEDIA_TYPE_AUDIO
} MEDIA_FORMAT_TYPE;
```



## Constants

<dl> <dt>

<span id="MEDIA_TYPE_VIDEO"></span><span id="media_type_video"></span>**MEDIA\_TYPE\_VIDEO**
</dt> <dd>

The buffer uses system memory.

</dd> <dt>

<span id="MEDIA_TYPE_AUDIO"></span><span id="media_type_audio"></span>**MEDIA\_TYPE\_AUDIO**
</dt> <dd>

The buffer uses video memory.

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

 

 





