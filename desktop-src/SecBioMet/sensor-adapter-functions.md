---
title: Sensor Adapter Functions
description: A sensor adapter wraps a biometric device and provides a standard interface that enables the Windows Biometric service to configure the sensor, capture samples, and control the flow of biometric data to the processing engine.
ms.assetid: '32cf28d3-cb78-442d-81db-7827f55b0ba8'
---

# Sensor Adapter Functions

A sensor adapter wraps a biometric device and provides a standard interface that enables the Windows Biometric service to configure the sensor, capture samples, and control the flow of biometric data to the processing engine. The following functions must be implemented by the developer of the adapter. They are called by the Windows Biometric service.

## In this section



| Topic                                                                                           | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SensorAdapterAcceptCalibrationData**](sensoradapteracceptcalibrationdata.md)<br/>     | Passes calibration data from the engine adapter to the sensor adapter.<br/>                                                                                            |
| [**SensorAdapterActivate**](sensoradapteractivate.md)<br/>                               | Gives the Sensor Adapter the chance to perform any work needed to bring the sensor component out of an idle state.<br/>                                                |
| [**SensorAdapterAttach**](sensoradapterattach.md)<br/>                                   | Adds a sensor adapter to the processing pipeline of the biometric unit.<br/>                                                                                           |
| [**SensorAdapterCancel**](sensoradaptercancel.md)<br/>                                   | Cancels all pending sensor operations.<br/>                                                                                                                            |
| [**SensorAdapterClearContext**](sensoradapterclearcontext.md)<br/>                       | Prepares the processing pipeline of the biometric unit for a new operation.<br/>                                                                                       |
| [**SensorAdapterControlUnit**](sensoradaptercontrolunit.md)<br/>                         | Performs a vendor-defined control operation that does not require elevated privilege.<br/>                                                                             |
| [**SensorAdapterControlUnitPrivileged**](sensoradaptercontrolunitprivileged.md)<br/>     | Performs a vendor-defined control operation that requires elevated privilege.<br/>                                                                                     |
| [**SensorAdapterDeactivate**](sensoradapterdeactivate.md)<br/>                           | Gives the Sensor Adapter the chance to perform any work needed to put the sensor component into an idle state.<br/>                                                    |
| [**SensorAdapterDetach**](sensoradapterdetach.md)<br/>                                   | Releases adapter specific resources attached to the pipeline.<br/>                                                                                                     |
| [**SensorAdapterExportSensorData**](sensoradapterexportsensordata.md)<br/>               | Retrieves the most recently captured biometric sample formatted as a standard [**WINBIO\_BIR**](winbio-bir.md) structure.<br/>                                        |
| [**SensorAdapterFinishCapture**](sensoradapterfinishcapture.md)<br/>                     | Retrieves a value that indicates whether the sensor indicator is on or off.<br/>                                                                                       |
| [**SensorAdapterGetIndicatorStatus**](sensoradaptergetindicatorstatus.md)<br/>           | Retrieves a value that indicates whether the sensor indicator is on or off.<br/>                                                                                       |
| [*SensorAdapterNotifyPowerChange*](sensoradapternotifypowerchange.md)<br/>               | Receives notification about a change in the computer power state and prepares the sensor adapter accordingly.<br/>                                                     |
| [**SensorAdapterPipelineCleanup**](sensoradapterpipelinecleanup.md)<br/>                 | Gives the Sensor Adapter the chance to perform any cleanup in that requires help from the Engine or Storage adapter components.<br/>                                   |
| [**SensorAdapterPipelineInit**](sensoradapterpipelineinit.md)<br/>                       | Gives the Sensor Adapter the chance to perform any initialization that remains incomplete, and which requires help from the Engine or Storage adapter components.<br/> |
| [**SensorAdapterPushDataToEngine**](sensoradapterpushdatatoengine.md)<br/>               | Makes the current contents of the sample buffer available to the engine adapter.<br/>                                                                                  |
| [**SensorAdapterQueryCalibrationFormats**](sensoradapterquerycalibrationformats.md)<br/> | Determines the set of calibration formats supported by the Sensor Adapter.<br/>                                                                                        |
| [**SensorAdapterQueryExtendedInfo**](sensoradapterqueryextendedinfo.md)<br/>             | Determines the capabilities and limitations of the biometric sensor component.<br/>                                                                                    |
| [**SensorAdapterQueryStatus**](sensoradapterquerystatus.md)<br/>                         | Retrieves information about the current status of the sensor device.<br/>                                                                                              |
| [**SensorAdapterReset**](sensoradapterreset.md)<br/>                                     | Reinitializes the sensor.<br/>                                                                                                                                         |
| [**SensorAdapterSetCalibrationFormat**](sensoradaptersetcalibrationformat.md)<br/>       | Notifies the sensor adapter that a particular calibration data format has been selected by the engine adapter.<br/>                                                    |
| [**SensorAdapterSetIndicatorStatus**](sensoradaptersetindicatorstatus.md)<br/>           | Toggles the sensor indicator on or off.<br/>                                                                                                                           |
| [**SensorAdapterSetMode**](sensoradaptersetmode.md)<br/>                                 | Sets the sensor adapter mode.<br/>                                                                                                                                     |
| [**SensorAdapterStartCapture**](sensoradapterstartcapture.md)<br/>                       | Begins an asynchronous biometric capture.<br/>                                                                                                                         |
| [**WbioQuerySensorInterface**](wbioquerysensorinterface.md)<br/>                         | Retrieves a pointer to the [**WINBIO\_SENSOR\_INTERFACE**](winbio-sensor-interface.md) structure for the sensor adapter.<br/>                                         |



 

## Related topics

<dl> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





