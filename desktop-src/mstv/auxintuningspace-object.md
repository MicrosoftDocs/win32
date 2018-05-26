---
title: AuxInTuningSpace Object
description: AuxInTuningSpace Object
ms.assetid: f3d0948c-aa40-4a19-a620-af75495ecde2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AuxInTuningSpace Object

The **AuxInTuningSpace** object represents an auxiliary video input such as composite video or S-video.



|                           |                                                                                                  |
|---------------------------|--------------------------------------------------------------------------------------------------|
| Interfaces                | [**IAuxInTuningSpace**](/windows/previous-versions/tuner/?branch=master), [**IAuxInTuningSpace2**](/windows/previous-versions/tuner/nn-tuner-iauxintuningspace2?branch=master) |
| Outgoing Event Interfaces | None                                                                                             |



 

## Remarks

Applications should get this object from the [SystemTuningSpaces](systemtuningspaces-object.md) collection. See [Default Tuning Spaces](default-tuning-spaces.md).

Tune request objects created by this tuning space support the [**ITuneRequest**](/windows/previous-versions/tuner/nn-tuner-itunerequest?branch=master) and [**IChannelTuneRequest**](/windows/previous-versions/tuner/nn-tuner-ichanneltunerequest?branch=master) interfaces. The channel number indicates the input source:



| Channel Number | Input           |
|----------------|-----------------|
| 0              | S-video         |
| 1              | Composite video |



 

When the Video Control receives an AuxIn tune request, it creates a WDM analog TV filter graph and uses the crossbar filter to select the input.

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




