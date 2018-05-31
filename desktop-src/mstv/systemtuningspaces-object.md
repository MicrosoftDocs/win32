---
title: SystemTuningSpaces Object
description: SystemTuningSpaces Object
ms.assetid: 57cdd437-6219-4a72-96d9-642ff79d5879
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SystemTuningSpaces Object

The **SystemTuningSpaces** object represents the collection of tuning spaces installed on the host system.



|                           |                                                        |
|---------------------------|--------------------------------------------------------|
| Interfaces                | [**ITuningSpaceContainer**](ituningspacecontainer.md) |
| Outgoing Event Interfaces | None                                                   |
| CLSID                     | CLSID\_SystemTuningSpaces                              |



 

## Remarks

This object is used by installation applications or some other component to create new tuning spaces or enumerate or modify existing ones. A Guide Store Loader creates this object as the first step in the creation of tune requests. After creating the object, the loader uses the **ITuningSpaceContainer** interface to obtain an [**IEnumTuningSpaces**](ienumtuningspaces.md) collection of the tuning spaces installed on the host system. The loader then enumerates this collection to obtain the desired tuning space, then calls **QueryInterface** on that tuning space to obtain the required network-specific interface. It then uses this interface to create all tune requests for any program or service located in the tuning space.

## Related topics

<dl> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> <dt>

[Tuning Spaces](tuning-spaces.md)
</dt> </dl>

 

 




