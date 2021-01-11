---
description: Defines algorithms for the video processor which is use by MF\_VIDEO\_PROCESSOR\_ALGORITHM.
ms.assetid: 3BB0836E-39E6-40FA-9BA0-C986EB587CF1
title: MF_VIDEO_PROCESSOR_ALGORITHM_TYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MF_VIDEO_PROCESSOR_ALGORITHM_TYPE
api_type: 
- HeaderDef
api_location: 
- mfidl.h
---

# MF\_VIDEO\_PROCESSOR\_ALGORITHM\_TYPE enumeration

Defines algorithms for the video processor which is use by [MF\_VIDEO\_PROCESSOR\_ALGORITHM](mf-video-processor-algorithm.md).

## Syntax


```C++
typedef enum _MF_VIDEO_PROCESSOR_ALGORITHM_TYPE { 
  MF_VIDEO_PROCESSOR_ALGORITHM_DEFAULT      = 0,
  MF_VIDEO_PROCESSOR_ALGORITHM_MRF_CRF_444  = 1
} MF_VIDEO_PROCESSOR_ALGORITHM_TYPE;
```



## Constants

<dl> <dt>

<span id="MF_VIDEO_PROCESSOR_ALGORITHM_DEFAULT"></span><span id="mf_video_processor_algorithm_default"></span>**MF\_VIDEO\_PROCESSOR\_ALGORITHM\_DEFAULT**
</dt> <dd>

default mode favors a balance of quality and speed

</dd> <dt>

<span id="MF_VIDEO_PROCESSOR_ALGORITHM_MRF_CRF_444"></span><span id="mf_video_processor_algorithm_mrf_crf_444"></span>**MF\_VIDEO\_PROCESSOR\_ALGORITHM\_MRF\_CRF\_444**
</dt> <dd>

The video processor will always internally process in AYUV and use high quality filters.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| IDL<br/>                      | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Enumerations](media-foundation-enumerations.md)
</dt> </dl>

 

 




