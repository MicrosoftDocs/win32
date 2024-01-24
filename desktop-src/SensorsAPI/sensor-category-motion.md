---
description: The SENSOR\_CATEGORY\_MOTION category contains sensors that provide information that is related to physical movement.
ms.assetid: be025c86-46b5-4f50-a3af-0408bb3c9b5b
title: SENSOR_CATEGORY_MOTION (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_MOTION

The SENSOR\_CATEGORY\_MOTION category contains sensors that provide information that is related to physical movement. Accelerometers measure acceleration of the sensor, including gravitational acceleration. Motion detectors, such as human movement detection in a security system, sense moving objects. Gyrometers sense changes in angular velocity. Speedometers measure velocity.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                              | Description                                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| <span id="SENSOR_TYPE_ACCELEROMETER_1D"></span><span id="sensor_type_accelerometer_1d"></span><dl> <dt>**SENSOR\_TYPE\_ACCELEROMETER\_1D**</dt> <dt>{C04D2387-7340-4CC2-991E-3B18CB8EF2F4}</dt> </dl> | One-axis accelerometers.<br/>                                  |
| <span id="SENSOR_TYPE_ACCELEROMETER_2D"></span><span id="sensor_type_accelerometer_2d"></span><dl> <dt>**SENSOR\_TYPE\_ACCELEROMETER\_2D**</dt> <dt>{B2C517A8-F6B5-4BA6-A423-5DF560B4CC07}</dt> </dl> | Two-axis accelerometers.<br/>                                  |
| <span id="SENSOR_TYPE_ACCELEROMETER_3D"></span><span id="sensor_type_accelerometer_3d"></span><dl> <dt>**SENSOR\_TYPE\_ACCELEROMETER\_3D**</dt> <dt>{C2FB0F5F-E2D2-4C78-BCD0-352A9582819D}</dt> </dl> | Three-axis accelerometers.<br/>                                |
| <span id="SENSOR_TYPE_GYROMETER_1D"></span><span id="sensor_type_gyrometer_1d"></span><dl> <dt>**SENSOR\_TYPE\_GYROMETER\_1D**</dt> <dt>{FA088734-F552-4584-8324-EDFAF649652C}</dt> </dl>             | One-axis gyrometers.<br/>                                      |
| <span id="SENSOR_TYPE_GYROMETER_2D"></span><span id="sensor_type_gyrometer_2d"></span><dl> <dt>**SENSOR\_TYPE\_GYROMETER\_2D**</dt> <dt>{31EF4F83-919B-48BF-8DE0-5D7A9D240556}</dt> </dl>             | Two-axis gyrometers.<br/>                                      |
| <span id="SENSOR_TYPE_GYROMETER_3D"></span><span id="sensor_type_gyrometer_3d"></span><dl> <dt>**SENSOR\_TYPE\_GYROMETER\_3D**</dt> <dt>{09485F5A-759E-42C2-BD4B-A349B75C8643}</dt> </dl>             | Three-axis gyrometers.<br/>                                    |
| <span id="SENSOR_TYPE_MOTION_DETECTOR"></span><span id="sensor_type_motion_detector"></span><dl> <dt>**SENSOR\_TYPE\_MOTION\_DETECTOR**</dt> <dt>{5C7C1A12-30A5-43B9-A4B2-CF09EC5B7BE8}</dt> </dl>    | Motion detectors, such as those used in security systems.<br/> |
| <span id="SENSOR_TYPE_SPEEDOMETER"></span><span id="sensor_type_speedometer"></span><dl> <dt>**SENSOR\_TYPE\_SPEEDOMETER**</dt> <dt>{6BD73C1F-0BB4-4310-81B2-DFC18A52BF94}</dt> </dl>                 | Rate-of-motion sensors.<br/>                                   |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_MOTION\_GUID:

{3F8A69A2-07C5-4E48-A965-CD797AAB56D5}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                     |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_ACCELERATION_X_G"></span><span id="sensor_data_type_acceleration_x_g"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ACCELERATION\_X\_G**</dt> <dt>(PID = 2) </dt> </dl>                                                                                                         | **VT\_R8**<br/> X-axis acceleration, in *g*'s.<br/>                                 |
| <span id="SENSOR_DATA_TYPE_ACCELERATION_Y_G"></span><span id="sensor_data_type_acceleration_y_g"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ACCELERATION\_Y\_G**</dt> <dt>(PID = 3) </dt> </dl>                                                                                                         | **VT\_R8**<br/> Y-axis acceleration, in *g*'s.<br/>                                 |
| <span id="SENSOR_DATA_TYPE_ACCELERATION_Z_G"></span><span id="sensor_data_type_acceleration_z_g"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ACCELERATION\_Z\_G**</dt> <dt>(PID = 4) </dt> </dl>                                                                                                         | **VT\_R8**<br/> Z-axis acceleration, in *g*'s.<br/>                                 |
| <span id="SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED"></span><span id="sensor_data_type_angular_acceleration_x_degrees_per_second_squared"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_ACCELERATION\_X\_DEGREES\_PER\_SECOND\_SQUARED**</dt> <dt>(PID = 5) </dt> </dl>  | **VT\_R8**<br/> Gyrometric x-axis acceleration, in degrees per second squared.<br/> |
| <span id="SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED"></span><span id="sensor_data_type_angular_acceleration_y_degrees_per_second_squared"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_ACCELERATION\_Y\_DEGREES\_PER\_SECOND\_SQUARED**</dt> <dt> (PID = 6) </dt> </dl> | **VT\_R8**<br/> Gyrometric y-axis acceleration, in degrees per second squared.<br/> |
| <span id="SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED"></span><span id="sensor_data_type_angular_acceleration_z_degrees_per_second_squared"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_ACCELERATION\_Z\_DEGREES\_PER\_SECOND\_SQUARED**</dt> <dt> (PID = 7) </dt> </dl> | **VT\_R8**<br/> Gyrometric z-axis acceleration, in degrees per second squared.<br/> |
| <span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_x_degrees_per_second"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_VELOCITY\_X\_DEGREES\_PER\_SECOND**</dt> <dt> (PID = 10)</dt> </dl>                                      | **VT\_R8**<br/> Gyrometric x-axis velocity, in degrees per second.<br/>             |
| <span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_y_degrees_per_second"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_VELOCITY\_Y\_DEGREES\_PER\_SECOND**</dt> <dt> (PID = 11)</dt> </dl>                                      | **VT\_R8**<br/> Gyrometric y-axis velocity, in degrees per second.<br/>             |
| <span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_z_degrees_per_second"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ANGULAR\_VELOCITY\_Z\_DEGREES\_PER\_SECOND**</dt> <dt> (PID = 12)</dt> </dl>                                      | **VT\_R8**<br/> Gyrometric z-axis velocity, in degrees per second.<br/>             |
| <span id="SENSOR_DATA_TYPE_MOTION_STATE"></span><span id="sensor_data_type_motion_state"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_MOTION\_STATE**</dt> <dt>(PID = 9) </dt> </dl>                                                                                                                      | **VT\_BOOL**<br/> **TRUE** if motion is detected; otherwise, **FALSE**.<br/>        |
| <span id="SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND"></span><span id="sensor_data_type_speed_meters_per_second"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_SPEED\_METERS\_PER\_SECOND**</dt> <dt> (PID = 8) </dt> </dl>                                                                                  | **VT\_R8**<br/> Speed in meters per second.<br/>                                    |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




