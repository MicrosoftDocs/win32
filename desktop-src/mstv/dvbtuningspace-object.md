---
title: DVBTuningSpace Object
description: DVBTuningSpace Object
ms.assetid: 3414b1b7-21d4-4d10-b487-d6886ef36c7b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DVBTuningSpace Object

The **DVBTuningSpace** object represents a tuning space for DVB-T and DVB-C network types.



|                           |                                                                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces                | [**IDVBTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace?branch=master), [**IDVBTuningSpace2**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace2?branch=master), [**IMPEG2TuneRequestSupport**](/windows/previous-versions/tuner/?branch=master) |
| Outgoing Event Interfaces | None                                                                                                                                                   |
| CLSID                     | CLSID\_DVBTuningSpace                                                                                                                                  |



 

## Remarks

Tune request objects created by this tuning space support the [**ITuneRequest**](/windows/previous-versions/tuner/nn-tuner-itunerequest?branch=master) and [**IDVBTuneRequest**](/windows/previous-versions/tuner/nn-tuner-idvbtunerequest?branch=master) interfaces.

For DVB-S network types, use the [DVBSTuningSpace](dvbstuningspace-object.md) object.

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




