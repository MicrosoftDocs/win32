---
description: The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.
ms.assetid: 4a29d44b-8949-474d-a2bf-0c6e1d30b198
title: SENSOR_CATEGORY_ENVIRONMENTAL (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_ENVIRONMENTAL

The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                                                                                     | Description               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| <span id="SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE"></span><span id="sensor_type_environmental_atmospheric_pressure"></span><dl> <dt>**SENSOR\_TYPE\_ENVIRONMENTAL\_ATMOSPHERIC\_PRESSURE**</dt> <dt>{0E903829-FF8A-4A93-97DF-3DCBDE402288}</dt> </dl> | Barometers.<br/>    |
| <span id="SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY"></span><span id="sensor_type_environmental_humidity"></span><dl> <dt>**SENSOR\_TYPE\_ENVIRONMENTAL\_HUMIDITY**</dt> <dt>{5C72BF67-BD7E-4257-990B-98A3BA3B400A}</dt> </dl>                                      | Hygrometers.<br/>   |
| <span id="SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE"></span><span id="sensor_type_environmental_temperature"></span><dl> <dt>**SENSOR\_TYPE\_ENVIRONMENTAL\_TEMPERATURE**</dt> <dt>{04FD0EC4-D5DA-45FA-95A9-5DB38EE19306}</dt> </dl>                             | Thermometers<br/>   |
| <span id="SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION"></span><span id="sensor_type_environmental_wind_direction"></span><dl> <dt>**SENSOR\_TYPE\_ENVIRONMENTAL\_WIND\_DIRECTION**</dt> <dt>{9EF57A35-9306-434D-AF09-37FA5A9C00BD}</dt> </dl>                   | Weather vanes.<br/> |
| <span id="SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED"></span><span id="sensor_type_environmental_wind_speed"></span><dl> <dt>**SENSOR\_TYPE\_ENVIRONMENTAL\_WIND\_SPEED**</dt> <dt>{DD50607B-A45F-42CD-8EFD-EC61761C4226}</dt> </dl>                               | Anemometers.<br/>   |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_ENVIRONMENTAL\_GUID:

{8B0AA2F1-2D57-42EE-8CC0-4D27622B46C4}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR"></span><span id="sensor_data_type_atmospheric_pressure_bar"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ATMOSPHERIC\_PRESSURE\_BAR**</dt> <dt>(PID = 4) </dt> </dl>                                      | **VT\_R4**<br/> Atmospheric pressure in atmospheres (bars).<br/>                                                                                                                                              |
| <span id="SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS"></span><span id="sensor_data_type_temperature_celsius"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_TEMPERATURE\_CELSIUS**</dt> <dt>(PID = 2) </dt> </dl>                                                      | **VT\_R4**<br/> Temperature in degrees Celsius.<br/>                                                                                                                                                          |
| <span id="SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT"></span><span id="sensor_data_type_relative_humidity_percent"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_RELATIVE\_HUMIDITY\_PERCENT**</dt> <dt> (PID = 3) </dt> </dl>                                  | **VT\_R4**<br/> Relative humidity as a percentage.<br/>                                                                                                                                                       |
| <span id="SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE"></span><span id="sensor_data_type_wind_direction_degrees_anticlockwise"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_WIND\_DIRECTION\_DEGREES\_ANTICLOCKWISE**</dt> <dt>(PID = 5) </dt> </dl> | **VT\_R4**<br/> Wind direction relative to magnetic north, in degrees. North is represented as 0.0 (top of the X axis), with values increasing in an anticlockwise rotation. The Z axis points upwards. <br/> |
| <span id="SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND"></span><span id="sensor_data_type_wind_speed_meters_per_second"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_WIND\_SPEED\_METERS\_PER\_SECOND**</dt> <dt>(PID = 6) </dt> </dl>                        | **VT\_R4**<br/> Wind speed in meters per second.<br/>                                                                                                                                                         |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




