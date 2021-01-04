---
title: WINBIO_INDICATOR_STATUS Constants (Winbio\_types.h)
description: Set an indicator light.
ms.assetid: 1e00ff9d-6693-4763-8ac3-b42d2a3e987d
topic_type:
- apiref
api_name:
- WINBIO_INDICATOR_ON
- WINBIO_INDICATOR_OFF
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_INDICATOR\_STATUS Constants

The following values can be used to set an indicator light. By default, sensors will not have a light on, but applications can use these values to enable or disable indicator lights. The **WINBIO\_SENSOR\_STATUS** value provides more detail about the status of an indicator light that is on. For more information, see the following functions:

-   [**SensorAdapterSetIndicatorStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_indicator_status_fn)
-   [**SensorAdapterGetIndicatorStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_get_indicator_status_fn)
-   [**SensorAdapterQueryStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_status_fn)



| Constant                                                                                                                                                                            | Description                                   |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|
| <span id="WINBIO_INDICATOR_ON"></span><span id="winbio_indicator_on"></span><dl> <dt>**WINBIO\_INDICATOR\_ON**</dt> </dl>    | The sensor indicator light is on.<br/>  |
| <span id="WINBIO_INDICATOR_OFF"></span><span id="winbio_indicator_off"></span><dl> <dt>**WINBIO\_INDICATOR\_OFF**</dt> </dl> | The sensor indicator light is off.<br/> |



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

 

 





