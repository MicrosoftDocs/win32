---
title: Sensor Adapter Wrappers
description: Functions that you can use to call functions on your sensor adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: 302a831c-38f7-4d32-8d9f-5ff58931224b
ms.topic: article
ms.date: 05/31/2018
---

# Sensor Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your sensor adapter.



| Function                                     | Description                                                                                                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioSensorAcceptCalibrationData<br/>   | Calls the [**SensorAdapterAcceptCalibrationData**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_accept_calibration_data_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioSensorActivate<br/>                | Calls the [**SensorAdapterActivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_activate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                               |
| WbioSensorAttach<br/>                  | Calls the [**SensorAdapterAttach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_attach_fn) function.<br/>                                                                                                         |
| WbioSensorCancel<br/>                  | Calls the [**SensorAdapterCancel**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_cancel_fn) function.<br/>                                                                                                         |
| WbioSensorClearContext<br/>            | Calls the [**SensorAdapterClearContext**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_clear_context_fn) function.<br/>                                                                                             |
| WbioSensorControlUnit<br/>             | Calls the [**SensorAdapterControlUnit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_fn) function.<br/>                                                                                               |
| WbioSensorControlUnitPrivileged<br/>   | Calls the [**SensorAdapterControlUnitPrivileged**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_privileged_fn) function.<br/>                                                                           |
| WbioSensorDeactivate<br/>              | Calls the [**SensorAdapterDeactivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_deactivate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                           |
| WbioSensorDetach<br/>                  | Calls the [**SensorAdapterDetach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_detach_fn) function.<br/>                                                                                                         |
| WbioSensorExportSensorData<br/>        | Calls the [**SensorAdapterExportSensorData**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_export_sensor_data_fn) function.<br/>                                                                                     |
| WbioSensorFinishCapture<br/>           | Calls the [**SensorAdapterFinishCapture**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_finish_capture_fn) function.<br/>                                                                                           |
| WbioSensorNotifyPowerChange<br/>       | Calls the [**SensorAdapterNotifyPowerChange**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_notify_power_change_fn) function.<br/> This wrapper function is supported starting in Windows 8.<br/>              |
| WbioSensorPipelineCleanup<br/>         | Calls the [**SensorAdapterPipelineCleanup**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_cleanup_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                 |
| WbioSensorPipelineInit<br/>            | Calls the [**SensorAdapterPipelineInit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_init_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                       |
| WbioSensorPushDataToEngine<br/>        | Calls the [**SensorAdapterPushDataToEngine**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_push_data_to_engine_fn) function.<br/>                                                                                     |
| WbioSensorQueryCalibrationFormats<br/> | Calls the [**SensorAdapterQueryCalibrationFormats**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_calibration_formats_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |
| WbioSensorQueryExtendedInfo<br/>       | Calls the [**SensorAdapterQueryExtendedInfo**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_extended_info_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioSensorQueryStatus<br/>             | Calls the [**SensorAdapterQueryStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_status_fn) function.<br/>                                                                                               |
| WbioSensorReset<br/>                   | Calls the [**SensorAdapterReset**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_reset_fn) function.<br/>                                                                                                           |
| WbioSensorSetCalibrationFormat<br/>    | Calls the [**SensorAdapterSetCalibrationFormat**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_calibration_format_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>       |
| WbioSensorSetMode<br/>                 | Calls the [**SensorAdapterSetMode**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_mode_fn) function.<br/>                                                                                                       |
| WbioSensorStartCapture<br/>            | Calls the [**SensorAdapterStartCapture**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_start_capture_fn) function.<br/>                                                                                             |



 

There are no wrapper functions for the [**SensorAdapterGetIndicatorStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_get_indicator_status_fn) and [**SensorAdapterSetIndicatorStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_indicator_status_fn) functions.

## Related topics

<dl> <dt>

[Sensor Adapter Functions](sensor-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





