---
description: The SENSOR\_CATEGORY\_MECHANICAL category contains sensors that provide information related to mechanical devices and measurements.
ms.assetid: d1243303-d26c-45ce-b97b-d554daeeb462
title: SENSOR_CATEGORY_MECHANICAL (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_MECHANICAL

The SENSOR\_CATEGORY\_MECHANICAL category contains sensors that provide information related to mechanical devices and measurements.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                                           | Description                                         |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| <span id="SENSOR_TYPE_BOOLEAN_SWITCH"></span><span id="sensor_type_boolean_switch"></span><dl> <dt>**SENSOR\_TYPE\_BOOLEAN\_SWITCH**</dt> <dt>{9C7E371F-1041-460B-8D5C-71E4752E350C}</dt> </dl>                    | Two-state switches (off or on).<br/>          |
| <span id="SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY"></span><span id="sensor_type_boolean_switch_array"></span><dl> <dt>**SENSOR\_TYPE\_BOOLEAN\_SWITCH\_ARRAY**</dt> <dt>{545C8BA5-B143-4545-868F-CA7FD986B4F6}</dt> </dl> | Array of two-state switches (off or on).<br/> |
| <span id="SENSOR_TYPE_FORCE"></span><span id="sensor_type_force"></span><dl> <dt>**SENSOR\_TYPE\_FORCE**</dt> <dt>{C2AB2B02-1A1C-4778-A81B-954A1788CC75}</dt> </dl>                                                | Force sensors.<br/>                           |
| <span id="SENSOR_TYPE_MULTIVALUE_SWITCH"></span><span id="sensor_type_multivalue_switch"></span><dl> <dt>**SENSOR\_TYPE\_MULTIVALUE\_SWITCH**</dt> <dt>{B3EE4D76-37A4-4402-B25E-99C60A775FA1}</dt> </dl>           | Multiple-position switches.<br/>              |
| <span id="SENSOR_TYPE_PRESSURE"></span><span id="sensor_type_pressure"></span><dl> <dt>**SENSOR\_TYPE\_PRESSURE**</dt> <dt>{26D31F34-6352-41CF-B793-EA0713D53D77}</dt> </dl>                                       | Pressure sensors.<br/>                        |
| <span id="SENSOR_TYPE_SCALE"></span><span id="sensor_type_scale"></span><dl> <dt>**SENSOR\_TYPE\_SCALE**</dt> <dt>{C06DD92C-7FEB-438E-9BF6-82207FFF5BB8}</dt> </dl>                                                | Weight sensors.<br/>                          |
| <span id="SENSOR_TYPE_STRAIN"></span><span id="sensor_type_strain"></span><dl> <dt>**SENSOR\_TYPE\_STRAIN**</dt> <dt>{C6D1EC0E-6803-4361-AD3D-85BCC58C6D29}</dt> </dl>                                             | Strain sensors.<br/>                          |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_GUID\_MECHANICAL\_GUID:

{38564A7C-F2F2-49BB-9B2B-BA60F66A58DF}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                                         | Description                                                                        |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL"></span><span id="sensor_data_type_absolute_pressure_pascal"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ABSOLUTE\_PRESSURE\_PASCAL**</dt> <dt> (PID = 5) </dt> </dl>          | **VT\_R8**<br/> Absolute pressure, in pascals.<br/>                    |
| <span id="SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES"></span><span id="sensor_data_type_boolean_switch_array_states"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_BOOLEAN\_SWITCH\_ARRAY\_STATES**</dt> <dt>(PID = 10)</dt> </dl> | **VT\_UI4**<br/> State fields for an array of Boolean switches.<br/>   |
| <span id="SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE"></span><span id="sensor_data_type_boolean_switch_state"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_BOOLEAN\_SWITCH\_STATE**</dt> <dt>(PID = 2) </dt> </dl>                       | **VT\_BOOL**<br/> State field for SENSOR\_TYPE\_BOOLEAN\_SWITCH.<br/>  |
| <span id="SENSOR_DATA_TYPE_FORCE_NEWTONS"></span><span id="sensor_data_type_force_newtons"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_FORCE\_NEWTONS**</dt> <dt> (PID = 4) </dt> </dl>                                            | **VT\_R8**<br/> Force, in newtons.<br/>                                |
| <span id="SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL"></span><span id="sensor_data_type_gauge_pressure_pascal"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_GAUGE\_PRESSURE\_PASCAL**</dt> <dt> (PID = 6) </dt> </dl>                   | **VT\_R8**<br/> Relative gauge pressure, in pascals.<br/>              |
| <span id="SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE"></span><span id="sensor_data_type_multivalue_switch_state"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_MULTIVALUE\_SWITCH\_STATE**</dt> <dt> (PID = 3) </dt> </dl>             | **VT\_R8**<br/> State field for SENSOR\_TYPE\_MULTIVALUE\_SWITCH.<br/> |
| <span id="SENSOR_DATA_TYPE_STRAIN"></span><span id="sensor_data_type_strain"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_STRAIN**</dt> <dt> (PID = 7) </dt> </dl>                                                                  | **VT\_R8**<br/> Strain.<br/>                                           |
| <span id="SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS"></span><span id="sensor_data_type_weight_kilograms"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_WEIGHT\_KILOGRAMS**</dt> <dt> (PID = 8) </dt> </dl>                                   | **VT\_R8**<br/> Weight, in kilograms.<br/>                             |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




