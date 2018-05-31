---
title: DVBTuningSpace Object
description: DVBTuningSpace Object
ms.assetid: 3414b1b7-21d4-4d10-b487-d6886ef36c7b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DVBTuningSpace Object

The **DVBTuningSpace** object represents a tuning space for DVB-T and DVB-C network types.



|                           |                                                                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IDVBTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace), [**IDVBTuningSpace2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace2), [**IMPEG2TuneRequestSupport**](/previous-versions/windows/desktop/api/tuner/) |
| Outgoing Event Interfaces | None                                                                                                                                                   |
| CLSID                     | CLSID\_DVBTuningSpace                                                                                                                                  |



 

## Remarks

Tune request objects created by this tuning space support the [**ITuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-itunerequest) and [**IDVBTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtunerequest) interfaces.

For DVB-S network types, use the [DVBSTuningSpace](dvbstuningspace-object.md) object.

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




