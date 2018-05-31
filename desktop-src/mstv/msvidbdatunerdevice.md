---
title: MSVidBDATunerDevice
description: MSVidBDATunerDevice
ms.assetid: a29f2bb1-650e-43f8-8949-b3944c54a9e1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSVidBDATunerDevice

This topic applies to Windows XP or later.

The **MSVidBDATunerDevice** object represents a BDA-compatible digital TV tuner.



|                           |                                                                            |
|---------------------------|----------------------------------------------------------------------------|
| Interfaces                | [**IMSVidDevice2**](/windows/desktop/api/segment/nn-segment-imsviddevice2), [**IMSVidTuner**](/windows/desktop/api/segment/nn-segment-imsvidtuner) |
| Outgoing Event Interfaces | [**IMSVidTunerEvent**](/windows/desktop/api/segment/nn-segment-imsvidtunerevent)                               |



 

## Remarks

If the current input device is a BDA-compatible digital tuner, you can obtain this object by calling the [**IMSVidCtl::get\_InputActive**](imsvidctl-get-inputactive.md) method on the Video Control. Also, if the user's system contains a BDA-compatible digital tuner, you can obtain this object by calling the [**IMSVidCtl::get\_\_InputsAvailable**](imsvidctl-get--inputsavailable.md) method.

## Related topics

<dl> <dt>

[Video Control Objects (C++)](video-control-objects--c.md)
</dt> </dl>

 

 




