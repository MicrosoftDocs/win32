---
description: Specifies the maximum number of dynamic audio objects that can be rendered by the audio endpoint simulataneously.
ms.assetid: 6B6D73C1-C2E6-4C23-BBAD-7B51E8441C71
title: MF_MT_SPATIAL_AUDIO_MAX_DYNAMIC_OBJECTS attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_SPATIAL\_AUDIO\_MAX\_DYNAMIC\_OBJECTS attribute

Specifies the maximum number of dynamic audio objects that can be rendered by the audio endpoint simulataneously.

## Data type

**UINT32**

## Remarks

An [**IMFSpatialAudioSample**](/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudiosample) may contain fewer samples than the number specified by this attribute. If a sample contains more audio objects than specified by this attribute, the behavior is undefined.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




