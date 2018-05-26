---
title: Sensor Adapter Wrappers
description: Functions that you can use to call functions on your sensor adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: 302a831c-38f7-4d32-8d9f-5ff58931224b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sensor Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your sensor adapter.



| Function                                     | Description                                                                                                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioSensorAcceptCalibrationData<br/>   | Calls the [**SensorAdapterAcceptCalibrationData**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_accept_calibration_data_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioSensorActivate<br/>                | Calls the [**SensorAdapterActivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_activate_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                               |
| WbioSensorAttach<br/>                  | Calls the [**SensorAdapterAttach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_attach_fn?branch=master) function.<br/>                                                                                                         |
| WbioSensorCancel<br/>                  | Calls the [**SensorAdapterCancel**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_cancel_fn?branch=master) function.<br/>                                                                                                         |
| WbioSensorClearContext<br/>            | Calls the [**SensorAdapterClearContext**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_clear_context_fn?branch=master) function.<br/>                                                                                             |
| WbioSensorControlUnit<br/>             | Calls the [**SensorAdapterControlUnit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_fn?branch=master) function.<br/>                                                                                               |
| WbioSensorControlUnitPrivileged<br/>   | Calls the [**SensorAdapterControlUnitPrivileged**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_privileged_fn?branch=master) function.<br/>                                                                           |
| WbioSensorDeactivate<br/>              | Calls the [**SensorAdapterDeactivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_deactivate_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                           |
| WbioSensorDetach<br/>                  | Calls the [**SensorAdapterDetach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_detach_fn?branch=master) function.<br/>                                                                                                         |
| WbioSensorExportSensorData<br/>        | Calls the [**SensorAdapterExportSensorData**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_export_sensor_data_fn?branch=master) function.<br/>                                                                                     |
| WbioSensorFinishCapture<br/>           | Calls the [**SensorAdapterFinishCapture**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_finish_capture_fn?branch=master) function.<br/>                                                                                           |
| WbioSensorNotifyPowerChange<br/>       | Calls the [**SensorAdapterNotifyPowerChange**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_notify_power_change_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 8.<br/>              |
| WbioSensorPipelineCleanup<br/>         | Calls the [**SensorAdapterPipelineCleanup**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_cleanup_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                 |
| WbioSensorPipelineInit<br/>            | Calls the [**SensorAdapterPipelineInit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_init_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                       |
| WbioSensorPushDataToEngine<br/>        | Calls the [**SensorAdapterPushDataToEngine**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_push_data_to_engine_fn?branch=master) function.<br/>                                                                                     |
| WbioSensorQueryCalibrationFormats<br/> | Calls the [**SensorAdapterQueryCalibrationFormats**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_calibration_formats_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |
| WbioSensorQueryExtendedInfo<br/>       | Calls the [**SensorAdapterQueryExtendedInfo**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_extended_info_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioSensorQueryStatus<br/>             | Calls the [**SensorAdapterQueryStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_status_fn?branch=master) function.<br/>                                                                                               |
| WbioSensorReset<br/>                   | Calls the [**SensorAdapterReset**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_reset_fn?branch=master) function.<br/>                                                                                                           |
| WbioSensorSetCalibrationFormat<br/>    | Calls the [**SensorAdapterSetCalibrationFormat**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_calibration_format_fn?branch=master) function.<br/> This wrapper function is supported starting in Windows 10.<br/>       |
| WbioSensorSetMode<br/>                 | Calls the [**SensorAdapterSetMode**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_mode_fn?branch=master) function.<br/>                                                                                                       |
| WbioSensorStartCapture<br/>            | Calls the [**SensorAdapterStartCapture**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_start_capture_fn?branch=master) function.<br/>                                                                                             |



 

There are no wrapper functions for the [**SensorAdapterGetIndicatorStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_get_indicator_status_fn?branch=master) and [**SensorAdapterSetIndicatorStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_indicator_status_fn?branch=master) functions.

## Related topics

<dl> <dt>

[Sensor Adapter Functions](sensor-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





