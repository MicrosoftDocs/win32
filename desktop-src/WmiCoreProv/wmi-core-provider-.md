---
description: The WMI Core provider defines classes that compose the core functionality of WMI.
ms.assetid: 6EEA4284-CCFE-4206-9EAA-B4BCF988DE03
title: WMI Core Provider
ms.topic: article
ms.date: 05/31/2018
---

# WMI Core Provider

The WMI Core provider defines classes that compose the core functionality of WMI.

A majority of the WMI Core provider classes contain data supplied by the [WDM Provider](wdm-provider.md), and describe display monitors. The classes are defined in Wmi.mof and are located in the "Root\\WMI" namespace.

## In this section



| Topic                                                                                           | Description                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MSMonitorClass**](msmonitorclass.md)<br/>                                             | is an abstract WMI base class. The classes that describe video display monitors inherit from this [**MSMonitorClass**](msmonitorclass.md).<br/>                                                                         |
| [MSMCA Classes](msmca-classes.md)<br/>                                                   | a set of WMI classes that expose the Machine Check Architecture (MCA). The System Abstraction Layer (SAL) provides all events reported in the MSMCA class. The Intel Corporation develops and owns the MCA.<br/>         |
| [**FrequencyRangeDescriptor**](frequencyrangedescriptor.md)<br/>                         | represents a container for characteristics of a supported frequency range.<br/>                                                                                                                                          |
| [**SupportedDisplayFeaturesDescriptor**](supporteddisplayfeaturesdescriptor.md)<br/>     | represents the supported display features of the monitor.<br/>                                                                                                                                                           |
| [**VideoModeDescriptor**](videomodedescriptor.md)<br/>                                   | contains mode descriptor elements for the **MonitorSourceModes** array in the [**WmiMonitorListedSupportedSourceModes**](wmimonitorlistedsupportedsourcemodes.md) class.<br/>                                           |
| [**WMIEvent**](wmievent.md)<br/>                                                         | The [**WMIEvent**](wmievent.md) class is a base class from which all WMI event classes are derived.<br/>                                                                                                                |
| [**WmiMonitorAnalogVideoInputParams**](wmimonitoranalogvideoinputparams.md)<br/>         | represents the analog video input parameters of a computer monitor.<br/>                                                                                                                                                 |
| [**WmiMonitorBasicDisplayParams**](wmimonitorbasicdisplayparams.md)<br/>                 | represents the basic display features of a computer monitor.<br/>                                                                                                                                                        |
| [**WmiMonitorBrightness**](wmimonitorbrightness.md)<br/>                                 | represents the brightness parameters of a computer monitor.<br/>                                                                                                                                                         |
| [**WmiMonitorBrightnessEvent**](wmimonitorbrightnessevent.md)<br/>                       | represents a change in the brightness of a monitor.<br/>                                                                                                                                                                 |
| [**WmiMonitorBrightnessMethods**](wmimonitorbrightnessmethods.md)<br/>                   | contains methods that manage monitor brightness.<br/>                                                                                                                                                                    |
| [**WmiMonitorColorCharacteristics**](wmimonitorcolorcharacteristics.md)<br/>             | represents the International Commission on Illumination (CIE) color characteristics of a computer monitor.<br/>                                                                                                          |
| [**WmiMonitorConnectionParams**](wmimonitorconnectionparams.md)<br/>                     | contains the connection type of the monitor.<br/>                                                                                                                                                                        |
| [**WmiMonitorDescriptorMethods**](wmimonitordescriptormethods.md)<br/>                   | contains methods that obtain the raw content of Video Input Definition of Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) v.1.x standard 128-byte data blocks.<br/> |
| [**WmiMonitorDigitalVideoInputParams**](wmimonitordigitalvideoinputparams.md)<br/>       | represents input parameters for digital video.<br/>                                                                                                                                                                      |
| [**WmiMonitorID**](wmimonitorid.md)<br/>                                                 | represents the identifying information about a video monitor, such as manufacturer name, year of manufacture, or serial number.<br/>                                                                                     |
| [**WmiMonitorListedFrequencyRanges**](wmimonitorlistedfrequencyranges.md)<br/>           | lists the frequency ranges supported by the monitor.<br/>                                                                                                                                                                |
| [**WmiMonitorListedSupportedSourceModes**](wmimonitorlistedsupportedsourcemodes.md)<br/> | lists the supported source modes for a video monitor in its monitor descriptor, if any exist.<br/>                                                                                                                       |
| [**WmiMonitorRawEEdidV1Block**](wmimonitorraweedidv1block.md)<br/>                       | represents the raw data from a Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure.<br/>                                                                      |
| [**XYZinCIE**](xyzincie.md)<br/>                                                         | contains the coordinates of the display in the International Commission on Illumination (CIE) XYZ color space.<br/>                                                                                                      |



 

 

 




