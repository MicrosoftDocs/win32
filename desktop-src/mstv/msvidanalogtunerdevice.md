---
title: MSVidAnalogTunerDevice
description: MSVidAnalogTunerDevice
ms.assetid: 432b16f1-a732-4610-9214-363b3a313a18
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidAnalogTunerDevice

This topic applies to Windows XP or later.

The **MSVidAnalogTunerDevice** object represents a non-BDA analog TV tuner.



|                           |                                                                                                                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IMSVidAnalogTuner**](/windows/win32/segment/nn-segment-imsvidanalogtuner?branch=master), [**IMSVidAnalogTuner2**](/windows/win32/segment/nn-segment-imsvidanalogtuner2?branch=master), [**IMSVidDevice2**](/windows/win32/segment/nn-segment-imsviddevice2?branch=master), [**IScanningTuner**](/windows/previous-versions/tuner/nn-tuner-iscanningtuner?branch=master) |
| Outgoing Event Interfaces | [**IMSVidAnalogTunerEvent**](/windows/win32/segment/?branch=master)                                                                                                                           |



 

## Remarks

If the current input device is a non-BDA analog tuner, you can obtain this object by calling the [**IMSVidCtl::get\_InputActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_inputactive?branch=master) method on the Video Control. Also, if the user's system contains a non-BDA analog tuner, you can obtain this object by calling the [**IMSVidCtl::get\_\_InputsAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get__inputsavailable?branch=master) method.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




