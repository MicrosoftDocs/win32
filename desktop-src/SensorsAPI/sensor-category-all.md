---
description: The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.
ms.assetid: e2d9fe6d-450a-446b-968b-0924116af6fe
title: SENSOR_CATEGORY_ALL (Sensors.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SENSOR\_CATEGORY\_ALL

The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.

**Platform-Defined Property Keys**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_COMMON\_GUID:

{DB5E0CF2-CF1F-4C18-B46C-D86011D62150}

The following table describes platform-defined data fields.



| Data field name and PID                                                                                                                                                                                                                                                 | Description                                                                                                                                                                        |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SENSOR_DATA_TYPE_TIMESTAMP"></span><span id="sensor_data_type_timestamp"></span><dl> <dt>**SENSOR\_DATA\_TYPE\_TIMESTAMP**</dt> <dt>(PID = 2 ) </dt> </dl> | **VT\_FILETIME**<br/> Required for all data reports. Marks each data report with the time the data report was created in Coordinated Universal Time (UTC) format.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Sensors.h</dt> </dl> |



 

 




