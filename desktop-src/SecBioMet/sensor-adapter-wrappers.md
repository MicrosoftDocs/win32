---
title: Sensor Adapter Wrappers
description: Functions that you can use to call functions on your sensor adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: '302a831c-38f7-4d32-8d9f-5ff58931224b'
---

# Sensor Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your sensor adapter.



| Function                                     | Description                                                                                                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioSensorAcceptCalibrationData<br/>   | Calls the [**SensorAdapterAcceptCalibrationData**](sensoradapteracceptcalibrationdata.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>     |
| WbioSensorActivate<br/>                | Calls the [**SensorAdapterActivate**](sensoradapteractivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                               |
| WbioSensorAttach<br/>                  | Calls the [**SensorAdapterAttach**](sensoradapterattach.md) function.<br/>                                                                                                         |
| WbioSensorCancel<br/>                  | Calls the [**SensorAdapterCancel**](sensoradaptercancel.md) function.<br/>                                                                                                         |
| WbioSensorClearContext<br/>            | Calls the [**SensorAdapterClearContext**](sensoradapterclearcontext.md) function.<br/>                                                                                             |
| WbioSensorControlUnit<br/>             | Calls the [**SensorAdapterControlUnit**](sensoradaptercontrolunit.md) function.<br/>                                                                                               |
| WbioSensorControlUnitPrivileged<br/>   | Calls the [**SensorAdapterControlUnitPrivileged**](sensoradaptercontrolunitprivileged.md) function.<br/>                                                                           |
| WbioSensorDeactivate<br/>              | Calls the [**SensorAdapterDeactivate**](sensoradapterdeactivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                           |
| WbioSensorDetach<br/>                  | Calls the [**SensorAdapterDetach**](sensoradapterdetach.md) function.<br/>                                                                                                         |
| WbioSensorExportSensorData<br/>        | Calls the [**SensorAdapterExportSensorData**](sensoradapterexportsensordata.md) function.<br/>                                                                                     |
| WbioSensorFinishCapture<br/>           | Calls the [**SensorAdapterFinishCapture**](sensoradapterfinishcapture.md) function.<br/>                                                                                           |
| WbioSensorNotifyPowerChange<br/>       | Calls the [**SensorAdapterNotifyPowerChange**](sensoradapternotifypowerchange.md) function.<br/> This wrapper function is supported starting in Windows 8.<br/>              |
| WbioSensorPipelineCleanup<br/>         | Calls the [**SensorAdapterPipelineCleanup**](sensoradapterpipelinecleanup.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                 |
| WbioSensorPipelineInit<br/>            | Calls the [**SensorAdapterPipelineInit**](sensoradapterpipelineinit.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                       |
| WbioSensorPushDataToEngine<br/>        | Calls the [**SensorAdapterPushDataToEngine**](sensoradapterpushdatatoengine.md) function.<br/>                                                                                     |
| WbioSensorQueryCalibrationFormats<br/> | Calls the [**SensorAdapterQueryCalibrationFormats**](sensoradapterquerycalibrationformats.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |
| WbioSensorQueryExtendedInfo<br/>       | Calls the [**SensorAdapterQueryExtendedInfo**](sensoradapterqueryextendedinfo.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioSensorQueryStatus<br/>             | Calls the [**SensorAdapterQueryStatus**](sensoradapterquerystatus.md) function.<br/>                                                                                               |
| WbioSensorReset<br/>                   | Calls the [**SensorAdapterReset**](sensoradapterreset.md) function.<br/>                                                                                                           |
| WbioSensorSetCalibrationFormat<br/>    | Calls the [**SensorAdapterSetCalibrationFormat**](sensoradaptersetcalibrationformat.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>       |
| WbioSensorSetMode<br/>                 | Calls the [**SensorAdapterSetMode**](sensoradaptersetmode.md) function.<br/>                                                                                                       |
| WbioSensorStartCapture<br/>            | Calls the [**SensorAdapterStartCapture**](sensoradapterstartcapture.md) function.<br/>                                                                                             |



 

There are no wrapper functions for the [**SensorAdapterGetIndicatorStatus**](sensoradaptergetindicatorstatus.md) and [**SensorAdapterSetIndicatorStatus**](sensoradaptersetindicatorstatus.md) functions.

## Related topics

<dl> <dt>

[Sensor Adapter Functions](sensor-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





