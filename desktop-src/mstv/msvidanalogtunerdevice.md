---
title: MSVidAnalogTunerDevice
description: MSVidAnalogTunerDevice
ms.assetid: '432b16f1-a732-4610-9214-363b3a313a18'
---

# MSVidAnalogTunerDevice

This topic applies to Windows XP or later.

The **MSVidAnalogTunerDevice** object represents a non-BDA analog TV tuner.



|                           |                                                                                                                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IMSVidAnalogTuner**](imsvidanalogtuner.md), [**IMSVidAnalogTuner2**](imsvidanalogtuner2.md), [**IMSVidDevice2**](imsviddevice2.md), [**IScanningTuner**](iscanningtuner.md) |
| Outgoing Event Interfaces | [**IMSVidAnalogTunerEvent**](imsvidanalogtunerevent.md)                                                                                                                           |



 

## Remarks

If the current input device is a non-BDA analog tuner, you can obtain this object by calling the [**IMSVidCtl::get\_InputActive**](imsvidctl-get-inputactive.md) method on the Video Control. Also, if the user's system contains a non-BDA analog tuner, you can obtain this object by calling the [**IMSVidCtl::get\_\_InputsAvailable**](imsvidctl-get--inputsavailable.md) method.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




