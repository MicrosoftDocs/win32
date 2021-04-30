---
title: WINBIO_ORIENTATION Constants (Winbio\_types.h)
description: The following constants specify the possible camera orientations that the sensor component specifies as mandatory.
ms.assetid: E44A6F17-5F38-47C7-947B-FB6FB79B1217
topic_type:
- apiref
api_name:
- WINBIO_ORIENTATION_UNSPECIFIED
- WINBIO_ORIENTATION_LANDSCAPE
- WINBIO_ORIENTATION_PORTRAIT
- WINBIO_ORIENTATION_ANY
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_ORIENTATION Constants

The following constants specify the possible camera orientations that the sensor component specifies as mandatory.



| Constant/value                                                                                                                                                                                                                                                           | Description                                                         |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|
| <span id="WINBIO_ORIENTATION_UNSPECIFIED"></span><span id="winbio_orientation_unspecified"></span><dl> <dt>**WINBIO\_ORIENTATION\_UNSPECIFIED**</dt> <dt>0</dt> </dl> | A mandatory orientation for the camera is not specified.<br/> |
| <span id="WINBIO_ORIENTATION_LANDSCAPE"></span><span id="winbio_orientation_landscape"></span><dl> <dt>**WINBIO\_ORIENTATION\_LANDSCAPE**</dt> <dt>1</dt> </dl>       | The landscape orientation is required for the camera.<br/>    |
| <span id="WINBIO_ORIENTATION_PORTRAIT"></span><span id="winbio_orientation_portrait"></span><dl> <dt>**WINBIO\_ORIENTATION\_PORTRAIT**</dt> <dt>2</dt> </dl>          | The portrait orientation is required for the camera.<br/>     |
| <span id="WINBIO_ORIENTATION_ANY"></span><span id="winbio_orientation_any"></span><dl> <dt>**WINBIO\_ORIENTATION\_ANY**</dt> <dt>3</dt> </dl>                         | Any orientation is permitted for the camera.<br/>             |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[**WINBIO\_EXTENDED\_SENSOR\_INFO**](winbio-extended-sensor-info.md)
</dt> </dl>

 

 





