---
description: The SENSOR\_CATEGORY\_ELECTRICAL category contains sensors that provide information about electrical systems.
ms.assetid: c4efa821-fb9f-4606-898a-5be103581f39
title: SENSOR_CATEGORY_ELECTRICAL (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_ELECTRICAL

The SENSOR\_CATEGORY\_ELECTRICAL category contains sensors that provide information about electrical systems.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                              | Description                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| <span id="SENSOR_TYPE_CAPACITANCE"></span><span id="sensor_type_capacitance"></span><dl> <dt>**SENSOR\_TYPE\_CAPACITANCE**</dt> <dt>{CA2FFB1C-2317-49C0-A0B4-B63CE63461A0}</dt> </dl>                 | Capacitance sensors.<br/>         |
| <span id="SENSOR_TYPE_CURRENT"></span><span id="sensor_type_current"></span><dl> <dt>**SENSOR\_TYPE\_CURRENT**</dt> <dt>{5ADC9FCE-15A0-4BBE-A1AD-2D38A9AE831C}</dt> </dl>                             | Electrical current sensors.<br/>  |
| <span id="SENSOR_TYPE_ELECTRICAL_POWER"></span><span id="sensor_type_electrical_power"></span><dl> <dt>**SENSOR\_TYPE\_ELECTRICAL\_POWER**</dt> <dt>{212F10F5-14AB-4376-9A43-A7794098C2FE}</dt> </dl> | Electrical power sensors.<br/>    |
| <span id="SENSOR_TYPE_FREQUENCY"></span><span id="sensor_type_frequency"></span><dl> <dt>**SENSOR\_TYPE\_FREQUENCY**</dt> <dt>{8CD2CBB6-73E6-4640-A709-72AE8FB60D7F}</dt> </dl>                       | Electrical frequency sensor.<br/> |
| <span id="SENSOR_TYPE_INDUCTANCE"></span><span id="sensor_type_inductance"></span><dl> <dt>**SENSOR\_TYPE\_INDUCTANCE**</dt> <dt>{DC1D933F-C435-4C7D-A2FE-607192A524D3}</dt> </dl>                    | Inductance sensors.<br/>          |
| <span id="SENSOR_TYPE_POTENTIOMETER"></span><span id="sensor_type_potentiometer"></span><dl> <dt>**SENSOR\_TYPE\_POTENTIOMETER**</dt> <dt>{2B3681A9-CADC-45AA-A6FF-54957C8BB440}</dt> </dl>           | Potentiometers.<br/>              |
| <span id="SENSOR_TYPE_RESISTANCE"></span><span id="sensor_type_resistance"></span><dl> <dt>**SENSOR\_TYPE\_RESISTANCE**</dt> <dt>{9993D2C8-C157-4A52-A7B5-195C76037231}</dt> </dl>                    | Resistance sensors.<br/>          |
| <span id="SENSOR_TYPE_VOLTAGE"></span><span id="sensor_type_voltage"></span><dl> <dt>**SENSOR\_TYPE\_VOLTAGE**</dt> <dt>{C5484637-4FB7-4953-98B8-A56D8AA1FB1E}</dt> </dl>                             | Voltage sensors.<br/>             |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_ELECTRICAL\_GUID:

{BBB246D1-E242-4780-A2D3-CDED84F35842}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                                         | Description                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_CAPACITANCE_FARAD"></span><span id="sensor_data_type_capacitance_farad"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_CAPACITANCE\_FARAD**</dt> <dt> (PID = 4) </dt> </dl>                                | **VT\_R8**<br/> Capacitance in farads.<br/>                                       |
| <span id="SENSOR_DATA_TYPE_CURRENT_AMPS"></span><span id="sensor_data_type_current_amps"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_CURRENT\_AMPS**</dt> <dt>(PID = 3) </dt> </dl>                                                | **VT\_R8**<br/> Current in amperes.<br/>                                          |
| <span id="SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ"></span><span id="sensor_data_type_electrical_frequency_hertz"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ELECTRICAL\_FREQUENCY\_HERTZ**</dt> <dt>(PID = 9) </dt> </dl>     | **VT\_R8**<br/> Electrical frequency in hertz.<br/>                               |
| <span id="SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE"></span><span id="sensor_data_type_electrical_percent_of_range"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ELECTRICAL\_PERCENT\_OF\_RANGE**</dt> <dt>(PID = 8) </dt> </dl> | **VT\_R8**<br/> Potentiometer reading as a percentage of its possible range.<br/> |
| <span id="SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS"></span><span id="sensor_data_type_electrical_power_watts"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_ELECTRICAL\_POWER\_WATTS**</dt> <dt> (PID = 7) </dt> </dl>                | **VT\_R8**<br/> Electrical power in watts.<br/>                                   |
| <span id="SENSOR_DATA_TYPE_INDUCTANCE_HENRY"></span><span id="sensor_data_type_inductance_henry"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_INDUCTANCE\_HENRY**</dt> <dt>(PID = 6) </dt> </dl>                                    | **VT\_R8**<br/> Inductance in henries.<br/>                                       |
| <span id="SENSOR_DATA_TYPE_RESISTANCE_OHMS"></span><span id="sensor_data_type_resistance_ohms"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_RESISTANCE\_OHMS**</dt> <dt>(PID = 5) </dt> </dl>                                       | **VT\_R8**<br/> Resistance in ohms.<br/>                                          |
| <span id="SENSOR_DATA_TYPE_VOLTAGE_VOLTS"></span><span id="sensor_data_type_voltage_volts"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_VOLTAGE\_VOLTS**</dt> <dt>(PID = 2) </dt> </dl>                                             | **VT\_R8**<br/> Electrical potential in volts.<br/>                               |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




