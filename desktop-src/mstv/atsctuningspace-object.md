---
title: ATSCTuningSpace Object
description: ATSCTuningSpace Object
ms.assetid: 8535a8c3-35df-4c6c-872a-437f5c7a2e56
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ATSCTuningSpace Object

The **ATSCTuningSpace** object represents a tuning space for ATSC networks.



|                           |                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IATSCTuningSpace**](/windows/previous-versions/tuner/nn-tuner-iatsctuningspace?branch=master), [**IMPEG2TuneRequestSupport**](/windows/previous-versions/tuner/?branch=master) |
| Outgoing Event Interfaces | None                                                                                                       |
| CLSID                     | CLSID\_ATSCTuningSpace                                                                                     |



 

## Remarks

Applications should get this object from the [SystemTuningSpaces](systemtuningspaces-object.md) collection; the CLSID is provided for clients that wish to create custom tuning spaces.

Tune request objects created by this tuning space support following interfaces:

-   [**IATSCChannelTuneRequest**](/windows/previous-versions/tuner/nn-tuner-iatscchanneltunerequest?branch=master)
-   [**IChannelTuneRequest**](/windows/previous-versions/tuner/nn-tuner-ichanneltunerequest?branch=master)
-   [**ITuneRequest**](/windows/previous-versions/tuner/nn-tuner-itunerequest?branch=master)

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




