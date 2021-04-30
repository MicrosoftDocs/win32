---
title: WINBIO_BIOMETRIC_SENSOR_SUBTYPE Constants (Winbio\_types.h)
description: Specify a bitmask for onboard sensor capabilities.
ms.assetid: ED2A26BC-AED4-4304-9A17-A9BA126B0AFC
topic_type:
- apiref
api_name:
- WINBIO_SENSOR_SUBTYPE_UNKNOWN
- WINBIO_FP_SENSOR_SUBTYPE_SWIPE
- WINBIO_FP_SENSOR_SUBTYPE_TOUCH
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIOMETRIC\_SENSOR\_SUBTYPE Constants

The following constants can be used as a bitmask for the *Capabilities* parameter of the [**WINBIO\_UNIT\_SCHEMA**](winbio-unit-schema.md) structure. These refer to the onboard sensor capabilities.



| Constant                                                                                                                                                                                                            | Description                                        |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| <span id="WINBIO_SENSOR_SUBTYPE_UNKNOWN"></span><span id="winbio_sensor_subtype_unknown"></span><dl> <dt>**WINBIO\_SENSOR\_SUBTYPE\_UNKNOWN**</dt> </dl>     | The sensor sub types is not known.<br/>      |
| <span id="WINBIO_FP_SENSOR_SUBTYPE_SWIPE"></span><span id="winbio_fp_sensor_subtype_swipe"></span><dl> <dt>**WINBIO\_FP\_SENSOR\_SUBTYPE\_SWIPE**</dt> </dl> | The sensor supports fingerprint swipes.<br/> |
| <span id="WINBIO_FP_SENSOR_SUBTYPE_TOUCH"></span><span id="winbio_fp_sensor_subtype_touch"></span><dl> <dt>**WINBIO\_FP\_SENSOR\_SUBTYPE\_TOUCH**</dt> </dl> | The sensor supports finger touches.<br/>     |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> <dt>

[**WINBIO\_UNIT\_SCHEMA**](winbio-unit-schema.md)
</dt> </dl>

 

 





