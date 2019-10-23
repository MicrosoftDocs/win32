---
Description: A value specifying the size, in bytes, of the spatial audio metadata object type that the decoder will output.
ms.assetid: C133693D-A8D5-4520-B561-57BF11074257
title: MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_LENGTH attribute
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_LENGTH attribute

A value specifying the size, in bytes, of the spatial audio metadata object type that the decoder will output.

## Data type

**UINT32**

## Remarks

The metadata blob with the specified format is written using the [**ISpatialAudioMetadataWriter**](https://msdn.microsoft.com/en-us/library/Mt798197(v=VS.85).aspx) interface and read using the [**ISpatialAudioMetadataReader**](https://msdn.microsoft.com/en-us/library/Mt798191(v=VS.85).aspx) interface. The metadata blob is opaque to the Media Foundation pipeline and components. The attribute is applied to the spatial audio media type.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




