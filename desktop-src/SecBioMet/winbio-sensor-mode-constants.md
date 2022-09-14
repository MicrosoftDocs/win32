---
title: WINBIO_SENSOR_MODE Constants (Winbio\_types.h)
description: Set the sensor adapter mode.
ms.assetid: fceaed5c-de59-4da7-9d7a-adeef353292f
topic_type:
- apiref
api_name:
- WINBIO_SENSOR_UNKNOWN_MODE
- WINBIO_SENSOR_BASIC_MODE
- WINBIO_SENSOR_ADVANCED_MODE
- WINBIO_SENSOR_NAVIGATION_MODE
- WINBIO_SENSOR_SLEEP_MODE
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_SENSOR\_MODE Constants

The following values are used in the [**SensorAdapterSetMode**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_mode_fn) function to set the sensor adapter mode.



| Constant                                                                                                                                                                                                        | Description                                                                                                                                                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_SENSOR_UNKNOWN_MODE"></span><span id="winbio_sensor_unknown_mode"></span><dl> <dt>**WINBIO\_SENSOR\_UNKNOWN\_MODE**</dt> </dl>          | The operating mode is not known.<br/>                                                                                                                    |
| <span id="WINBIO_SENSOR_BASIC_MODE"></span><span id="winbio_sensor_basic_mode"></span><dl> <dt>**WINBIO\_SENSOR\_BASIC\_MODE**</dt> </dl>                | Operate the sensor in basic mode. The sensor acts only as a capture device. Any onboard processing or storage capabilities that exist are not used.<br/> |
| <span id="WINBIO_SENSOR_ADVANCED_MODE"></span><span id="winbio_sensor_advanced_mode"></span><dl> <dt>**WINBIO\_SENSOR\_ADVANCED\_MODE**</dt> </dl>       | Operate the sensor in advanced mode. The sensor can capture samples and perform matching and storage functions.<br/>                                     |
| <span id="WINBIO_SENSOR_NAVIGATION_MODE"></span><span id="winbio_sensor_navigation_mode"></span><dl> <dt>**WINBIO\_SENSOR\_NAVIGATION\_MODE**</dt> </dl> | Operate the sensor as a mouse pad. This is not currently supported.<br/>                                                                                 |
| <span id="WINBIO_SENSOR_SLEEP_MODE"></span><span id="winbio_sensor_sleep_mode"></span><dl> <dt>**WINBIO\_SENSOR\_SLEEP\_MODE**</dt> </dl>                | Operate the sensor in sleep mode.<br/>                                                                                                                   |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





