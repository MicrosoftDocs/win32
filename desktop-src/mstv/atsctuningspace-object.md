---
title: ATSCTuningSpace Object
description: ATSCTuningSpace Object
ms.assetid: 8535a8c3-35df-4c6c-872a-437f5c7a2e56
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ATSCTuningSpace Object

The **ATSCTuningSpace** object represents a tuning space for ATSC networks.



|                           |                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IATSCTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsctuningspace), [**IMPEG2TuneRequestSupport**](/previous-versions/windows/desktop/api/tuner/) |
| Outgoing Event Interfaces | None                                                                                                       |
| CLSID                     | CLSID\_ATSCTuningSpace                                                                                     |



 

## Remarks

Applications should get this object from the [SystemTuningSpaces](systemtuningspaces-object.md) collection; the CLSID is provided for clients that wish to create custom tuning spaces.

Tune request objects created by this tuning space support following interfaces:

-   [**IATSCChannelTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatscchanneltunerequest)
-   [**IChannelTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ichanneltunerequest)
-   [**ITuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-itunerequest)

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




