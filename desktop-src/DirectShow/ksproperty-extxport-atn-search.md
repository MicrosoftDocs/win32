---
Description: This property sends a command to the device to search for an absolute track number (ATN). The UVC device driver supports this property.
ms.assetid: 209e0aa3-d7a3-4b5c-ae5a-5063a3804a9d
title: KSPROPERTY\_EXTXPORT\_ATN\_SEARCH
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# KSPROPERTY\_EXTXPORT\_ATN\_SEARCH

This property sends a command to the device to search for an absolute track number (ATN). The UVC device driver supports this property.



|                   |                                       |
|-------------------|---------------------------------------|
| Property Set GUID | PROPSETID\_EXT\_TRANSPORT             |
| Property ID       | KSPROPERTY\_EXTXPORT\_ATN\_SEARCH     |
| Data Type         | **KSPROPERTY\_EXTXPORT\_S** structure |



 

## Remarks

Set the **dwAbsTrackNumber** member of the **KSPROPERTY\_EXTXPORT\_S** structure to the following value:


```
(absolute track number << 1) + continuity bit
```



The UVC specification does not define how the device uses the continuity bit. The **KSPROPERTY\_EXTXPORT\_S** structure is described in the Windows DDK.

## See also

<dl> <dt>

[External Device Transport Property Set](external-device-transport-property-set.md)
</dt> </dl>

 

 



