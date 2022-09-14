---
description: The SENSOR\_CATEGORY\_BIOMETRIC category contains sensors that provide information about living beings.
ms.assetid: dfc7ad46-c13b-46d1-8854-0d93ecaac55a
title: SENSOR_CATEGORY_BIOMETRIC (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_BIOMETRIC

The SENSOR\_CATEGORY\_BIOMETRIC category contains sensors that provide information about living beings.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                           | Description                                     |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
| <span id="SENSOR_TYPE_HUMAN_PRESENCE"></span><span id="sensor_type_human_presence"></span><dl> <dt>**SENSOR\_TYPE\_HUMAN\_PRESENCE**</dt> <dt>{C138C12B-AD52-451C-9375-87F518FF10C6}</dt> </dl>    | Sensors that detect human presence.<br/>  |
| <span id="SENSOR_TYPE_HUMAN_PROXIMITY"></span><span id="sensor_type_human_proximity"></span><dl> <dt>**SENSOR\_TYPE\_HUMAN\_PROXIMITY**</dt> <dt>{5220DAE9-3179-4430-9F90-06266D2A34DE}</dt> </dl> | Sensors that detect human proximity.<br/> |
| <span id="SENSOR_TYPE_TOUCH"></span><span id="sensor_type_touch"></span><dl> <dt>**SENSOR\_TYPE\_TOUCH**</dt> <dt>{17DB3018-06C4-4F7D-81AF-9274B7599C27}</dt> </dl>                                | Touch sensors.<br/>                       |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_BIOMETRIC\_GUID:

{2299288A-6D9E-4B0B-B7EC-3528F89E40AF}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                                         | Description                                                                                               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_HUMAN_PRESENCE"></span><span id="sensor_data_type_human_presence"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_HUMAN\_PRESENCE**</dt> <dt>(PID = 2) </dt> </dl>                          | **VT\_BOOL**<br/> **TRUE** when a human is using the computer.<br/>                           |
| <span id="SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS"></span><span id="sensor_data_type_human_proximity_meters"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_HUMAN\_PROXIMITY\_METERS**</dt> <dt>(PID = 3) </dt> </dl> | **VT\_R4**<br/> Distance between a human and the computer, in meters.<br/>                    |
| <span id="SENSOR_DATA_TYPE_TOUCH_STATE"></span><span id="sensor_data_type_touch_state"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_TOUCH\_STATE**</dt> <dt>(PID = 4) </dt> </dl>                                   | **VT\_BOOL**<br/> **TRUE** when the touch sensor is being touched; otherwise, **FALSE**.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




