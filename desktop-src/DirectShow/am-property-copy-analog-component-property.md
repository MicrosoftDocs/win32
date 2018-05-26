---
Description: Queries whether the video output is standard-definition, analog component video.
ms.assetid: bd4fc5bc-c45d-4228-9759-6300fdfff6a0
title: AM\_PROPERTY\_COPY\_ANALOG\_COMPONENT Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AM\_PROPERTY\_COPY\_ANALOG\_COMPONENT Property

Queries whether the video output is standard-definition, analog component video.



|                   |                                       |
|-------------------|---------------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_CopyProt             |
| Property ID       | AM\_PROPERTY\_COPY\_ANALOG\_COMPONENT |
| Data Type         | **ULONG**                             |



 

## Remarks

This property is read-only.

The value of the property is **TRUE** if the video output is analog component video with a resolution not greater than 480p for NTSC or 540p for PAL. Otherwise, the value is **FALSE**.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**DVD Copy Protection Property Set**](dvd-copy-protection-property-set.md)
</dt> </dl>

 

 




