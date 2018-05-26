---
title: MSVidBDATunerDevice
description: MSVidBDATunerDevice
ms.assetid: a29f2bb1-650e-43f8-8949-b3944c54a9e1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSVidBDATunerDevice

This topic applies to Windows XP or later.

The **MSVidBDATunerDevice** object represents a BDA-compatible digital TV tuner.



|                           |                                                                            |
|---------------------------|----------------------------------------------------------------------------|
| Interfaces                | [**IMSVidDevice2**](/windows/win32/segment/nn-segment-imsviddevice2?branch=master), [**IMSVidTuner**](/windows/win32/segment/nn-segment-imsvidtuner?branch=master) |
| Outgoing Event Interfaces | [**IMSVidTunerEvent**](/windows/win32/segment/nn-segment-imsvidtunerevent?branch=master)                               |



 

## Remarks

If the current input device is a BDA-compatible digital tuner, you can obtain this object by calling the [**IMSVidCtl::get\_InputActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_inputactive?branch=master) method on the Video Control. Also, if the user's system contains a BDA-compatible digital tuner, you can obtain this object by calling the [**IMSVidCtl::get\_\_InputsAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get__inputsavailable?branch=master) method.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




