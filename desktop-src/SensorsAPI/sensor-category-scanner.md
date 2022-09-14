---
description: The SENSOR\_CATEGORY\_SCANNER category contains sensors that provide information that is obtained by scanning.
ms.assetid: 98a772c9-2a21-489f-ad8d-3b772b7ff892
title: SENSOR_CATEGORY_SCANNER (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_SCANNER

The SENSOR\_CATEGORY\_SCANNER category contains sensors that provide information that is obtained by scanning.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.



| Sensor type                                                                                                                                                                                                                                                                                           | Description                                                     |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| <span id="SENSOR_TYPE_BARCODE_SCANNER"></span><span id="sensor_type_barcode_scanner"></span><dl> <dt>**SENSOR\_TYPE\_BARCODE\_SCANNER**</dt> <dt>{990B3D8F-85BB-45FF-914D-998C04F372DF}</dt> </dl> | Sensors that use optical scanning to read bar codes.<br/> |
| <span id="SENSOR_TYPE_RFID_SCANNER"></span><span id="sensor_type_rfid_scanner"></span><dl> <dt>**SENSOR\_TYPE\_RFID\_SCANNER**</dt> <dt>{44328EF5-02DD-4E8D-AD5D-9249832B2ECA}</dt> </dl>          | Radio-frequency ID scanning sensors.<br/>                 |



**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_SCANNER\_GUID:

{D7A59A3C-3421-44AB-8D3A-9DE8AB6C4CAE}

This category includes the following platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                                     | Description                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_RFID_TAG_40_BIT"></span><span id="sensor_data_type_rfid_tag_40_bit"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_RFID\_TAG\_40\_BIT**</dt> <dt>(PID = 2) </dt> </dl> | **VT\_UI8**<br/> 40-bit radio frequency ID tag value.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




