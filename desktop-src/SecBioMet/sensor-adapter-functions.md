---
title: Sensor Adapter Functions
description: A sensor adapter wraps a biometric device and provides a standard interface that enables the Windows Biometric service to configure the sensor, capture samples, and control the flow of biometric data to the processing engine.
ms.assetid: 32cf28d3-cb78-442d-81db-7827f55b0ba8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sensor Adapter Functions

A sensor adapter wraps a biometric device and provides a standard interface that enables the Windows Biometric service to configure the sensor, capture samples, and control the flow of biometric data to the processing engine. The following functions must be implemented by the developer of the adapter. They are called by the Windows Biometric service.

## In this section



| Topic                                                                                           | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SensorAdapterAcceptCalibrationData**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_accept_calibration_data_fn?branch=master)<br/>     | Passes calibration data from the engine adapter to the sensor adapter.<br/>                                                                                            |
| [**SensorAdapterActivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_activate_fn?branch=master)<br/>                               | Gives the Sensor Adapter the chance to perform any work needed to bring the sensor component out of an idle state.<br/>                                                |
| [**SensorAdapterAttach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_attach_fn?branch=master)<br/>                                   | Adds a sensor adapter to the processing pipeline of the biometric unit.<br/>                                                                                           |
| [**SensorAdapterCancel**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_cancel_fn?branch=master)<br/>                                   | Cancels all pending sensor operations.<br/>                                                                                                                            |
| [**SensorAdapterClearContext**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_clear_context_fn?branch=master)<br/>                       | Prepares the processing pipeline of the biometric unit for a new operation.<br/>                                                                                       |
| [**SensorAdapterControlUnit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_fn?branch=master)<br/>                         | Performs a vendor-defined control operation that does not require elevated privilege.<br/>                                                                             |
| [**SensorAdapterControlUnitPrivileged**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_control_unit_privileged_fn?branch=master)<br/>     | Performs a vendor-defined control operation that requires elevated privilege.<br/>                                                                                     |
| [**SensorAdapterDeactivate**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_deactivate_fn?branch=master)<br/>                           | Gives the Sensor Adapter the chance to perform any work needed to put the sensor component into an idle state.<br/>                                                    |
| [**SensorAdapterDetach**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_detach_fn?branch=master)<br/>                                   | Releases adapter specific resources attached to the pipeline.<br/>                                                                                                     |
| [**SensorAdapterExportSensorData**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_export_sensor_data_fn?branch=master)<br/>               | Retrieves the most recently captured biometric sample formatted as a standard [**WINBIO\_BIR**](winbio-bir.md) structure.<br/>                                        |
| [**SensorAdapterFinishCapture**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_finish_capture_fn?branch=master)<br/>                     | Retrieves a value that indicates whether the sensor indicator is on or off.<br/>                                                                                       |
| [**SensorAdapterGetIndicatorStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_get_indicator_status_fn?branch=master)<br/>           | Retrieves a value that indicates whether the sensor indicator is on or off.<br/>                                                                                       |
| [*SensorAdapterNotifyPowerChange*](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_notify_power_change_fn?branch=master)<br/>               | Receives notification about a change in the computer power state and prepares the sensor adapter accordingly.<br/>                                                     |
| [**SensorAdapterPipelineCleanup**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_cleanup_fn?branch=master)<br/>                 | Gives the Sensor Adapter the chance to perform any cleanup in that requires help from the Engine or Storage adapter components.<br/>                                   |
| [**SensorAdapterPipelineInit**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_pipeline_init_fn?branch=master)<br/>                       | Gives the Sensor Adapter the chance to perform any initialization that remains incomplete, and which requires help from the Engine or Storage adapter components.<br/> |
| [**SensorAdapterPushDataToEngine**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_push_data_to_engine_fn?branch=master)<br/>               | Makes the current contents of the sample buffer available to the engine adapter.<br/>                                                                                  |
| [**SensorAdapterQueryCalibrationFormats**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_calibration_formats_fn?branch=master)<br/> | Determines the set of calibration formats supported by the Sensor Adapter.<br/>                                                                                        |
| [**SensorAdapterQueryExtendedInfo**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_extended_info_fn?branch=master)<br/>             | Determines the capabilities and limitations of the biometric sensor component.<br/>                                                                                    |
| [**SensorAdapterQueryStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_query_status_fn?branch=master)<br/>                         | Retrieves information about the current status of the sensor device.<br/>                                                                                              |
| [**SensorAdapterReset**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_reset_fn?branch=master)<br/>                                     | Reinitializes the sensor.<br/>                                                                                                                                         |
| [**SensorAdapterSetCalibrationFormat**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_calibration_format_fn?branch=master)<br/>       | Notifies the sensor adapter that a particular calibration data format has been selected by the engine adapter.<br/>                                                    |
| [**SensorAdapterSetIndicatorStatus**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_indicator_status_fn?branch=master)<br/>           | Toggles the sensor indicator on or off.<br/>                                                                                                                           |
| [**SensorAdapterSetMode**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_set_mode_fn?branch=master)<br/>                                 | Sets the sensor adapter mode.<br/>                                                                                                                                     |
| [**SensorAdapterStartCapture**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_start_capture_fn?branch=master)<br/>                       | Begins an asynchronous biometric capture.<br/>                                                                                                                         |
| [**WbioQuerySensorInterface**](/windows/win32/Winbio_adapter/nf-winbio_adapter-wbioquerysensorinterface?branch=master)<br/>                         | Retrieves a pointer to the [**WINBIO\_SENSOR\_INTERFACE**](/windows/win32/Winbio_adapter/ns-winbio_adapter-_winbio_sensor_interface?branch=master) structure for the sensor adapter.<br/>                                         |



 

## Related topics

<dl> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





