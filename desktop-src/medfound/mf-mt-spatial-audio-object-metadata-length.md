---
Description: A value specifying the size, in bytes, of the spatial audio metadata object type that the decoder will output.
ms.assetid: C133693D-A8D5-4520-B561-57BF11074257
title: MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_LENGTH attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_LENGTH attribute

A value specifying the size, in bytes, of the spatial audio metadata object type that the decoder will output.

## Data type

**UINT32**

## Remarks

The metadata blob with the specified format is written using the [**ISpatialAudioMetadataWriter**](https://msdn.microsoft.com/windows/desktop/F8CD8B79-9442-46D0-ABF5-5F6734474B01) interface and read using the [**ISpatialAudioMetadataReader**](https://msdn.microsoft.com/windows/desktop/BD1AD4CE-6E88-4292-AA79-E71FE00C2078) interface. The metadata blob is opaque to the Media Foundation pipeline and components. The attribute is applied to the spatial audio media type.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




