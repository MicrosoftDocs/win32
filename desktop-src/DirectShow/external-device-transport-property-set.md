---
description: External Device Transport Property Set
ms.assetid: 9c80cf59-054f-49b6-9456-ed5e091cbfaf
title: External Device Transport Property Set
ms.topic: article
ms.date: 05/31/2018
---

# External Device Transport Property Set

This property set controls the transport of data to and from an external device. In most cases, applications should not use this property set directly. Use the [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport) interface instead.

The following table lists the properties that are relevant to user-mode applications. For a complete description of this property set, refer to the Microsoft Windows Driver Development Kit DDK.



| Label | Value |
|-------------------|---------------------------|
| Property Set GUID | PROPSETID\_EXT\_TRANSPORT |



 



| Property ID                                                                           | Description                                  |
|---------------------------------------------------------------------------------------|----------------------------------------------|
| [**KSPROPERTY\_EXTXPORT\_ATN\_SEARCH**](ksproperty-extxport-atn-search.md)           | Searches for an absolute track number (ATN). |
| [**KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH**](ksproperty-extxport-timecode-search.md) | Searches for a time code.                    |



 

## Related topics

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 



