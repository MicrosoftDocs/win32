---
title: MPEG2Component Object
description: MPEG2Component Object
ms.assetid: 901636df-7b37-40e8-b194-2dfa50fdf8fd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPEG2Component Object

The **MPEG2Component** object represents a component in an MPEG-2 stream.



|                           |                                            |
|---------------------------|--------------------------------------------|
| Interfaces                | [**IMPEG2Component**](/windows/previous-versions/tuner/nn-tuner-impeg2component?branch=master) |
| Outgoing Event Interfaces | None                                       |
| CLSID                     | CLSID\_MPEG2Component                      |



 

## Remarks

To get this object from an existing tune request, use the [**ITuneRequest::get\_Components**](/windows/previous-versions/tuner/nf-tuner-itunerequest-get_components?branch=master) method to enumerate the components collection on the tune request. The CLSID is provided for guide store loaders that need to set the component information for a tune request.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




