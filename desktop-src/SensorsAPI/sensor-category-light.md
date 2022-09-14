---
description: The SENSOR\_CATEGORY\_LIGHT category contains sensors that provide information about characteristics of light.
ms.assetid: 0327bda5-f1d7-476d-9f0f-f4d60a6a106f
title: SENSOR_CATEGORY_LIGHT (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_LIGHT

The SENSOR\_CATEGORY\_LIGHT category contains sensors that provide information about characteristics of light.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                     | Description                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| <span id="SENSOR_TYPE_AMBIENT_LIGHT"></span><span id="sensor_type_ambient_light"></span><dl> <dt>**SENSOR\_TYPE\_AMBIENT\_LIGHT**</dt> <dt>{97F115C8-599A-4153-8894-D2D12899918A}</dt> </dl> | Ambient light sensors.<br/> |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_LIGHT\_GUID:

{E4C77CE2-DCB7-46E9-8439-4FEC548833A6}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_LIGHT_CHROMACITY__"></span><span id="sensor_data_type_light_chromacity__"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_LIGHT\_CHROMACITY** </dt> <dt> (PID = 4) </dt> </dl>                     | **VT\_VECTOR\|VT\_UI1**<br/> Chromaticity as a counted array of float values.<br/> Data for vector types is always serialized as **VT\_UI1** (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 4-byte real value (**VT\_R4**).<br/> For information about working with arrays, see [Retrieving Vector Types](retrieving-vector-types.md).<br/> |
| <span id="SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX"></span><span id="sensor_data_type_light_level_lux"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_LIGHT\_LEVEL\_LUX**</dt> <dt> (PID = 2) </dt> </dl>                            | **VT\_R4**<br/> Illuminance level, in lux.<br/>                                                                                                                                                                                                                                                                                                                                                              |
| <span id="SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN"></span><span id="sensor_data_type_light_temperature_kelvin"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_LIGHT\_TEMPERATURE\_KELVIN**</dt> <dt> (PID = 3) </dt> </dl> | **VT\_R4**<br/> Color temperature, in degrees Kelvin.<br/>                                                                                                                                                                                                                                                                                                                                                   |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




