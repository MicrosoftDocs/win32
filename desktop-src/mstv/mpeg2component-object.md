---
title: MPEG2Component Object
description: MPEG2Component Object
ms.assetid: 901636df-7b37-40e8-b194-2dfa50fdf8fd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MPEG2Component Object

The **MPEG2Component** object represents a component in an MPEG-2 stream.



|                           |                                            |
|---------------------------|--------------------------------------------|
| Interfaces                | [**IMPEG2Component**](impeg2component.md) |
| Outgoing Event Interfaces | None                                       |
| CLSID                     | CLSID\_MPEG2Component                      |



 

## Remarks

To get this object from an existing tune request, use the [**ITuneRequest::get\_Components**](itunerequest-get-components.md) method to enumerate the components collection on the tune request. The CLSID is provided for guide store loaders that need to set the component information for a tune request.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




