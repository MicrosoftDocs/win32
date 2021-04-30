---
description: A decoder-defined GUID that identifies the spatial audio metadata format, notifying downstream components of the metadata object type that the decoder will output.
ms.assetid: 9714A2C7-25A1-4735-A0AC-22329ECBBC46
title: MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_FORMAT_ID attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_FORMAT\_ID attribute

A decoder-defined GUID that identifies the spatial audio metadata format, notifying downstream components of the metadata object type that the decoder will output.

## Data type

**GUID**

## Remarks

The metadata blob with the specified format is written using the [**ISpatialAudioMetadataWriter**](/windows/win32/api/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudiometadatawriter) interface and read using the [**ISpatialAudioMetadataReader**](/windows/win32/api/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudiometadatareader) interface. The metadata blob is opaque to the Media Foundation pipeline and components. The attribute is applied to the spatial audio media type. If a downstream component does not support the metadata format specified by the GUID, the component should reject the input media type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 
